# coding: utf-8
# (c) Copyright 2011 by Miguel Paolino <mpaolino@ideal.com.uy>
from config import (INTERIOR_SMALL, INTERIOR_MEDIUM, INTERIOR_LARGE,
                    EXTERIOR_SMALL, EXTERIOR_MEDIUM, EXTERIOR_LARGE,
                    LOGO_IMAGE_PATH, FOOTER_TEXT_FONT, FOOTER_TEXT_COLOR,
                    FOOTER_URL, TEXT_TRANS)


def width_validation(width):
    if not isinstance(width, int) or width < 100 or width > 1000:
        raise Exception('QR width validation failed (100 <= int(width) <= 1000)')
    return True

def height_validation(height):
    if not isinstance(height, int) or height < 100 or height > 1000:
        raise Exception('QR height validation failed (100 <= int(height) <= 1000)')
    return True

def logo_margin_validation(margin):
    if not isinstance(margin, int) or margin < 50 or margin > 300:
        raise Exception('Logo margin validation failed (50 <= int(margin) <= 300)')
    return True

def ec_level_validation(ec_level):
    if not isinstance(ec_level, (unicode, str)) or \
            ec_level.upper() not in ('L', 'M', 'Q', 'H'):
        raise Exception('Unrecognized QR error correction level')
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

def validate_all_config():    
    width_validation(INTERIOR_SMALL['width'])
    width_validation(INTERIOR_MEDIUM['width'])
    width_validation(INTERIOR_LARGE['width'])
    width_validation(EXTERIOR_SMALL['width'])
    width_validation(EXTERIOR_MEDIUM['width'])
    width_validation(EXTERIOR_LARGE['width'])
    height_validation(INTERIOR_SMALL['height'])
    height_validation(INTERIOR_MEDIUM['height'])
    height_validation(INTERIOR_LARGE['height'])
    height_validation(EXTERIOR_SMALL['height'])
    height_validation(EXTERIOR_MEDIUM['height'])
    height_validation(EXTERIOR_LARGE['height'])
    ec_level_validation(INTERIOR_SMALL['error_correction'])
    ec_level_validation(INTERIOR_MEDIUM['error_correction'])
    ec_level_validation(INTERIOR_LARGE['error_correction'])
    ec_level_validation(EXTERIOR_SMALL['error_correction'])
    ec_level_validation(EXTERIOR_MEDIUM['error_correction'])
    ec_level_validation(EXTERIOR_LARGE['error_correction'])
