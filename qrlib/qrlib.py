# coding: utf-8
# (c) Copyright 2012 by Miguel Paolino <mpaolino@ideal.com.uy>
from config import (INTERIOR_SMALL, INTERIOR_MEDIUM, INTERIOR_LARGE,
                    EXTERIOR_SMALL, EXTERIOR_MEDIUM, EXTERIOR_LARGE,
                    LOGO_IMAGE_PATH, LOGO_MARGIN, DASHFRAME_MARGIN,
                    SCISSORS_IMAGE_PATH, PDF_CREATOR, PDF_AUTHOR,
                    INSTRUCTIONS_IMAGE_PATH, INSTRUCTIONS_CENTER_OFFSET)
from . import qrsvg
import cairosvg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import HexColor
from .validation import (format_validation, application_validation,
                        appsize_validation, language_validation,
                        ec_level_validation, size_validation,
                        style_validation, inner_eye_style_validation,
                        outer_eye_style_validation)
import cStringIO
import Image
# Monkey patch ReportLab
# http://stackoverflow.com/questions/2227493/\
# reportlab-and-python-imaging-library-images-from-memory-issue
import reportlab.lib.utils
reportlab.lib.utils.Image = Image


def _gen_pdf(qr_pil, instructions=True, bg_color='#FFFFFF', frame=True,
             put_logo=True):
    """
        Receives a PIL image with a QR and generates a PDF output
        in a filelike (StringIO)
    """
    (qr_width, qr_height) = qr_pil.size  # qr_width == qr_height, always
    filelike = cStringIO.StringIO()
    page_size = landscape(A4)
    page_width, page_height = page_size
    qr_canvas = canvas.Canvas(filelike, pagesize=page_size)

    # Center qr draw on first half of the page
    qr_draw_x = (page_width / 4) - (qr_width / 2)
    qr_draw_y = (page_height / 2) - (qr_height / 2)
    sq_width = qr_width + DASHFRAME_MARGIN
    sq_height = qr_height + DASHFRAME_MARGIN
    sq_draw_x = qr_draw_x - (DASHFRAME_MARGIN / 2)
    sq_draw_y = qr_draw_y - (DASHFRAME_MARGIN / 2)

    # Place dashed frame and QR PIL in the canvas
    if frame:
        qr_canvas.saveState()
        qr_canvas.setDash((5, 2))
        hexcolor = HexColor(bg_color)
        r = hexcolor.red
        g = hexcolor.green
        b = hexcolor.blue
        qr_canvas.setFillColorRGB(r, g, b)
        qr_canvas.rect(x=sq_draw_x, y=sq_draw_y, width=sq_width,
                       height=sq_height, fill=1)
        qr_canvas.restoreState()

        # Add the scissors to dashed frame
        scissors = Image.open(SCISSORS_IMAGE_PATH)
        scissors_width, scissors_height = scissors.size
        scissors_x = sq_draw_x - scissors_width
        qr_canvas.drawImage(SCISSORS_IMAGE_PATH, x=scissors_x, y=sq_draw_y,
                            mask='auto')

    imagereader = ImageReader(qr_pil)
    qr_canvas.drawImage(imagereader, qr_draw_x, qr_draw_y)

    #Get logo dimentions and place it inside dashed frame
    if put_logo:
        logo = Image.open(LOGO_IMAGE_PATH)
        logo_width, logo_height = logo.size
        logo_x = sq_draw_x + (sq_width / 2) - (logo_width / 2)
        logo_y = sq_draw_y + LOGO_MARGIN
        qr_canvas.drawImage(LOGO_IMAGE_PATH, x=logo_x, y=logo_y, mask='auto')

    if instructions:
        #TODO: Paste the instructions in the PDF
        instructions = Image.open(INSTRUCTIONS_IMAGE_PATH)
        instruction_width, instruction_height = instructions.size
        inst_x = (page_width / 2) - INSTRUCTIONS_CENTER_OFFSET
        qr_canvas.drawImage(INSTRUCTIONS_IMAGE_PATH, x=inst_x,
                            y=(page_height / 2) - (instruction_width / 2),
                            mask='auto')

    # Set some file properties and save canvas to filelike
    qr_canvas.setPageCompression(pageCompression=1)
    qr_canvas.setCreator(PDF_CREATOR)
    qr_canvas.setAuthor(PDF_AUTHOR)
    qr_canvas.save()

    return filelike


