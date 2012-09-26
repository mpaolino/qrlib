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
    from .validation import (size_validation, ec_level_validation,
                             validate_all_config, logo_margin_validation)
    from .config import *

    #validate_all_config()    
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


    from .qrlib import (generate_qr_file)

except ImportError, e:
    print e
#    import sys
#    sys.stderr.write("Error: Can't find the file 'config.py' in the directory containing %r." % __file__)
    sys.exit(1)
