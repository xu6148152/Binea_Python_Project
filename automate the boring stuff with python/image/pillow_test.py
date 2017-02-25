#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from PIL import Image


def test_cat_props():
    catIm = Image.open('zophie.png')
    print(catIm.size)

    print(catIm.format)
    print(catIm.format_description)

    croppedIm = catIm.crop((335, 345, 565, 560))
    croppedIm.save('cropped.png')


def test_create_image():
    im = Image.new('RGBA', (100, 200), 'purple')
    im.save('purpleImage.png')
    im2 = Image.new('RGBA', (20, 20))
    im2.save('transparentImage.png')


if __name__ == '__main__':
    test_cat_props()
