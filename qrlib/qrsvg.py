# coding: utf-8
# (c) Copyright 2012 by Miguel Paolino <mpaolino@ideal.com.uy>
from lib import pyqrcode
from xml.etree import cElementTree as et
from config import (BLOCK_SIZE, BASIC_SHAPES, SHAPE_GROUP, STYLE_FILES,
                    QUIET_ZONE, EYE_STYLE_FILES, STYLES_DIR, EYE_STYLES_DIR)
from validation import (color_validation, ec_level_validation,
                        size_validation, style_validation,
                        inner_eye_style_validation,
                        outer_eye_style_validation)

from os.path import join
import re
import cStringIO
import copy


def _get_style_dict(style='default'):
    '''
        Iterates over STYLE_FILES for the defined style and builds
        a dictionary with it's shape groups
    '''
    style = style.lower()
    directory = join(STYLES_DIR, style)
    style_dict = {}

    for filename in STYLE_FILES:
        filepath = join(directory, filename)
        document = et.parse(filepath)
        root = document.getroot()
        style_dict[filename] = []
        for group_elem in root.findall(SHAPE_GROUP):
            style_dict[filename].append(group_elem)
        # No group defined, must be basic shape
        for basic_shape in BASIC_SHAPES:
            for group_elem in root.findall(basic_shape):
                style_dict[filename].append(group_elem)
    return style_dict


def _get_eyes_dict(style='default'):
    '''
        Iterates over EYE_STYLES for the defined style and builds
        a dictionary with it's shape groups
    '''
    style = style.lower()
    directory = join(EYE_STYLES_DIR, style)
    eyes_dict = {}

    for filename in EYE_STYLE_FILES:
        filepath = join(directory, filename)
        document = et.parse(filepath)
        root = document.getroot()
        eyes_dict[filename] = []
        for group_elem in root.findall(SHAPE_GROUP):
            eyes_dict[filename].append(group_elem)
        for basic_shape in BASIC_SHAPES:
            for group_elem in root.findall(basic_shape):
                eyes_dict[filename].append(group_elem)
    return eyes_dict


# If it has an attrib to set (or it's children), it must be whatever we say
def _set_attrib(one_elem, color='#000000'):
    '''
        Recursive function to set all elements and this childrens
        that have attributes to change stroke and fill colors.
    '''
    if hasattr(one_elem, 'getchildren'):
        for elem in one_elem.getchildren():
            _set_attrib(elem, color=color)
    if hasattr(one_elem, 'attrib') and 'style' in one_elem.attrib:
        elem_style = one_elem.attrib['style']
        elem_style = re.sub(r'fill:\#\d+;', 'fill:%s;' % color, elem_style)
        elem_style = re.sub(r'stroke:\#\d+;', 'stroke:%s;' % color, elem_style)
        one_elem.attrib['style'] = elem_style


def _insert_shape(x, y, shape_w_rotation, final_svg, style_dict='default',
                                         color='#000000', block_scale=1.0):
    '''
        Inserts svg shape in the appropiate place, with selected style
        and fill color
    '''
    shape = None
    rotation = 0
    if isinstance(shape_w_rotation, tuple):
        (shape, rotation) = shape_w_rotation
        rotation = int(rotation)
    else:
        shape = shape_w_rotation
        rotation = 0

    block_size = BLOCK_SIZE
    if block_scale > 0:
        block_size = BLOCK_SIZE * block_scale
    else:
        raise Exception('Block scale \'%s\' not valid' % (block_scale))

    bound = QUIET_ZONE * (block_size)
    if style_dict == None:
        et.SubElement(final_svg, 'rect', x=str((x * block_size) + bound),
                      y=str((y * block_size) + bound), width=str(block_size),
                      height=str(block_size), fill=color)
        return

    translate = "translate( %(x)s %(y)s )" % \
                {
                  'x': str((x * block_size) + bound),
                  'y': str((y * block_size) + bound)
                }

    if int(rotation) != 0:
        rotate = "rotate(%(angle)s, %(center)s, %(center)s)" % \
                {
                 'angle': str(rotation),
                 'center': str((float(block_size) / 2))
                }
        translate = translate + " " + rotate

    if block_scale != 1 and block_scale > 0:
        scale = "scale(%s)" % (str(block_scale))
        translate = translate + " " + scale

    new_container = et.SubElement(final_svg, 'g', transform=translate)
    for elem in style_dict[shape]:
        dup_elem = copy.copy(elem)
        _set_attrib(dup_elem, color=color)
        new_container.append(dup_elem)


