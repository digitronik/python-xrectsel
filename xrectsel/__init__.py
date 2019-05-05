import sys
from Xlib import X, display, Xcursorfont


def coordinates(start_point, end_point):
    """
    :param start_point: Start co-ordinates of rectangle
    :param end_point: End co-ordinates of rectangle
    :return: dict of start co-ordinates, end co-ordinates, width, height of rectangle.
    """
    X = dict(x=0, y=0)
    Y = dict(x=0, y=0)

    X["x"] = end_point["x"] if start_point["x"] > end_point["x"] else start_point["x"]
    Y["x"] = start_point["x"] if start_point["x"] > end_point["x"] else end_point["x"]

    X["y"] = end_point["y"] if start_point["y"] > end_point["y"] else start_point["y"]
    Y["y"] = start_point["y"] if start_point["y"] > end_point["y"] else end_point["y"]

    return {"start": X, "end": Y, "width": Y["x"] - X["x"], "height": Y["y"] - X["y"]}


class XRectSel(object):
    """
    Base class for python-xrectsel

    TODO: Enhancement like colors, pixels customization.
    """

    def __init__(self, _display=None):
        """
        :param _display: custom display else it will take default
        """
        self.display = _display if _display else display.Display()
        self.screen = self.display.screen()
        self.window = self.screen.root

        # Grab mouse pointer
        self.window.grab_pointer(
            1,
            X.PointerMotionMask | X.ButtonReleaseMask | X.ButtonPressMask,
            X.GrabModeAsync,
            X.GrabModeAsync,
            X.NONE,
            self._cursor,
            X.CurrentTime,
        )

        # Grab keyboard
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

    def draw_rectangle(self, coords):
        self.window.rectangle(
            self.gc, coords["start"]["x"], coords["start"]["y"], coords["width"], coords["height"]
        )

    def select(self):
        """
        Draw rectangle with mouse events

        :return: dict of start co-ordinates, end co-ordinates, width, height of rectangle.
        """
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
                    coords = coordinates(start_point, tmp_point)
                    self.draw_rectangle(coords)
                    tmp_point = None

                tmp_point = dict(x=event.root_x, y=event.root_y)
                coords = coordinates(start_point, tmp_point)
                self.draw_rectangle(coords)

            # Mouse button release
            elif event.type == X.ButtonRelease:
                if tmp_point:
                    coords = coordinates(start_point, tmp_point)
                    self.draw_rectangle(coords)
                end_point = dict(x=event.root_x, y=event.root_y)

        self.display.flush()
        self.display.close()
        return coordinates(start_point, end_point)


if __name__ == "__main__":
    print(XRectSel().select())
