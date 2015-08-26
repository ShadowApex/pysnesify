#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# PySNESify
# Copyright (C) 2015, William Edwards <shadowapex@gmail.com>,
#
# PySNESify is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySNESify is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySNESify.  If not, see <http://www.gnu.org/licenses/>.
#
# Contributor(s):
#
# William Edwards <shadowapex@gmail.com>
#
# PySNESify was inspired by SNEStify by Kelvin:
# https://gum.co/lqdY
#

import sys
import getopt
from PIL import Image

def show_help():
    print "Usage:"
    print "  %s filename.png [output.png]" % sys.argv[0]
    print ""
    print "Arguments:"
    print "  -h      show this help message and exit"
    print ""

def round_to_multiple(x, base=8):
    return int(base * round(float(x)/base))


def round_rgb(x, base=8):
    x = round_to_multiple(x, base)
    if x > 255:
        x = 255
    elif x < 0:
        x = 0
    return x


def snesify(filename):
    image = Image.open(filename)
    image = image.convert("RGBA")
    datas = image.getdata()

    new_data = []
    for pixel in datas:
        r = round_rgb(pixel[0])
        g = round_rgb(pixel[1])
        b = round_rgb(pixel[2])
        a = round_rgb(pixel[3])

        new_pixel = (r, g, b, a)
        new_data.append(new_pixel)

    image.putdata(new_data)

    return image


if __name__ == "__main__":

    if len(sys.argv[1:]) < 1 or "-h" in sys.argv[1:] or len(sys.argv[1:]) > 2:
        show_help()
        sys.exit(2)

    filename = sys.argv[1:][0]

    if len(sys.argv[1:]) is 1:
        output = "SNES_" + filename
    else:
        output = sys.argv[1:][1]

    image = snesify(filename)
    image.save(output)