def _generate_pil(text, size='100', ec_level='L', style='default',
                  style_color='#000000', inner_eye_style='default',
                  inner_eye_color='#000000', outer_eye_style='default',
                  outer_eye_color='#000000', bg_color='#FFFFFF'):

    generated_svg = qrsvg.generate_QR_for_text(text, size=size,
                                               ec_level=ec_level,
                                               style=style,
                                               style_color=style_color,
                                               inner_eye_style=inner_eye_style,
                                               inner_eye_color=inner_eye_color,
                                               outer_eye_style=outer_eye_style,
                                               outer_eye_color=outer_eye_color,
                                               bg_color=bg_color)
    converted_file = cStringIO.StringIO()
    cairosvg.svg2png(generated_svg.getvalue(),
                     write_to=converted_file)
    converted_file.seek(0)
    qr_pil = Image.open(converted_file)
    return qr_pil


def _gen_filelike(text, language='es', size=150, ec_level='L', qr_format='PDF',
                  instructions=True, style='default', style_color='#000000',
                  inner_eye_style='default', inner_eye_color='#000000',
                  outer_eye_style='default', outer_eye_color='#000000',
                  bg_color='#FFFFFF'):

    if qr_format == 'SVG':
        return qrsvg.generate_QR_for_text(text, size=size,
                                          ec_level=ec_level,
                                          style=style,
                                          style_color=style_color,
                                          inner_eye_style=inner_eye_style,
                                          inner_eye_color=inner_eye_color,
                                          outer_eye_style=outer_eye_style,
                                          outer_eye_color=outer_eye_color,
                                          bg_color=bg_color)

    pil = _generate_pil(text, size=size,
                        ec_level=ec_level,
                        style=style,
                        style_color=style_color,
                        inner_eye_style=inner_eye_style,
                        inner_eye_color=inner_eye_color,
                        outer_eye_style=outer_eye_style,
                        outer_eye_color=outer_eye_color,
                        bg_color=bg_color)

    if qr_format == 'PDF':
        return _gen_pdf(pil, instructions=instructions, bg_color=bg_color,
                        put_logo=True)
    if qr_format in ['GIF', 'JPEG', 'PNG']:
        filelike = cStringIO.StringIO()
        pil.save(filelike, qr_format)
        return filelike
    else:
        raise Exception('Awkward, unrecognised qr_format ' + \
                        '"%s". This should NOT happen.' % (qr_format))


def generate_qr_file(text, language='es', qr_format='PDF', app='interior',
                     app_size='small', instructions=True,
                     style='default', style_color='#000000',
                     inner_eye_style='default', inner_eye_color='#000000',
                     outer_eye_style='default', outer_eye_color='#000000',
                     bg_color='#FFFFFF'):
    """
        Returns a QR of the provided text in the format and predefined sizes
        specified in config.py

        Parameters:

            language: Text language for PDF instructions. Only 'es' spanish for
                      now.

            qr_format: Format of QR, Values 'PDF', 'GIF', 'PNG', 'JPEG', 'SVG'.
                       Defaults to 'PDF'.

            app: Application for QR, 'interior' or 'exterior'.
                 Automatically chooses error correction level for QR.
                 Defaults to 'interior'.

            app_size: Application size, 'small', 'medium', 'large'.
                      Defaults to 'small'.

            instructions: Print or not the instructions in the PDF

            style: Style to apply to QR blocks (one of static/styles).
                   Defaults to 'default' style.

            style_color: Hex color code for style. Defaults to #000000

            inner_eye_style: Style to apply to inner eyes of QR.
                             Defaults to 'default' style.

            inner_eye_color: Hex color code for inner eye style.
                             Defaults to #000000.

            outer_eye_style: Style to apply to inner eyes of QR.
                             Defaults to 'default' style.

            outer_eye_color: Hex color code for outer eye style.
                             Defaults to #000000.

            bg_color: Hex color code for QR background. Defaults to #FFFFFF
    """
    try:
        language = language.lower()
        qr_format = qr_format.upper()
        app = app.lower()
        app_size = app_size.lower()
        language_validation(language)
        format_validation(qr_format)
        application_validation(app)
        appsize_validation(app_size)
    except Exception, e:
        raise e

    ec_level = None
    # TODO: please, use a little introspection and look for attribs
    if app == 'interior':
        if app_size == 'small':
            ec_level = INTERIOR_SMALL['error_correction']
            size = INTERIOR_SMALL['size']
        elif app_size == 'medium':
            ec_level = INTERIOR_MEDIUM['error_correction']
            size = INTERIOR_MEDIUM['size']
        elif app_size == 'large':
            ec_level = INTERIOR_LARGE['error_correction']
            size = INTERIOR_LARGE['size']
    elif app == 'exterior':
        if app_size == 'small':
            ec_level = EXTERIOR_SMALL['error_correction']
            size = EXTERIOR_SMALL['size']
        elif app_size == 'medium':
            ec_level = EXTERIOR_MEDIUM['error_correction']
            size = EXTERIOR_MEDIUM['size']
        elif app_size == 'large':
            ec_level = EXTERIOR_LARGE['error_correction']
            size = EXTERIOR_LARGE['size']
        else:
            raise Exception('No app size defined for QR generation, ' +\
                            'looks like validation failed. Awkward!')
    else:
        raise Exception('No app type defined for QR generation, looks like' +\
                        ' validation failed. Awkward!')

    return _gen_filelike(text, size=size, ec_level=ec_level,
                         qr_format=qr_format, style=style,
                         style_color=style_color,
                         inner_eye_style=inner_eye_style,
                         inner_eye_color=inner_eye_color,
                         outer_eye_style=outer_eye_style,
                         outer_eye_color=outer_eye_color, bg_color=bg_color)


