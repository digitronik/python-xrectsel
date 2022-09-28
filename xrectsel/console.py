import click

from xrectsel import XRectSel

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
CURSOR_ICONS = ["crosshair", "cross", "pencil", "dotbox"]

FORMAT_HELP = """Format output string with fallowing options:

        %x - start x-coordinate

        %y - start y-coordinate

        %X - start

        %Y - end

        %w - width

        %h - height

        Note: default output is in "%wx%h+%x+%y" format.
        """


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-f", "--format", default="%wx%h+%x+%y", help=FORMAT_HELP)
@click.option(
    "-ci",
    "--cursor-icon",
    default="crosshair",
    type=click.Choice(CURSOR_ICONS),
    help="Select cursor icon",
)
@click.option(
    "-cf",
    "--cursor-foreground",
    default=(65535, 65535, 65535),
    type=click.Tuple([int, int, int]),
    help="Select cursor foreground color",
)
@click.option(
    "-cb",
    "--cursor-background",
    default=(0, 0, 0),
    type=click.Tuple([int, int, int]),
    help="Select cursor background color",
)
def cli(format, cursor_icon, cursor_foreground, cursor_background):
    xrect = XRectSel(
        cursor_icon=cursor_icon,
        cursor_foreground=cursor_foreground,
        cursor_background=cursor_background,
    )
    geometry = xrect.select()

    if geometry and (geometry["width"] >= 1 or geometry["height"] >= 1):
        click.echo(
            format.replace("%x", str(geometry["start"]["x"]))
            .replace("%y", str(geometry["start"]["y"]))
            .replace("%X", str(geometry["start"]))
            .replace("%Y", str(geometry["end"]))
            .replace("%w", str(geometry["width"]))
            .replace("%h", str(geometry["height"]))
        )
    else:
        click.echo("Please select area!")