def _one_touching(top_left=False, top_center=False, top_right=False,
                   middle_left=False, middle_right=False,
                   bottom_left=False, bottom_center=False,
                   bottom_right=False):

    # First the cross
    if top_center:
        return ('1b.svg', 0)
    if middle_right:
        return ('1b.svg', 90)
    if bottom_center:
        return ('1b.svg', 180)
    if middle_left:
        return ('1b.svg', 270)

    # Diagonals, they still don't have very much effect
    # We treat it as if it was alone
    if top_left:
        return ('2b.svg', 0)
    if top_right:
        return ('2b.svg', 0)
    if bottom_left:
        return ('2b.svg', 0)
    if bottom_right:
        return ('2b.svg', 0)

    raise Exception('Not even one module touching, this is wrong.')


def _two_touching(top_left=False, top_center=False, top_right=False,
                  middle_left=False, middle_right=False,
                  bottom_left=False, bottom_center=False,
                  bottom_right=False):

    # First the cross
    if top_center and bottom_center:
        return ('1b3b.svg', 0)
    if middle_left and middle_right:
        return ('1b3b.svg', 90)

    # Checking for curves
    if middle_left and top_center:
        return ('2a1b.svg', 0)
    if top_center and middle_right:
        return ('2a1b.svg', 90)
    if middle_right and bottom_center:
        return ('2a1b.svg', 180)
    if middle_left and bottom_center:
        return ('2a1b.svg', 270)

    # Let's check if position is a path ending (1 diagonal, 1 touching side)
    cross = [top_center, middle_right, bottom_center, middle_left]

    if cross.count(True) == 1:
        return _one_touching(top_left=False, top_center=top_center,
                             top_right=False, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=False,
                             bottom_center=bottom_center,
                             bottom_right=False)
    # Every other possibility are diagonal combinations, we don't care,
    # and treat it like it was alone.
    return ('2b.svg', 0)


def _three_touching(top_left=False, top_center=False, top_right=False,
                    middle_left=False, middle_right=False,
                    bottom_left=False, bottom_center=False,
                    bottom_right=False):

    # First the cross
    if middle_left and top_center and middle_right:
        return ('2a1b2c.svg', 0)
    if top_center and middle_right and bottom_center:
        return ('2a1b2c.svg', 90)
    if middle_left and middle_right and bottom_center:
        return ('2a1b2c.svg', 180)
    if middle_left and top_center and bottom_center:
        return ('2a1b2c.svg', 270)

    cross = [top_center, middle_right, bottom_center, middle_left]

    # Let's check if it's a curve position is a path ending
    # (2 in curve, 1 in a diagonal)
    if cross.count(True) == 2:
        # Let's pretend the other touching nodes don't exist
        # pass only the cross values
        return _two_touching(top_left=False, top_center=top_center,
                             top_right=False, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=False,
                             bottom_center=bottom_center,
                             bottom_right=False)

    elif cross.count(True) == 1:
        return _one_touching(top_left=False, top_center=top_center,
                             top_right=False, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=False,
                             bottom_center=bottom_center,
                             bottom_right=False)
    # Every other possibility means three nodes in diagonals
    # we treat it like it's alone
    return ('2b.svg', 0)


