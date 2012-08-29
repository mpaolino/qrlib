# coding: utf-8
# (c) Copyright 2011 by Miguel Paolino <mpaolino@ideal.com.uy>
from config import (INTERIOR_SMALL, INTERIOR_MEDIUM, INTERIOR_LARGE,
                    EXTERIOR_SMALL, EXTERIOR_MEDIUM, EXTERIOR_LARGE,
                    PUBLISHING_SMALL, PUBLISHING_MEDIUM,
                    FOOTER_IMAGE_PATH, FOOTER_TEXT_FONT, FOOTER_TEXT_COLOR,
                    FOOTER_URL, TEXT_TRANS)
from lib.pyqrcode import (MakeQRImage, QRErrorCorrectLevel)
# Still not used
# from lib.potrace import Bitmap

from PIL import (Image, ImageDraw, ImageFont)
#import numpy


def _get_qr_pil(text, ec_level='M', block_pixels=10, border_blocks=4):
    """
        Returns a customized PIL image with an encoded QR
    """
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
    """Get's a small QR for interior use"""
    non_decorated = _get_qr_pil(text,
                                ec_level=INTERIOR_SMALL['error_correction'],
                                block_pixels=INTERIOR_SMALL['block_pixels'],
                                border_blocks=INTERIOR_SMALL['border_blocks'])
    return _decorate_pil(non_decorated, language=language,
                         margin=INTERIOR_SMALL['block_pixels']\
                               * INTERIOR_SMALL['border_blocks'])


def interior_medium_qr_pil(text, language='es'):
    """Get's a medium QR for interior use"""
    non_decorated = _get_qr_pil(text,
                                ec_level=INTERIOR_MEDIUM['error_correction'],
                                block_pixels=INTERIOR_MEDIUM['block_pixels'],
                                border_blocks=INTERIOR_MEDIUM['border_blocks'])
    return _decorate_pil(non_decorated, language=language,
                         margin=INTERIOR_MEDIUM['block_pixels']\
                               * INTERIOR_MEDIUM['border_blocks'])


def interior_large_qr_pil(text, language='es'):
    """Get's a large QR for interior use"""
    non_decorated = _get_qr_pil(text,
                                ec_level=INTERIOR_LARGE['error_correction'],
                                block_pixels=INTERIOR_LARGE['block_pixels'],
                                border_blocks=INTERIOR_LARGE['border_blocks'])
    return _decorate_pil(non_decorated, language=language,
                         margin=INTERIOR_LARGE['block_pixels']\
                               * INTERIOR_LARGE['border_blocks'])


def exterior_small_qr_pil(text, language='es'):
    """Get's a small QR for exterior use"""
    non_decorated = _get_qr_pil(text,
                                ec_level=EXTERIOR_SMALL['error_correction'],
                                block_pixels=EXTERIOR_SMALL['block_pixels'],
                                border_blocks=EXTERIOR_SMALL['border_blocks'])
    return _decorate_pil(non_decorated, language=language,
                         margin=EXTERIOR_SMALL['block_pixels']\
                               * EXTERIOR_SMALL['border_blocks'])


def exterior_medium_qr_pil(text, language='es'):
    """Get's a medium QR for exterior use"""
    non_decorated = _get_qr_pil(text,
                                ec_level=EXTERIOR_MEDIUM['error_correction'],
                                block_pixels=EXTERIOR_MEDIUM['block_pixels'],
                                border_blocks=EXTERIOR_MEDIUM['border_blocks'])
    return _decorate_pil(non_decorated, language=language,
                         margin=EXTERIOR_MEDIUM['block_pixels']\
                               * EXTERIOR_MEDIUM['border_blocks'])


def exterior_large_qr_pil(text, language='es'):
    """Get's a large QR for exterior use"""
    non_decorated = _get_qr_pil(text,
                                ec_level=EXTERIOR_LARGE['error_correction'],
                                block_pixels=EXTERIOR_LARGE['block_pixels'],
                                border_blocks=EXTERIOR_LARGE['border_blocks'])
    return _decorate_pil(non_decorated, language=language,
                         margin=EXTERIOR_LARGE['block_pixels']\
                               * EXTERIOR_LARGE['border_blocks'])


def publishing_small_qr_pil(text, language='es'):
    """Get's a small QR for publishing use"""
    non_decorated = _get_qr_pil(text,
                                ec_level=PUBLISHING_SMALL['error_correction'],
                                block_pixels=PUBLISHING_SMALL['block_pixels'],
                                border_blocks=PUBLISHING_SMALL['border_blocks']
                                )
    return _decorate_pil(non_decorated, language=language,
                         margin=PUBLISHING_SMALL['block_pixels']\
                               * PUBLISHING_SMALL['border_blocks'])


def publishing_medium_qr_pil(text, language='es'):
    """Get's a medium QR for publishing use"""
    non_decorated = _get_qr_pil(text,
                               ec_level=PUBLISHING_MEDIUM['error_correction'],
                               block_pixels=PUBLISHING_MEDIUM['block_pixels'],
                               border_blocks=PUBLISHING_MEDIUM['border_blocks']
                               )
    return _decorate_pil(non_decorated, language=language,
                         margin=PUBLISHING_MEDIUM['block_pixels']\
                               * PUBLISHING_MEDIUM['border_blocks'])


def custom_qr_pil(text, error_correction, block_pixels, border_blocks,
                  language='es', logo=True):
    """Get's a custom QR with decorations"""
    non_decorated = _get_qr_pil(text, ec_level=error_correction,
                                block_pixels=block_pixels,
                                border_blocks=border_blocks)
    return _decorate_pil(non_decorated, language=language,
                        margin=block_pixels * border_blocks, logo=logo)


def _decorate_pil(one_pil, language='es', margin=100, logo=True):
    """Takes a PIL with encoded QR and decorates it"""
    # TTF font size must be aprox 1/4 of margin (given in pixels)
    font_size = margin / 4
    # Vertical margin from image inferior border (3 lines of text)
    v_margin = font_size * 3
    (pil_width, pil_height) = one_pil.size

    if logo:
        footer = Image.open(FOOTER_IMAGE_PATH)
        (footer_width, footer_height) = footer.size
        one_pil.paste(footer, (pil_width - margin - footer_width,
                      margin / 2 - footer_height / 2), footer)

    draw = ImageDraw.Draw(one_pil)

    if language not in TEXT_TRANS:
        raise Exception('No "%s" language text.' % language)

    text_font = ImageFont.truetype(FOOTER_TEXT_FONT, font_size)
    draw.text((margin, pil_height - v_margin), TEXT_TRANS[language],
              font=text_font, fill=FOOTER_TEXT_COLOR)
    # We give an extra 4 px for line separation
    draw.text((margin, pil_height - v_margin + font_size + 4),
               FOOTER_URL, font=text_font, fill=FOOTER_TEXT_COLOR)
    return one_pil


def _pil_to_svg(pil_to_convert):
    """Converts PIL to SVG"""
    mode_f_converted = pil_to_convert.convert(mode='F')
    as_array = numpy.asarray(mode_f_converted)
    potrace_bmp = Bitmap(as_array)
    potraced_path = potrace_bmp.trace()
    return None
