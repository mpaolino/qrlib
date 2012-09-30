=====
qrlib
=====

This is a library for QR images generation.

Sample Usage
============

::

    import qrlib

    one_qr = qrlib.interior_small_qr_pil('http://ideal.com.uy', language='en')
    one_qr.show()



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
Both functions will return a filelike object with string binary data
of the requested format.

Supported outputs:
* GIF
* PNG
* JPEG
* PDF


Functions
=========




Tests
=====

To run included tests you must be in the library directory and then run:

$ python -m unittest2 discover

Once installed you can run the tests from any directory:

$ python -m unittest2 discover qrlib
