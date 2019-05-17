<h1 align="center"> python-xrectsel</h2>

<h3 align="center">Geometry of a rectangular screen region</h3>
<p align="center">
<a href="https://pypi.org/project/python-xrectsel"><img alt="Python Versions"
src="https://img.shields.io/pypi/pyversions/python-xrectsel.svg?style=flat"></a>
<a href="https://travis-ci.org/digitronik/python-xrectsel"><img alt="Build Status"
src="https://travis-ci.org/digitronik/python-xrectsel.svg?branch=master"></a>
<a href="https://pypi.org/project/python-xrectsel/#history"><img alt="PyPI version"
src="https://badge.fury.io/py/python-xrectsel.svg"></a>
<a href="https://github.com/digitronik/python-xrectsel/blob/master/LICENSE"><img alt="License: GPLV3"
src="https://img.shields.io/pypi/l/miqsel.svg?version=latest"></a>
<a href="https://pypi.org/project/black"><img alt="Code style: black"
src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

This project idea based on `xrectsel` https://github.com/lolilolicon/xrectsel.
## Installation:
```bash
pip3 install python-xrectsel --user
```

## Usage:
```shell
Usage: xrectsel [OPTIONS]

Options:
  -f, --format TEXT  Format string...
                     %x - start x-coordinate
                     %y - start y-coordinate
                     %X - start
                     %Y - end
                     %w - width
                     %h - height
  --help             Show this message and exit.

```
- Default format is `%wx%h+%x+%y`
```bash
$ xrectsel
$ # select rectangle on sreen
901x634+44+7 #(x-coordinate, y-coordinate, width, height)
```
- Formatting string
```bash
$ xrectsel -f "--x=%x --y=%y --width=%w --height=%h"
--x=264 --y=387 --width=1204 --height=519
```
