# coding: utf-8
from os.path import abspath, dirname


# relative to static dir
LOGO_IMAGE = 'ideal_160x80.png'
LOGO_MARGIN = 50
# relative to font dir
FOOTER_FONT = 'FreeSans.ttf'

FOOTER_TEXT_COLOR = '#000000'

TEXT_TRANS = {'es': 'Descargue su lector de QR',
              'en': 'Download your QR reader',
              'br': 'Baixe o seu leitor de QR'}

FOOTER_URL = 'http://cuadraditos.uy'

# QR code version 1 (21x21 modules) 10-25 alphanumeric chars
# 180 dpi default print quality

# 20 block_pixels = 420x420 px = 2.33x2.33 inches = 5.92x5.92 cm
# 5 border_blocks = 100px
INTERIOR_SMALL = {'width': 150,
                  'height': 150,
                  'error_correction': 'M'}

# 40 block_pixels = 840x840px = 4.66x4.66 inches = 11.84x11.84 cm
# 6 border_blocks = 240px
INTERIOR_MEDIUM = {'width': 300,
                   'height': 300,
                   'error_correction': 'M'}

# 80 block_pixels = 1680x1680px = 9.33x9.33 inches = 23.7x23.7 cm
# 6 border_blocks = 480px
INTERIOR_LARGE = {'width': 400,
                  'height': 400,
                  'error_correction': 'M'}

EXTERIOR_SMALL = {'width': 150,
                  'height': 150,
                  'error_correction': 'H'}

EXTERIOR_MEDIUM = {'width': 300,
                   'height': 300,
                   'error_correction': 'H'}

EXTERIOR_LARGE = {'width': 400,
                  'height': 400,
                  'error_correction': 'H'}

BLOCK_SIZE = 10  # In pixels, svg style files must be BLOCK_SIZExBLOCK_SIZE size

LIB_ROOT = dirname(abspath(__file__))
FOOTER_TEXT_FONT = LIB_ROOT + "/fonts/" + FOOTER_FONT
LOGO_IMAGE_PATH = LIB_ROOT + "/static/" + LOGO_IMAGE

STYLE_FILES = ['2b.svg', '1b.svg', '1b3b.svg', '2a1b.svg',
               '2a1b1a.svg', '2a1b2c.svg', '2a1b2c3b.svg']

SHAPE_GROUP = '{http://www.w3.org/2000/svg}g'

BASIC_SHAPES = ['{http://www.w3.org/2000/svg}rect',
                '{http://www.w3.org/2000/svg}circle',
                '{http://www.w3.org/2000/svg}ellipse']

QUIET_ZONE = 4  # In blocks
