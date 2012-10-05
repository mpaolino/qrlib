# coding: utf-8
# (c) Copyright 2011 by Miguel Paolino <mpaolino@ideal.com.uy>
from config import (INTERIOR_SMALL, INTERIOR_MEDIUM, INTERIOR_LARGE,
                    EXTERIOR_SMALL, EXTERIOR_MEDIUM, EXTERIOR_LARGE,
                    LOGO_MARGIN, EYE_STYLES_DIR, STYLES_DIR)
from exceptions import (StyleMissing, InvalidColor, InvalidSize,
                        InvalidApplication, InnerEyeStyleMissing,
                        OuterEyeStyleMissing, InvalidSize,
                        InvalidLanguage, InvalidEcLevel)

import re
from os.path import (join, isdir)


def _check_style(style_dir, style):
    if not isinstance(style, (str, unicode)):
        raise AttributeError('style must be str or unicode')
    style = style.lower()
    directory = join(style_dir, style)
    if not isdir(directory):
        raise StyleMissing(style)
    return True


def style_validation(style):
    return _check_style(STYLES_DIR, style)


def inner_eye_style_validation(style):
    try:
        _check_style(EYE_STYLES_DIR, style)
    except StyleMissing:
        raise InnerEyeStyleMissing('Inner style \'%s\' missing' % (style))
    return True


def outer_eye_style_validation(style):
    try:
        _check_style(EYE_STYLES_DIR, style)
    except StyleMissing:
        raise OuterEyeStyleMissing('Outer style \'%s\' missing' % (style))
    return True


def size_validation(width):
    if not isinstance(width, (int, float)) or width < 100 or width > 1000:
        raise InvalidSize('QR size validation failed 100 <= width <= 1000)')
    return True


def logo_margin_validation(margin):
    if not isinstance(margin, (int, float)) or margin < 0 or margin > 300:
        raise InvalidLogoMargin('Logo margin validation failed (50 <= margin'
                                '<= 300)')
    return True


def ec_level_validation(ec_level):
    if not isinstance(ec_level, (unicode, str)) or \
            ec_level.upper() not in ('L', 'M', 'Q', 'H'):
        raise InvalidEcLevel('Unrecognized QR error correction'
                        'level "%s"' % str(ec_level))
    return True


def format_validation(qr_format):
    if not isinstance(qr_format, (unicode, str)) or \
            qr_format.upper() not in ('PDF', 'GIF', 'PNG', 'JPEG'):
        raise Exception('Unrecognized QR output format')
    return True


def application_validation(application):
    if not isinstance(application, (unicode, str)) or \
            application.lower() not in ('interior', 'exterior'):
        raise InvalidApplication('Unrecognized QR application')
    return True


def appsize_validation(app_size):
    if not isinstance(app_size, (unicode, str)) or \
            app_size.lower() not in ('small', 'medium', 'large'):
        raise InvalidAppSize('Unrecognized QR application size')
    return True


def language_validation(language):
    if not isinstance(language, (unicode, str)) or \
            language.lower() not in ('es', 'en', 'br'):
        raise InvalidLanguage('Unrecognized QR footer language')
    return True


def color_validation(color):
    if not re.match('\#[0-9A-Fa-f]{6}', color):
        raise InvalidColor('Invalid color \'%s\'' % (color))
    return True


def validate_all_config():
    size_validation(INTERIOR_SMALL['size'])
    size_validation(INTERIOR_MEDIUM['size'])
    size_validation(INTERIOR_LARGE['size'])
    size_validation(EXTERIOR_SMALL['size'])
    size_validation(EXTERIOR_MEDIUM['size'])
    size_validation(EXTERIOR_LARGE['size'])
    ec_level_validation(INTERIOR_SMALL['error_correction'])
    ec_level_validation(INTERIOR_MEDIUM['error_correction'])
    ec_level_validation(INTERIOR_LARGE['error_correction'])
    ec_level_validation(EXTERIOR_SMALL['error_correction'])
    ec_level_validation(EXTERIOR_MEDIUM['error_correction'])
    ec_level_validation(EXTERIOR_LARGE['error_correction'])
    logo_margin_validation(LOGO_MARGIN)
