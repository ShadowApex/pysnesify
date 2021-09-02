#!/bin/env python
# -*- coding: utf-8 -*-
#
# PySNESify
# Copyright (C) 2021, William Edwards <shadowapex@gmail.com>,
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

import argparse
import os
import sys

import cv2
import numpy as np


# Returns the color with the closest euclidean distance in color space.
def closest_color(pixel, palette):
    _, size, _ = palette.shape
    value = np.array((0, 0, 0))
    closest = 100000
    for i in range(size):
        color = palette[0, i]
        dist = np.linalg.norm(color-pixel)
        if dist < closest:
            closest = dist
            value = color
    return value

def snesify(filename, palette, technique='bgr'):
    # Read input img
    in_img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    height, width, _ = in_img.shape
    # extract alpha channel
    alpha = in_img[:,:,3]
    
    # Read the palette image
    palette_img = cv2.imread(palette)
    
    # Convert to HSV
    if technique == "bgr":
        in_img_conv = cv2.cvtColor(in_img, cv2.COLOR_BGR2BGRA)
        palette_conv = cv2.cvtColor(palette_img, cv2.COLOR_BGR2BGRA)
    elif technique == "hsv":
        in_img_conv = cv2.cvtColor(in_img, cv2.COLOR_BGR2HSV)
        palette_conv = cv2.cvtColor(palette_img, cv2.COLOR_BGR2HSV)
    else:
        print("Invalid technique provided")
        sys.exit(1)
    
    # Loop through all pixels of the image
    for y in range(height):
        for x in range(width):
            pixel = in_img_conv[y, x]
            in_img_conv[y, x] = closest_color(pixel, palette_conv)
    
    # Convert the image back to BGRA
    if technique == "bgr":
        out_img = in_img_conv
    elif technique == "hsv":
        bgr_img = cv2.cvtColor(in_img_conv, cv2.COLOR_HSV2BGR)
        out_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2BGRA)
    else:
        print("Invalid technique provided")
        sys.exit(1)
    
    # put alpha back into bgr_new
    out_img[:,:,3] = alpha
    
    # Return the image file
    return out_img


if __name__ == "__main__":
    # Define the arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('filename', help="Path to file of the image to convert")
    parser.add_argument('palette', help="Path to palette image file")
    parser.add_argument('-t', '--technique', default="bgr", help="Technique to use (bgr, hsv)")
    parser.add_argument('-o', '--output', help="Output filename")
    
    # Parse our arguments
    args = parser.parse_args()

    # SNESify the image according to the given palette
    image = snesify(args.filename, args.palette, args.technique)
    if args.output:
        output = args.output
    else:
        palette = os.path.splitext(os.path.split(args.palette)[-1])[0]
        file, ext = os.path.splitext(os.path.split(args.filename)[-1])
        output = "{}_{}_{}{}".format(file, palette, args.technique, ext)
    print("Saving to: {}".format(output))
    cv2.imwrite(output, image)
