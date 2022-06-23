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

try:
    from .validation import (validate_all_config)
    validate_all_config()    
    from .qrlib import (generate_qr_file, generate_custom_qr_file)
    from .exceptions import (StyleMissing, InvalidColor, InvalidSize,
                             InvalidApplication, InnerEyeStyleMissing,
                             OuterEyeStyleMissing, InvalidSize,
                             InvalidLanguage, InvalidEcLevel)

except ImportError as e:
    print(e)
#    import sys
#    sys.stderr.write("Error: Can't find the file 'config.py' in the directory containing %r." % __file__)
    sys.exit(1)
