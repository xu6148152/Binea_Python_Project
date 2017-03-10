#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from PIL import Image
import os

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWith, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image
        print('Resizing %s...' % filename)
        im = im.resize((width, height))

        # Add the logo
        print('Adding logo to %s...' % filename)
        im.paste(logoIm, (width - logoWith, height - logoHeight), logoIm)


        # Save changes
        im.save(os.path.join('withLogo', filename))
