import click
from xrectsel import XRectSel

format_help = (
    "Format string...\n"
    "%x - start x-coordinate\n"
    "%y - start y-coordinate\n"
    "%X - start\n"
    "%Y - end\n"
    "%w - width\n"
    "%h - height"
)


@click.command(help="xrectsel")
@click.option("-f", "--format", default="%wx%h+%x+%y", help=format_help)
def cli(format):
    xrect = XRectSel()
    geormetry = xrect.select()

    if geormetry["width"] <= 1 or geormetry["height"] <= 1:
        pass
    else:
        click.echo(
            format.replace("%x", str(geormetry["start"]["x"]))
            .replace("%y", str(geormetry["start"]["y"]))
            .replace("%X", str(geormetry["start"]))
            .replace("%Y", str(geormetry["end"]))
            .replace("%w", str(geormetry["width"]))
            .replace("%h", str(geormetry["height"]))
        )
