import subprocess

import pytest

from xrectsel import XRectSel

CO_ORD = {"start": {"x": 412, "y": 419}, "end": {"x": 1014, "y": 458}, "width": 602, "height": 39}


def test_forground():
    xrect = XRectSel()
    assert xrect._foreground == 16777215


def test_grab_pointer():
    xrect = XRectSel()
    with xrect.grab_mouse_keyboard():
        # just run no operation; if not display not captured it will raise error
        xrect.display.no_operation()


def test_coordinate():
    xrect = XRectSel()
    co_ord = xrect.coordinates(CO_ORD["start"], CO_ORD["end"])
    assert co_ord == CO_ORD


def test_draw_rectangle():
    xrect = XRectSel()
    xrect.draw_rectangle(CO_ORD)


def test_xrectsel_command():
    # TODO: find easy way to click and drag
    with pytest.raises(
        subprocess.TimeoutExpired, match="Command 'xrectsel' timed out after 5 seconds"
    ):
        subprocess.run("xrectsel", stdout=subprocess.PIPE, timeout=5)


def test_xrectsel_help():
    result = subprocess.run(["xrectsel", "--help"], stdout=subprocess.PIPE)
    assert result.returncode == 0
    assert "-f, --format TEXT" in result.stdout.decode().strip()