def _four_touching(top_left=False, top_center=False, top_right=False,
                   middle_left=False, middle_right=False,
                   bottom_left=False, bottom_center=False,
                   bottom_right=False):

    #return ('2b.svg')
    cross = [top_center, middle_right, bottom_center, middle_left]
    diagonals = [top_left, top_right, bottom_right, bottom_left]

    if cross.count(True) == 4:
        #Complete cross
        return ('2a1b2c3b.svg', 0)
    if diagonals.count(True) == 4:
        # Just for completeness, all diagonals
        return ('2a1b2c3b.svg', 0)
    if cross.count(True) == 3:
        # Three in the cross, let's delegate.
        return _three_touching(top_left=False, top_center=top_center,
                               top_right=False, middle_left=middle_left,
                               middle_right=middle_right,
                               bottom_left=False,
                               bottom_center=bottom_center,
                               bottom_right=False)
    if cross.count(True) == 2:
        # Two in the cross, let's delegate.
        return _two_touching(top_left=False, top_center=top_center,
                             top_right=False, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=False,
                             bottom_center=bottom_center,
                             bottom_right=False)
    elif cross.count(True) == 1:
        return _one_touching(top_left=False, top_center=top_center,
                             top_right=False, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=False,
                             bottom_center=bottom_center,
                             bottom_right=False)

    # Every other posibility are all diagonals, treat it like alone node
    return ('2b.svg', 0)


def _5plus_touching(top_left=False, top_center=False, top_right=False,
                    middle_left=False, middle_right=False,
                    bottom_left=False, bottom_center=False,
                    bottom_right=False):

    cross = [top_center, middle_right, bottom_center, middle_left]

    if cross.count(True) == 4:
        return _four_touching(top_left=False, top_center=top_center,
                              top_right=False, middle_left=middle_left,
                              middle_right=middle_right,
                              bottom_left=False,
                              bottom_center=bottom_center,
                              bottom_right=False)

    if cross.count(True) == 3:
        return _three_touching(top_left=False, top_center=top_center,
                               top_right=False, middle_left=middle_left,
                               middle_right=middle_right,
                               bottom_left=False,
                               bottom_center=bottom_center,
                               bottom_right=False)
    if cross.count(True) == 2:
        return _two_touching(top_left=False, top_center=top_center,
                             top_right=False, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=False,
                             bottom_center=bottom_center,
                             bottom_right=False)

    if cross.count(True) == 1:
        return _one_touching(top_left=False, top_center=top_center,
                             top_right=False, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=False,
                             bottom_center=bottom_center,
                             bottom_right=False)

    raise Exception('Five or more touching node, none in cross section,' +\
                    'impossible')


def _choose_module(top_left=False, top_center=False, top_right=False,
                   middle_left=False, middle_right=False,
                   bottom_left=False, bottom_center=False,
                   bottom_right=False):

    how_many = [top_left, top_center, top_right, middle_left, middle_right,
                bottom_left, bottom_center, bottom_right].count(True)

    if how_many == 0:
        return ('2b.svg', 0)
    if how_many == 1:
        return _one_touching(top_left=top_left, top_center=top_center,
                             top_right=top_right, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=bottom_left,
                             bottom_center=bottom_center,
                             bottom_right=bottom_right)
    if how_many == 2:
        return _two_touching(top_left=top_left, top_center=top_center,
                             top_right=top_right, middle_left=middle_left,
                             middle_right=middle_right,
                             bottom_left=bottom_left,
                             bottom_center=bottom_center,
                             bottom_right=bottom_right)
    if how_many == 3:
        return _three_touching(top_left=top_left, top_center=top_center,
                               top_right=top_right, middle_left=middle_left,
                               middle_right=middle_right,
                               bottom_left=bottom_left,
                               bottom_center=bottom_center,
                               bottom_right=bottom_right)

    if how_many == 4:
        return _four_touching(top_left=top_left, top_center=top_center,
                              top_right=top_right, middle_left=middle_left,
                              middle_right=middle_right,
                              bottom_left=bottom_left,
                              bottom_center=bottom_center,
                              bottom_right=bottom_right)
    if how_many >= 5:
        return _5plus_touching(top_left=top_left, top_center=top_center,
                               top_right=top_right, middle_left=middle_left,
                               middle_right=middle_right,
                               bottom_left=bottom_left,
                               bottom_center=bottom_center,
                               bottom_right=bottom_right)


