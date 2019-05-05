<h1 align="center"> python-xrectsel</h2>

<h3 align="center">Geometry of a rectangular screen region</h3>
<p align="center">
<a href="https://pypi.org/project/python-xrectsel"><img alt="Python Versions"
src="https://img.shields.io/pypi/pyversions/python-xrectsel.svg?style=flat"></a>
<a href="https://pypi.org/project/python-xrectsel/#history"><img alt="PyPI version"
src="https://badge.fury.io/py/python-xrectsel.svg"></a>
<a href="https://github.com/digitronik/python-xrectsel/blob/master/LICENSE"><img alt="License: GPLV3"
src="https://img.shields.io/pypi/l/miqsel.svg?version=latest"></a>
<a href="https://pypi.org/project/black"><img alt="Code style: black"
src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>


## Installation:
```bash
pip3 install python-xrectsel --user
```

## Usage:
- Shell
```bash
$ xrectsel
$ # select rectangle on sreen
127 172 862 465 #(x-coordinate, y-coordinate, width, height)
```
- Python
```python
❯❯❯ cat test.py 
from xrectsel import XRectSel
print(XRectSel().select())

❯❯❯ python3 test.py 
{'start': {'x': 102, 'y': 218}, 'end': {'x': 1170, 'y': 476}, 'width': 1068, 'height': 258}
```
