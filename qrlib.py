# coding: utf-8
from os.path import abspath, dirname
import sys

path = dirname(abspath(__file__))
if path not in sys.path:
    sys.path.append(path)
lib = path + '/lib'
if lib not in sys.path:
    sys.path.insert(0, lib)

from config import *
from lib.pyqrcode import (MakeQRImage, QRErrorCorrectLevel)
#from lib.potrace import Bitmap

from PIL import (Image, ImageDraw, ImageFont)
import numpy


def get_qr_pil(text, ec_level='M', block_pixels=10, border_blocks=4):
    if ec_level == 'L':
        error_correction = QRErrorCorrectLevel.L
    if ec_level == 'M':
        error_correction = QRErrorCorrectLevel.M
    if ec_level == 'Q':
        error_correction = QRErrorCorrectLevel.Q
    if ec_level == 'H':
        error_correction = QRErrorCorrectLevel.H

    pil_qrcode = MakeQRImage(text,
                             block_in_pixels=block_pixels,
                             border_in_blocks=border_blocks,
                             errorCorrectLevel=error_correction)

    return pil_qrcode


def interior_small_qr_pil(text, language='es'):
    """Get's a small QR"""
    non_decorated = get_qr_pil(text,
                               ec_level=INTERIOR_SMALL['error_correction'],
                               block_pixels=INTERIOR_SMALL['block_pixels'],
                               border_blocks=INTERIOR_SMALL['border_blocks'])
    return decorate_pil(non_decorated, language=language,
                        margin=INTERIOR_SMALL['block_pixels']\
                               * INTERIOR_SMALL['border_blocks'])


def interior_medium_qr_pil(text, language='es'):
    """Get's a medium QR"""
    non_decorated = get_qr_pil(text,
                               ec_level=INTERIOR_MEDIUM['error_correction'],
                               block_pixels=INTERIOR_MEDIUM['block_pixels'],
                               border_blocks=INTERIOR_MEDIUM['border_blocks'])
    return decorate_pil(non_decorated, language=language,
                        margin=INTERIOR_MEDIUM['block_pixels']\
                               * INTERIOR_MEDIUM['border_blocks'])


def interior_large_qr_pil(text, language='es'):
    """Get's a large QR"""
    non_decorated = get_qr_pil(text,
                               ec_level=INTERIOR_LARGE['error_correction'],
                               block_pixels=INTERIOR_LARGE['block_pixels'],
                               border_blocks=INTERIOR_LARGE['border_blocks'])
    return decorate_pil(non_decorated, language=language,
                        margin=INTERIOR_LARGE['block_pixels']\
                               * INTERIOR_LARGE['border_blocks'])


def exterior_small_qr_pil(text, language='es'):
    """Get's a small QR"""
    non_decorated = get_qr_pil(text,
                               ec_level=EXTERIOR_SMALL['error_correction'],
                               block_pixels=EXTERIOR_SMALL['block_pixels'],
                               border_blocks=EXTERIOR_SMALL['border_blocks'])
    return decorate_pil(non_decorated, language=language,
                        margin=EXTERIOR_SMALL['block_pixels']\
                               * EXTERIOR_SMALL['border_blocks'])


def exterior_medium_qr_pil(text, language='es'):
    """Get's a medium QR"""
    non_decorated = get_qr_pil(text,
                               ec_level=EXTERIOR_MEDIUM['error_correction'],
                               block_pixels=EXTERIOR_MEDIUM['block_pixels'],
                               border_blocks=EXTERIOR_MEDIUM['border_blocks'])
    return decorate_pil(non_decorated, language=language,
                        margin=EXTERIOR_MEDIUM['block_pixels']\
                               * EXTERIOR_MEDIUM['border_blocks'])


def exterior_large_qr_pil(text, language='es'):
    """Get's a large QR"""
    non_decorated = get_qr_pil(text,
                               ec_level=EXTERIOR_LARGE['error_correction'],
                               block_pixels=EXTERIOR_LARGE['block_pixels'],
                               border_blocks=EXTERIOR_LARGE['border_blocks'])
    return decorate_pil(non_decorated, language=language,
                        margin=EXTERIOR_LARGE['block_pixels']\
                               * EXTERIOR_LARGE['border_blocks'])


def publishing_small_qr_pil(text, language='es'):
    """Get's a small QR"""
    non_decorated = get_qr_pil(text,
                               ec_level=PUBLISHING_SMALL['error_correction'],
                               block_pixels=PUBLISHING_SMALL['block_pixels'],
                               border_blocks=PUBLISHING_SMALL['border_blocks'])
    return decorate_pil(non_decorated, language=language,
                        margin=PUBLISHING_SMALL['block_pixels']\
                               * PUBLISHING_SMALL['border_blocks'])


def publishing_medium_qr_pil(text, language='es'):
    """Get's a medium QR"""
    non_decorated = get_qr_pil(text,
                               ec_level=PUBLISHING_MEDIUM['error_correction'],
                               block_pixels=PUBLISHING_MEDIUM['block_pixels'],
                               border_blocks=PUBLISHING_MEDIUM['border_blocks']
                              )
    return decorate_pil(non_decorated, language=language,
                        margin=PUBLISHING_MEDIUM['block_pixels']\
                               * PUBLISHING_MEDIUM['border_blocks'])


def decorate_pil(one_pil, language='es', margin=100):
    footer = Image.open(FOOTER_IMAGE_PATH)
    (footer_width, footer_height) = footer.size
    (pil_width, pil_height) = one_pil.size
    one_pil.paste(footer, (pil_width - margin - footer_width,
                  margin - footer_height), footer)
    draw = ImageDraw.Draw(one_pil)

    if language not in TEXT_TRANS:
        raise Exception('No "%s" language text.' % language)

    # TTF font size must be aprox 1/4 of margin (given in pixels)
    font_size = margin / 4
    text_font = ImageFont.truetype(FOOTER_TEXT_FONT, font_size)
    draw.text((margin, pil_height - footer_height), TEXT_TRANS[language],
              font=text_font, fill=FOOTER_TEXT_COLOR)
    draw.text((margin, pil_height - footer_height + font_size + 2),
               FOOTER_URL, font=text_font, fill=FOOTER_TEXT_COLOR)
    one_pil.show()


def pil_to_svg(pil_to_convert):
    """Converts PIL to SVG"""
    mode_f_converted = pil_to_convert.convert(mode='F')
    as_array = numpy.asarray(mode_f_converted)
    potrace_bmp = Bitmap(as_array)
    potraced_path = potrace_bmp.trace()
    return None
