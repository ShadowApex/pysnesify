# PySNESify

PySNESify is a small utility that will convert an image to fit into the color limitations
provided by a given palette.

![](docs/sharpfin_mulfok32-1x_bgr.png)

## Requirements

* opencv

## Usage

```
usage: pysnesify.py [-h] [-t TECHNIQUE] [-o OUTPUT] filename palette

Process some integers.

positional arguments:
  filename              Path to file of the image to convert
  palette               Path to palette image file

optional arguments:
  -h, --help            show this help message and exit
  -t TECHNIQUE, --technique TECHNIQUE
                        Technique to use (bgr, hsv)
  -o OUTPUT, --output OUTPUT
                        Output filename
```


## License

GNU GENERAL PUBLIC LICENSE v3

Copyright (C) 2021 William Edwards <shadowapex@gmail.com>

This software is distributed under the GNU General Public Licence as published
by the Free Software Foundation.  See the file LICENCE for the conditions
under which this software is made available.
