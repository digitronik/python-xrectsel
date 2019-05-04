#!/usr/bin/env python

import sys
from Xlib import X, display, Xcursorfont


def coordinates(start_point, end_point):
    X = dict(x=0, y=0)
    Y = dict(x=0, y=0)

    X["x"] = end_point["x"] if start_point["x"] > end_point["x"] else start_point["x"]
    Y["x"] = start_point["x"] if start_point["x"] > end_point["x"] else end_point["x"]

    X["y"] = end_point["y"] if start_point["y"] > end_point["y"] else start_point["y"]
    Y["y"] = start_point["y"] if start_point["y"] > end_point["y"] else end_point["y"]

    return {"start": X, "end": Y, "width": Y["x"] - X["x"], "height": Y["y"] - X["y"]}


class XRectSel(object):
    def __init__(self, _display=None, screen=None):
        self.display = _display if _display else display.Display()
        self.screen = screen if screen else self.display.screen()
        self.window = self.screen.root

        self.window.grab_pointer(
            1,
            X.PointerMotionMask | X.ButtonReleaseMask | X.ButtonPressMask,
            X.GrabModeAsync,
            X.GrabModeAsync,
            X.NONE,
            self._cursor,
            X.CurrentTime,
        )

        self.window.grab_keyboard(1, X.GrabModeAsync, X.GrabModeAsync, X.CurrentTime)

        self.gc = self.window.create_gc(
            line_width=1,
            line_style=X.LineSolid,
            fill_style=X.FillOpaqueStippled,
            fill_rule=X.WindingRule,
            cap_style=X.CapButt,
            join_style=X.JoinMiter,
            foreground=self._foreground,
            background=self.screen.black_pixel,
            function=X.GXxor,
            graphics_exposures=False,
            subwindow_mode=X.IncludeInferiors,
        )

    @property
    def _foreground(self):
        alloc_colour = self.screen.default_colormap.alloc_color(0, 0, 0)
        return alloc_colour.pixel ^ 0xFFFFFF

    @property
    def _cursor(self):
        font = self.display.open_font("cursor")
        return font.create_glyph_cursor(
            font, Xcursorfont.crosshair, Xcursorfont.crosshair + 1, (65535, 65535, 65535), (0, 0, 0)
        )

    def draw_rectangle(self, start_point, end_point):
        coords = coordinates(start_point, end_point)
        self.window.rectangle(
            self.gc, coords["start"]["x"], coords["start"]["y"], coords["width"], coords["height"]
        )

    def select(self):
        start_point = {}
        end_point = {}
        tmp_point = {}
        drawlimit = 10
        i = 0

        while not end_point:
            event = self.display.next_event()

            if event.type == X.DestroyNotify or event.type == X.KeyPress:
                # Exit for events like Destroy Notification or any Key event.
                sys.exit(0)

            elif event.type == X.ButtonPress:
                # As mouse button button push
                if event.detail == 1:
                    # Left button
                    start_point = dict(x=event.root_x, y=event.root_y)

                elif event.detail == 3:
                    # Right button
                    sys.exit(0)

            elif event.type == X.MotionNotify and start_point:
                # Capture motion of mouse
                i = i + 1
                if i % drawlimit != 0:
                    continue

                if tmp_point:
                    self.draw_rectangle(start_point, tmp_point)
                    tmp_point = None

                tmp_point = dict(x=event.root_x, y=event.root_y)
                self.draw_rectangle(start_point, tmp_point)

            # Mouse button release
            elif event.type == X.ButtonRelease:
                if tmp_point:
                    self.draw_rectangle(start_point, tmp_point)

                end_point = dict(x=event.root_x, y=event.root_y)

        self.display.flush()
        return start_point, end_point
