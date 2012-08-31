# coding: utf-8
# (c) Copyright 2011 by Miguel Paolino <mpaolino@ideal.com.uy>
from os.path import abspath, dirname
import sys

path = dirname(abspath(__file__))
if path not in sys.path:
    sys.path.append(path)
lib = path + '/lib'
if lib not in sys.path:
    sys.path.insert(0, lib)

import imp


try:
    #imp.find_module('config')  # Assumed to be in the same directory.
    from .config import (INTERIOR_SMALL, INTERIOR_MEDIUM, INTERIOR_LARGE,
                    EXTERIOR_SMALL, EXTERIOR_MEDIUM, EXTERIOR_LARGE,
                    FOOTER_IMAGE_PATH, FOOTER_TEXT_FONT, FOOTER_TEXT_COLOR,
                    FOOTER_URL, TEXT_TRANS)
    from .validation import (width_validation, height_validation,
                             ec_level_validation)
    
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


    from .qrlib import (interior_small_qr_pil, interior_medium_qr_pil,
                        interior_large_qr_pil, exterior_small_qr_pil,
                        exterior_medium_qr_pil, exterior_large_qr_pil,
                        publishing_small_qr_pil, publishing_medium_qr_pil,
                        custom_qr_pil)

except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'config.py' in the directory containing %r." % __file__)
    sys.exit(1)
