from xrectsel import XRectSel, coordinates


def cli():
    xrect = XRectSel()
    start, end = xrect.select()
    geormetry = coordinates(start, end)

    if geormetry["width"] <= 1 or geormetry["height"] <= 1:
        pass
    else:
        print(
            "{} {} {} {}".format(
                geormetry["start"]["x"],
                geormetry["start"]["y"],
                geormetry["width"],
                geormetry["height"],
            )
        )
