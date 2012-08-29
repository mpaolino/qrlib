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
    imp.find_module('config')  # Assumed to be in the same directory.
    from .qrlib import (interior_small_qr_pil, interior_medium_qr_pil,
                        interior_large_qr_pil, exterior_small_qr_pil,
                        exterior_medium_qr_pil, exterior_large_qr_pil,
                        publishing_small_qr_pil, publishing_medium_qr_pil,
                        custom_qr_pil)

except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'config.py' in the directory containing %r." % __file__)
    sys.exit(1)
