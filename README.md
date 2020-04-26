<h1 align="center"> python-xrectsel</h1>
<h3 align="center">Geometry of a rectangular screen region</h3>

<p align="center">
<a href="https://pypi.org/project/python-xrectsel"><img alt="Python Versions"
src="https://img.shields.io/pypi/pyversions/python-xrectsel.svg?style=flat"></a>
<a href="https://github.com/digitronik/python-xrectsel/actions?query=workflow%3ATests"><img alt="Build Status"
src="https://github.com/digitronik/python-xrectsel/workflows/Tests/badge.svg?branch=master"></a>
<a href="https://codecov.io/gh/digitronik/python-xrectsel">
  <img src="https://codecov.io/gh/digitronik/python-xrectsel/branch/master/graph/badge.svg" />
</a>
<a href="https://pypi.org/project/python-xrectsel/#history"><img alt="PyPI version"
src="https://badge.fury.io/py/python-xrectsel.svg"></a>
<a href="https://github.com/digitronik/python-xrectsel/blob/master/LICENSE"><img alt="License: GPLV3"
src="https://img.shields.io/pypi/l/miqsel.svg?version=latest"></a>
<a href="https://pypi.org/project/black"><img alt="Code style: black"
src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

The project idea based on [xrectsel](https://github.com/lolilolicon/xrectsel). Its Python variant with some enhancements.

### Installation:
```bash
pip install python-xrectsel
```

### Usage:
```shell
❯ xrectsel --help
Usage: xrectsel [OPTIONS]

Options:
  -f, --format TEXT               Format output string with fallowing options:

                                  %x - start x-coordinate

                                  %y - start y-coordinate

                                  %X - start

                                  %Y - end

                                  %w - width

                                  %h - height

                                  Note: default output is in "%wx%h+%x+%y"
                                  format.

  -ci, --cursor-icon [crosshair|cross|pencil|dotbox]
                                  Select cursor icon
  -cf, --cursor-foreground <INTEGER INTEGER INTEGER>...
                                  Select cursor foreground color
  -cb, --cursor-background <INTEGER INTEGER INTEGER>...
                                  Select cursor background color
  -h, --help                      Show this message and exit.

```

- We can collect selected region geometry just by command `xrectsel`. Default format is `%wx%h+%x+%y`
```bash
$ xrectsel
$ # select rectangle on sreen
901x634+44+7 #(x-coordinate, y-coordinate, width, height)
```
- We can format output geometry string
```bash
$ xrectsel -f "--x=%x --y=%y --width=%w --height=%h"
--x=264 --y=387 --width=1204 --height=519
```