def _is_outer_eye_position(row, column, qr_size):
    if row == 0 and column == 0:
        # Top left corner eye
        return True
    if row == (qr_size - 7) and column == 0:
        # Bottom left corner eye
        return True
    if row == 0 and column == (qr_size - 7):
        # Top right corner eye
        return True
    return False


def _within_eyes(row, column, qr_size):
    if row <= 6 and column <= 6:
        # In top left corner eye
        return True
    if row >= (qr_size - 7) and column <= 6:
        # In bottom left corner eye
        return True
    if row <= 6 and column <= (qr_size - 7):
        # In top right corner eye
        return True
    return False


def _within_outer_eye(row, column, qr_size):
    # Top left eye
    if row == 0 and column <= 6:
        # Top edge
        return True
    if row <= 6 and column == 0:
        # Left edge
        return True
    if row <= 6 and column == 6:
        # Right edge
        return True
    if row == 6 and column <= 6:
        # Bottom edge
        return True

    # Bottom left eye
    if row == qr_size - 7 and column <= 6:
        # Top edge
        return True
    if row == qr_size - 1 and column <= 6:
        # Bottom edge
        return True
    if row >= qr_size - 7 and column == 0:
        # Left edge
        return True
    if row >= qr_size - 7 and column == 6:
        # Right edge
        return True

    # Top right eye
    if row == 0 and column >= (qr_size - 7):
        # Top edge
        return True
    if row == 6 and column >= (qr_size - 7):
        # Bottom edge
        return True
    if row <= 6 and column == (qr_size - 7):
        # Left edge
        return True
    if row <= 6 and column == (qr_size - 1):
        # Right edge
        return True
    return False


def _within_inner_eye(row, column, qr_size):
    if row >= 2 and row <= 4 and column >= 2 and column <= 4:
        # In top left inner eye
        return True
    if row >= qr_size - 6 and row <= qr_size - 3 and column >= 2 \
                                                    and column <= 4:
        # In the bottom left inner eye
        return True
    if row >= 2 and row <= 4 and column >= (qr_size - 6) \
                                        and column <= (qr_size - 3):
        # In the top right inner eye
        return True
    return False


def _is_inner_eye_position(row, column, qr_size):
    if row == 2 and column == 2:
        # Top left corner center eye first module
        return True
    if row == (qr_size - 5) and column == 2:
        # Bottom left corner center eye first module
        return True
    if row == 2 and column == (qr_size - 5):
        # Top right corner center eye first module
        return True
    return False


