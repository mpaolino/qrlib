# coding: utf-8
from os.path import abspath, dirname, join


# relative to static dir
LOGO_IMAGE = 'ideal_55x20.png'
LOGO_MARGIN = 2
# relative to font dir
FOOTER_FONT = 'FreeSans.ttf'

FOOTER_TEXT_COLOR = '#000000'

TEXT_TRANS = {'es': 'Descargue su lector de QR',
              'en': 'Download your QR reader',
              'br': 'Baixe o seu leitor de QR'}

FOOTER_URL = 'http://cuadraditos.uy'

# Aplication sizes in pixels
INTERIOR_SMALL = {'size': 150,
                  'error_correction': 'L'}

INTERIOR_MEDIUM = {'size': 300,
                   'error_correction': 'M'}

INTERIOR_LARGE = {'size': 350,
                  'error_correction': 'M'}

EXTERIOR_SMALL = {'size': 150,
                  'error_correction': 'H'}

EXTERIOR_MEDIUM = {'size': 300,
                   'error_correction': 'H'}

EXTERIOR_LARGE = {'size': 350,
                  'error_correction': 'H'}

BLOCK_SIZE = 10  # In pixels, svg style files must be BLOCK_SIZExBLOCK_SIZE

QUIET_ZONE = 4  # In blocks

DASHFRAME_MARGIN = 20  # In pixels, the margin from the generated QR for PDF

LIB_ROOT = dirname(abspath(__file__))
FOOTER_TEXT_FONT = join(LIB_ROOT, "fonts/", FOOTER_FONT)
LOGO_IMAGE_PATH = join(LIB_ROOT, "static/images/", LOGO_IMAGE)
STYLES_DIR = join(LIB_ROOT, "static/styles")
EYE_STYLES_DIR = join(LIB_ROOT, "static/eyes")
SCISSORS_IMAGE_PATH = join(LIB_ROOT, "static/images/scissors.png")
INSTRUCTIONS_IMAGE_PATH = join(LIB_ROOT, "static/images/instructions_es.png")
INSTRUCTIONS_CENTER_OFFSET = 0

STYLE_FILES = ['2b.svg', '1b.svg', '1b3b.svg', '2a1b.svg',
               '2a1b1a.svg', '2a1b2c.svg', '2a1b2c3b.svg']

EYE_STYLE_FILES = ['inner.svg', 'outer.svg']

SHAPE_GROUP = '{http://www.w3.org/2000/svg}g'

BASIC_SHAPES = ['{http://www.w3.org/2000/svg}rect',
                '{http://www.w3.org/2000/svg}circle',
                '{http://www.w3.org/2000/svg}ellipse',
                '{http://www.w3.org/2000/svg}path',
                '{http://www.w3.org/2000/svg}line']

PDF_CREATOR = 'http://cuadraditos.uy'
PDF_AUTHOR = 'ideal'
