=====
qrlib
=====

This is a library for QR images generation specifically designed for the
"spot" project.


Usage
=====

Usage is very simple. There are several functions to generate predefined-sized
QRs and customized size QRs. The library will choose the minimum QR version for
the text lenght to be encoded and will decorate the image with a logo and a
text footer aligned appropriately and return a PIL image.

There's a config.py in the main distribution directory to fine-tune several
parameters, notoriously all the predefined sizes and error correction
values, text font selection, etc. 


Common to all functions
-----------------------
All functions take a text parameter and a optional language parameter for
the footer language. As of version 0.1 only this languages are recognized:

'es' - Spanish
'en' - English
'br' - Portuguese (Brazilian)

Print sizes will directly depend on printing resolution, this library expects
180dpi as default print quality/resolution for all predefined QR generations
except for publishing oriented predefined sizes were 300dpi is expected. 
For actual estimated print sizes please refer to config.py.


Functions
=========

interior_small_qr_pil(text, language='es')
------------------------------------------
Returns a PIL image with a QR optimized for interior usage and small print
size.

interior_medium_qr_pil(text, language='es')
-------------------------------------------
Returns a PIL image with a QR optimized for interior usage and medium print
size.

interior_large_qr_pil(text, language='es')
------------------------------------------
Returns a PIL image with a QR optimized for interior usage and large print
size.

exterior_small_qr_pil(text, language='es')
------------------------------------------
Returns a PIL image with a QR optimized for exterior usage and small print
size.

exterior_medium_qr_pil(text, language='es')
-------------------------------------------
Returns a PIL image with a QR optimized for exterior usage and medium print
size.

exterior_large_qr_pil(text, language='es')
------------------------------------------
Returns a PIL image with a QR optimized for exterior usage and large print
size.

publishing_small_qr_pil(text, language='es')
--------------------------------------------
Returns a PIL image with a QR optimized for publishing usage and small print
size.

publishing_medium_qr_pil(text, language='es')
---------------------------------------------
Returns a PIL image with a QR optimized for publishing usage and medium print
size.

custom_qr_pil(text, error_correction, block_pixels, border_blocks, language='es', logo=True)
---------------------------------------------------------------------------------
Returns a custom sized QR especified by:

error_correction - (str) 'L', 'M', 'Q', 'H' (7%, 15%, 25% and 30% respectively)
block_pixels     - (int) Size in pixels (int) for QR blocks (modules)
border_blocks    - (int) How much blocks (modules) conform the image margin
logo             - (bool) If the upper right logo is pasted in image header