def generate_custom_qr_file(text, language='es', qr_format='PDF', size=150,
                            ec_level='L', instructions=True, style='default',
                            style_color='#000000', inner_eye_style='default',
                            inner_eye_color='#000000',
                            outer_eye_style='default',
                            outer_eye_color='#000000',
                            bg_color='#FFFFFF'):
    """
        Returns a QR of the provided text in the format and custom size
        and error corretion level.

        Parameters:

            language: Text language for PDF instructions. Only 'es' spanish for
                      now.

            qr_format: Format of QR, Values 'PDF', 'GIF', 'PNG', 'JPEG', 'SVG'.
                       Defaults to 'PDF'. No format besides PDF will show
                       instructions.

            size: Size in pixels for the generated QR. The size includes
                  a mandatory safe margin for QR readability. This border
                  size its relative to block sizes and can be customized
                  in config.py

            ec_level: Error correction level. Values:
                      'L' - approx 7%
                      'M' - approx 15%
                      'Q' - approx 25%
                      'H' - approx 30%

            instructions: Print or not the instructions in the PDF

            style: Style to apply to QR blocks (one of static/styles).
                   Defaults to 'default' style.

            style_color: Hex color code for style. Defaults to #000000

            inner_eye_style: Style to apply to inner eyes of QR.
                             Defaults to 'default' style.

            inner_eye_color: Hex color code for inner eye style.
                             Defaults to #000000.

            outer_eye_style: Style to apply to inner eyes of QR.
                             Defaults to 'default' style.

            outer_eye_color: Hex color code for outer eye style.
                             Defaults to #000000.

            bg_color: Hex color code for QR background. Defaults to #FFFFFF
    """

    try:
        language = language.lower()
        qr_format = qr_format.upper()
        ec_level = ec_level.upper()
        size = int(size)
        size_validation(size)
        ec_level_validation(ec_level)
        language_validation(language)
        format_validation(qr_format)
        style_validation(style)
        inner_eye_style_validation(inner_eye_style)
        outer_eye_style_validation(outer_eye_style)
    except Exception, e:
        raise e

    if qr_format == 'PDF' and size > EXTERIOR_LARGE['size']:
        raise Exception('size cannot be > ' + \
                        '%s when generating a PDF' % (EXTERIOR_LARGE['size']))

    return _gen_filelike(text, qr_format=qr_format, size=size,
                         ec_level=ec_level, style=style,
                         style_color=style_color,
                         inner_eye_style=inner_eye_style,
                         inner_eye_color=inner_eye_color,
                         outer_eye_style=outer_eye_style,
                         outer_eye_color=outer_eye_color, bg_color=bg_color)
