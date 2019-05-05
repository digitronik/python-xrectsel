from xrectsel import XRectSel


def cli():
    xrect = XRectSel()
    geormetry = xrect.select()

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
