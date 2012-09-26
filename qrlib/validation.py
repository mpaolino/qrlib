# coding: utf-8
# (c) Copyright 2011 by Miguel Paolino <mpaolino@ideal.com.uy>
from config import (INTERIOR_SMALL, INTERIOR_MEDIUM, INTERIOR_LARGE,
                    EXTERIOR_SMALL, EXTERIOR_MEDIUM, EXTERIOR_LARGE)
import re


def size_validation(width):
    if not isinstance(width, (int, float)) or width < 100 or width > 1000:
        raise Exception('QR size validation failed ' + \
                        '(100 <= int(width) <= 1000)')
    return True


def logo_margin_validation(margin):
    if not isinstance(margin, int) or margin < 50 or margin > 300:
        raise Exception('Logo margin validation failed (50 <= int(margin)' + \
                        '<= 300)')
    return True


def ec_level_validation(ec_level):
    if not isinstance(ec_level, (unicode, str)) or \
            ec_level.upper() not in ('L', 'M', 'Q', 'H'):
        raise Exception('Unrecognized QR error correction' +\
                        'level "%s"' % str(ec_level))
    return True


def format_validation(qr_format):
    if not isinstance(qr_format, (unicode, str)) or \
            qr_format.upper() not in ('PDF', 'GIF', 'PNG', 'JPG'):
        raise Exception('Unrecognized QR output format')
    return True


def application_validation(application):
    if not isinstance(application, (unicode, str)) or \
            application.lower() not in ('interior', 'exterior'):
        raise Exception('Unrecognized QR application')
    return True


def appsize_validation(app_size):
    if not isinstance(app_size, (unicode, str)) or \
            app_size.lower() not in ('small', 'medium', 'large'):
        raise Exception('Unrecognized QR application size')
    return True


def language_validation(language):
    if not isinstance(language, (unicode, str)) or \
            language.lower() not in ('es', 'en', 'br'):
        raise Exception('Unrecognized QR footer language')
    return True


def color_validation(color):
    string_colors = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green',
                     'lime', 'maroon', 'navy', 'olive', 'purple', 'red',
                     'silver', 'teal', 'white', 'yellow']

    if color in string_colors or re.match('\#[0-9A-Fa-f]{6}', color):
        return True
    raise Exception('Invalid color \'%s\'' % (color))


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
