import pyqrcode
from xml.etree import cElementTree as et
from config import (BLOCK_SIZE, SHAPE_GROUP, STYLE_FILES, QUIET_ZONE)

import re
import cStringIO


def _get_style_dict(style):
    '''
        Iterates over STYLE_FILES for the defined style and builds
        a dictionary with it's shape groups
    '''
    style = style.lower()
    directory = 'static/styles/' + style
    style_dict = {}

    for filename in STYLE_FILES:
        filepath = directory + '/' + filename
        document = et.parse(filepath)
        root = document.getroot()
        style_dict[filename] = []
        for group_elem in root.iter(SHAPE_GROUP):
            style_dict[filename].append(group_elem)
    return style_dict


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


def _insert_shape(x, y, shape_w_rotation, final_svg, style_dict=None,
                                                            color='#000000'):
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

    bound = QUIET_ZONE * BLOCK_SIZE
    if style_dict == None:
        et.SubElement(final_svg, 'rect', x=str((x * BLOCK_SIZE) + bound),
                      y=str((y * BLOCK_SIZE) + bound), width=str(BLOCK_SIZE),
                      height=str(BLOCK_SIZE), fill=color)
        return

    translate = "translate( %(x)s %(y)s )" % \
                {
                  'x': str((x * BLOCK_SIZE) + bound),
                  'y': str((y * BLOCK_SIZE) + bound)
                }

    if int(rotation) != 0:
        rotate = "rotate(%(angle)s, %(center)s, %(center)s)" % \
                {
                 'angle': str(rotation),
                 'center': str((float(BLOCK_SIZE) / 2))
                }
        translate = translate + " " + rotate

    new_container = et.SubElement(final_svg, 'g', transform=translate)

    for elem in style_dict[shape]:
        _set_attrib(elem, color=color)
        new_container.append(elem)


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
        return _three_touching(top_left=False, top_center=top_center,
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
    if how_many > 4:
        return ('2a1b2c3b.svg', 0)


def _qrcode_to_svg(qrcode, style=None, color='#000000'):
    style_dict = None
    if style:
        style_dict = _get_style_dict(style)  # Build the style dictionary
    module_count = qrcode.getModuleCount()   # Number of rows/columns of the QR
    # Width of the SVG QR code
    width = str((module_count + (QUIET_ZONE * 2)) * BLOCK_SIZE)
    height = width                          # Height of the SVG QR code
    svg_doc = et.Element('svg', width=width, height=height, version='1.1',
                         xmlns='http://www.w3.org/2000/svg')
    for row in range(module_count):
        for column in range(module_count):
            if not qrcode.isDark(row, column):
                continue
            # Module is active
            # create an SVG XML element (see the SVG specification
            # for attribute details)
            top_left = qrcode.isDark(row - 1, column - 1)
            top_center = qrcode.isDark(row, column - 1)
            top_right = qrcode.isDark(row, column + 1)
            middle_left = qrcode.isDark(row - 1, column)
            middle_right = qrcode.isDark(row + 1, column)
            bottom_left = qrcode.isDark(row - 1, column + 1)
            bottom_center = qrcode.isDark(row, column + 1)
            bottom_right = qrcode.isDark(row + 1, column + 1)

            shape = _choose_module(top_left=top_left,
                                   top_center=top_center,
                                   top_right=top_right,
                                   middle_left=middle_left,
                                   middle_right=middle_right,
                                   bottom_left=bottom_left,
                                   bottom_center=bottom_center,
                                   bottom_right=bottom_right)

            _insert_shape(column, row, shape, svg_doc,
                          style_dict=style_dict, color=color)

    filelike = cStringIO.StringIO()
    filelike.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
    filelike.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
    filelike.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
    filelike.write(et.tostring(svg_doc))
    return filelike


def generate_QR_for_url(url, style=None, color='#000000'):
    qr_code = pyqrcode.MakeQR(url,
                              errorCorrectLevel=pyqrcode.QRErrorCorrectLevel.Q)
    return _qrcode_to_svg(qr_code, style=style, color=color)
