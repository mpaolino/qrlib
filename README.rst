==========================================================================================================================
WARNING: This project is old and unmaintained. I don't have any use for it anymore, if you do, please consider taking over
==========================================================================================================================





=====
qrlib
=====

This is a library for QR images generation. It provides functions to
generate predefined sized and custom QRs with several output formats.
All functions return a filelike-object (StringIO) with the encoded QR.

Sample Usage
============

::

    import qrlib
    one_qr = qrlib.generate_qr_file('http://ideal.com.uy', qr_format='PDF')
    f = open(qrsample.pdf, 'w')
    f.write(one_qr.getvalue())
    f.close()


API
===

The API is very simple. There are only two functions to generate
predefined-sized QRs and customized size QRs. The library will choose the
minimum QR version for the text length to be encoded and will decorate the
image with a logo and instructions in case of PDF generation.

There's a config.py in the main distribution directory to fine-tune several
parameters, notoriously all the predefined sizes and error correction
values, logo and instructions image files, etc. 

File output
-----------
All public intended functions will return a filelike object with string binary
data of the requested format.

Supported outputs:

  * SVG
  * GIF
  * PNG
  * JPEG
  * PDF


Functions
=========

generate_qr_file
----------------
Function to return a filelike object with preconfigured sizes in config.py.

::

    generate_qr_file(text, language='es', qr_format='PDF', app='interior',
                     app_size='small', instructions=True,
                     style='default', style_color='#000000',
                     inner_eye_style='default', inner_eye_color='#000000',
                     outer_eye_style='default', outer_eye_color='#000000',
                     bg_color='#FFFFFF'):


----------
Parameters
----------

language
    Text language for PDF instructions. Only 'es' spanish for now.

qr_format
    Format of QR, Values 'SVG', 'PDF', 'GIF', 'PNG', 'JPEG'. Defaults to 'PDF'.

app
    Application for QR, 'interior' or 'exterior'.
    Automatically chooses error correction level for QR. 
    Defaults to 'interior'.

app_size
    Application size, 'small', 'medium', 'large'.
    Defaults to 'small'.

instructions
    Print or not the instructions in the PDF

style
    Style to apply to QR blocks (one of static/styles).
    Defaults to 'default' style.

style_color
    Hex color code for style. Defaults to #000000

inner_eye_style
    Style to apply to inner eyes of QR.
    Defaults to 'default' style.

inner_eye_color
    Hex color code for inner eye style.
    Defaults to #000000.

outer_eye_style
    Style to apply to inner eyes of QR.
    Defaults to 'default' style.

outer_eye_color
    Hex color code for outer eye style.
    Defaults to #000000.

bg_color
    Hex color code for QR background. Defaults to #FFFFFF


generate_custom_qr_file
-----------------------
Function to return a filelike object with custom QR size and error correction
level.


::

    generate_custom_qr_file(text, language='es', qr_format='PDF', size=150,
                            ec_level='L', instructions=True, style='default',
                            style_color='#000000', inner_eye_style='default',
                            inner_eye_color='#000000',
                            outer_eye_style='default',
                            outer_eye_color='#000000',
                            bg_color='#FFFFFF'):


Parameters
----------
language
    Text language for PDF instructions. Only 'es' spanish for now.

qr_format
    Format of QR, Values 'PDF', 'GIF', 'PNG', 'JPEG', 'SVG'.
    Defaults to 'PDF'. No format besides PDF will show
    instructions.

size
    Size in pixels for the generated QR. The size includes
    a mandatory safe margin for QR readability. This border
    size its relative to block sizes and can be customized
    in config.py

ec_level
    Error correction level. Values:
          'L' - approx 7%
          'M' - approx 15%
          'Q' - approx 25%
          'H' - approx 30%

instructions
    Print or not the instructions in the PDF

style
    Style to apply to QR blocks (one of static/styles).
    Defaults to 'default' style.

style_color
    Hex color code for style. Defaults to #000000

inner_eye_style
    Style to apply to inner eyes of QR. Defaults to 'default' style.

inner_eye_color
    Hex color code for inner eye style. Defaults to #000000.

outer_eye_style
    Style to apply to inner eyes of QR. Defaults to 'default' style.

outer_eye_color
    Hex color code for outer eye style. Defaults to #000000.

bg_color
    Hex color code for QR background. Defaults to #FFFFFF


Tests
=====

To run included tests you must be in the library directory and then run:

$ python -m unittest2 discover

Once installed you can run the tests from any directory:

$ python -m unittest2 discover qrlib