def _qrcode_to_svg(qrcode, style='default', style_color='#000000',
                    inner_eye_style='default', inner_eye_color='#000000',
                    outer_eye_style='default', outer_eye_color='#000000',
                    bg_color='#FFFFFF', size=200):

    style_dict = None
    inner_eyes_dict = None
    outer_eyes_dict = None
    if style:
        style_dict = _get_style_dict(style)  # Build the style dictionary
    if outer_eye_style:
        outer_eyes_dict = _get_eyes_dict(outer_eye_style)
    if inner_eye_style:
        inner_eyes_dict = _get_eyes_dict(inner_eye_style)

    module_count = qrcode.getModuleCount()   # Number of rows/columns of the QR
    # size             scale
    # 10px               1
    # new_block_size     x
    new_block_size = float(size) / (module_count + (QUIET_ZONE * 2))
    block_scale = new_block_size / BLOCK_SIZE
    # Width of the SVG QR code
    #width = str((module_count + (QUIET_ZONE * 2)) * BLOCK_SIZE)
    width = str(size)
    height = width                          # Height of the SVG QR code
    svg_doc = et.Element('svg', width=width, height=height, version='1.1',
                         xmlns='http://www.w3.org/2000/svg')

    # Background square
    et.SubElement(svg_doc, 'rect', x='0', y='0', width=width, height=height,
                  fill=bg_color)

    for row in range(module_count):
        for column in range(module_count):
            if not qrcode.isDark(row, column):
                continue
            # Module is active
            # create an SVG XML element (see the SVG specification
            # for attribute details)
            top_left = qrcode.isDark(row, column - 1)
            top_center = qrcode.isDark(row - 1, column)
            top_right = qrcode.isDark(row + 1, column + 1)
            middle_left = qrcode.isDark(row, column - 1)
            middle_right = qrcode.isDark(row, column + 1)
            bottom_left = qrcode.isDark(row + 1, column - 1)
            bottom_center = qrcode.isDark(row + 1, column)
            bottom_right = qrcode.isDark(row + 1, column + 1)

            # Let's check if there's a style for outer eye and insert the shape
            if outer_eyes_dict and _is_outer_eye_position(row, column,
                                                         module_count):
                _insert_shape(column, row, ('outer.svg', 0), svg_doc,
                              style_dict=outer_eyes_dict,
                              color=outer_eye_color, block_scale=block_scale)
                continue

            # Let's check if there's a style for inner eye and insert the shape
            if inner_eyes_dict and _is_inner_eye_position(row, column,
                                                         module_count):
                _insert_shape(column, row, ('inner.svg', 0), svg_doc,
                              style_dict=inner_eyes_dict,
                              color=inner_eye_color, block_scale=block_scale)
                continue

            if outer_eyes_dict and _within_outer_eye(row, column,
                                                     module_count):
                continue

            if inner_eyes_dict and _within_inner_eye(row, column,
                                                     module_count):
                continue

            shape = _choose_module(top_left=top_left,
                                   top_center=top_center,
                                   top_right=top_right,
                                   middle_left=middle_left,
                                   middle_right=middle_right,
                                   bottom_left=bottom_left,
                                   bottom_center=bottom_center,
                                   bottom_right=bottom_right)

            _insert_shape(column, row, shape, svg_doc,
                          style_dict=style_dict, color=style_color,
                          block_scale=block_scale)

    filelike = cStringIO.StringIO()
    filelike.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
    filelike.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
    filelike.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
    filelike.write(et.tostring(svg_doc))
    return filelike


def string_to_eclevel(level):
    if level == 'L':
        return pyqrcode.QRErrorCorrectLevel.L
    elif level == 'M':
        return pyqrcode.QRErrorCorrectLevel.M
    elif level == 'Q':
        return pyqrcode.QRErrorCorrectLevel.Q
    elif level == 'H':
        return pyqrcode.QRErrorCorrectLevel.H
    else:
        return pyqrcode.QRErrorCorrectLevel.Q


def generate_QR_for_text(text, eclevel='Q', style='default',
                         style_color='#000000', inner_eye_style='default',
                         inner_eye_color='#000000', outer_eye_style='default',
                         outer_eye_color='#000000', bg_color='#FFFFFF',
                         size=200, ec_level='Q'):

    ec_level_validation(ec_level)
    color_validation(style_color)
    color_validation(inner_eye_color)
    color_validation(outer_eye_color)
    color_validation(bg_color)
    size_validation(size)
    ec_level_validation(ec_level)
    style_validation(style)
    inner_eye_style_validation(inner_eye_style)
    outer_eye_style_validation(outer_eye_style)
    qr_code = pyqrcode.MakeQR(text,
                              errorCorrectLevel=string_to_eclevel(ec_level))
    return _qrcode_to_svg(qr_code, style=style, style_color=style_color,
                          inner_eye_style=inner_eye_style,
                          inner_eye_color=inner_eye_color,
                          outer_eye_style=outer_eye_style,
                          outer_eye_color=outer_eye_color,
                          size=size, bg_color=bg_color)
