# Image Watermark Desktop App

A desktop application with a graphical interface (Tkinter) that adds a
text watermark to an image. Built with Python and Pillow as part of the
100 Days of Code bootcamp (Day 85).

## Example

Before:

![Before](images/before.png)

After:

![After](images/after.png)

## Features
- Choose a PNG or JPEG image from your computer
- Type any watermark text
- The text goes in the bottom-right corner, white with a black outline
  so it stays readable on light and dark images
- Font size and margin scale with the size of the image
- Save the result as PNG or JPEG in a location of your choice
- Warning messages if no image or no text was provided

## Requirements
- Python 3
- Pillow

Install the dependencies with:

    pip install -r requirements.txt

## How to run

    python main.py

1. Click "Choose Image" and select a picture.
2. Type your watermark text in the text field.
3. Click "Apply Watermark" and choose where to save the new image.

## Notes
- The font is Arial (`arial.ttf`), so the app was tested on Windows.
  On other systems the font may need to be changed.

## Possible improvements
- Choose the position, color and transparency of the watermark
- Image preview inside the window
- Font size selection
- Logo (image) watermark