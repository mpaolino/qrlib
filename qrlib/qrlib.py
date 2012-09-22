# coding: utf-8
# (c) Copyright 2011 by Miguel Paolino <mpaolino@ideal.com.uy>
from config import (INTERIOR_SMALL, INTERIOR_MEDIUM, INTERIOR_LARGE,
                    EXTERIOR_SMALL, EXTERIOR_MEDIUM, EXTERIOR_LARGE,
                    LOGO_IMAGE_PATH, LOGO_MARGIN, FOOTER_TEXT_FONT,
                    FOOTER_TEXT_COLOR, FOOTER_URL, TEXT_TRANS,
                    BLOCK_SIZE, SHAPE_GROUP, STYLE_FILES, QUIET_ZONE)

from reportlab.graphics import (renderPDF, renderPM, barcode)
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from validation import (format_validation, application_validation, 
                        appsize_validation, language_validation,
                        color_validation, ec_level_validation)
import cStringIO
import Image
# Monkey patch ReportLab 
# http://stackoverflow.com/questions/2227493/reportlab-and-python-imaging-library-images-from-memory-issue
import reportlab.lib.utils
reportlab.lib.utils.Image= Image
import math
from xml.etree import cElementTree as et
import pyqrcode
import re
import ipdb


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def generate_qr_file(qr_svg, language='es', qr_format='PDF', app='interior',
                     app_size='small', decorate=True):
    """
        Returns a QR of the provided text in the format and size specified
        Specific values are customizable in config.py

        Parameters:

            language: Text language for PDF footer. Values 'es', 'en', 'br'.
                      Defaults to 'es'.

            qr_format: Format of QR, Values 'PDF', 'GIF', 'PNG', 'JPG'. 
                       Defaults to 'PDF'.

            app: Application for QR, 'interior' or 'exterior'. 
                 Automatically chooses error correction level for QR.
                 Defaults to 'interior'.

            app_size: Application size, 'small', 'medium', 'large'.
                      Defaults to 'small'.
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

    page_size = landscape(A4)
    page_width, page_height = page_size
    qr_width = None
    qr_height = None
    ec_level = None
    # TODO: please, use a little introspection and look for attribs
    if app == 'interior':
        if app_size == 'small':
            ec_level=INTERIOR_SMALL['error_correction']
            qr_width=INTERIOR_SMALL['width']
            qr_height=INTERIOR_SMALL['height']
        elif app_size == 'medium':
            ec_level=INTERIOR_MEDIUM['error_correction']
            qr_width=INTERIOR_MEDIUM['width']
            qr_height=INTERIOR_MEDIUM['height']
        elif app_size == 'large':
            ec_level=INTERIOR_LARGE['error_correction']
            qr_width=INTERIOR_LARGE['width']
            qr_height=INTERIOR_LARGE['height']
    elif app == 'exterior':
        if app_size == 'small':
            ec_level=EXTERIOR_SMALL['error_correction']
            qr_width=EXTERIOR_SMALL['width']
            qr_height=EXTERIOR_SMALL['height']
        elif app_size == 'medium':
            ec_level=EXTERIOR_MEDIUM['error_correction']
            qr_width=EXTERIOR_MEDIUM['width']
            qr_height=EXTERIOR_MEDIUM['height']
        elif app_size == 'large':
            ec_level=EXTERIOR_LARGE['error_correction']
            qr_width=EXTERIOR_LARGE['width']
            qr_height=EXTERIOR_LARGE['height']
    else:
        raise Exception('No app type defined for QR generation, looks like' +\
                        ' validation failed. Awkward!')
    
    filelike = cStringIO.StringIO()
    qr_canvas = canvas.Canvas(filelike, pagesize=page_size)
    qr_draw = barcode.createBarcodeDrawing("QR", value=text, barWidth=qr_width,
                                           barHeight=qr_height,
                                           barLevel=ec_level,
                                           barBorder=4)
    qrsvg_draw = qrsvg.generate_QR_for_url(text, barWidth=qr_width,
                                           barHeight=qr_height,
                                           ec_level=ec_level,
                                           barBorder=4)


    if qr_format == 'PDF':
        # Center qr draw on first half of the page
        qr_draw_x = (page_width / 4) - (qr_width / 2)
        qr_draw_y = (page_height / 2) - (qr_height / 2)
        sq_width = qr_width + 2 
        sq_height = qr_height + 2
        center_distance = distance((qr_width, qr_height), 
                                   (sq_width, sq_height))

        #renderPDF.draw(qr_draw, qr_canvas, x=qr_draw_x, y=qr_draw_y)
        #renderPM.drawToFile(qr_draw, filelike, fmt='PNG')
       
        # Lazy ass bastard, find out the block pixel numbers and do this 
        # with pyqrcode 
        imageqr = generate_qr_file(text, app=app, app_size=app_size, 
                                   qr_format='GIF')
        imageqr.seek(0)
        pil = Image.open(imageqr).convert('L')
        imagereader = ImageReader(pil)
        qr_canvas.drawImage(imagereader, qr_draw_x, qr_draw_y)

        sq_draw_x = qr_draw_x - (center_distance / 2)
        sq_draw_y = qr_draw_y - (center_distance / 2)

        qr_canvas.saveState()
        qr_canvas.setDash((5,2))
        qr_canvas.rect(x=sq_draw_x, y=sq_draw_y, width=qr_width,
                       height=qr_height, fill=0)
        qr_canvas.restoreState()

        #Get logo dimentions
        logo = Image.open(LOGO_IMAGE_PATH)
        logo_width, logo_height = logo.size
        logo_x = qr_draw_x + qr_width - logo_width - LOGO_MARGIN
        logo_y = qr_draw_y - logo_height + LOGO_MARGIN

        qr_canvas.drawImage(LOGO_IMAGE_PATH, x=logo_x, y=logo_y, mask='auto')
        # Save canvas to file
        qr_canvas.setPageCompression(pageCompression=1)
        qr_canvas.setCreator("http://cuadraditos.uy")
        qr_canvas.setAuthor("ideal")
        qr_canvas.save()

    else:
        renderPM.drawToFile(qr_draw, filelike, fmt=qr_format)

    return filelike 
    
def generate_custom_qr_file(text, error_correction, block_pixels, border_blocks,
                            language='es', logo=True):
    """Get's a custom QR with decorations"""
    non_decorated = _get_qr_pil(text, ec_level=error_correction,
                                block_pixels=block_pixels,
                                border_blocks=border_blocks)
    return _decorate_pil(non_decorated, language=language,
                        margin=block_pixels * border_blocks, logo=logo)


def _decorate_pil(one_pil, language='es', margin=100, logo=True):
    """Takes a PIL with encoded QR and decorates it"""
    # TTF font size must be aprox 1/4 of margin (given in pixels)
    font_size = margin / 4
    # Vertical margin from image inferior border (3 lines of text)
    v_margin = font_size * 3
    (pil_width, pil_height) = one_pil.size

    if logo:
        footer = Image.open(LOGO_PATH)
        (footer_width, footer_height) = footer.size
        one_pil.paste(footer, (pil_width - margin - footer_width,
                      margin / 2 - footer_height / 2), footer)

    draw = ImageDraw.Draw(one_pil)

    if language not in TEXT_TRANS:
        raise Exception('No "%s" language text.' % language)

    text_font = ImageFont.truetype(FOOTER_TEXT_FONT, font_size)
    draw.text((margin, pil_height - v_margin), TEXT_TRANS[language],
              font=text_font, fill=FOOTER_TEXT_COLOR)
    # We give an extra 4 px for line separation
    draw.text((margin, pil_height - v_margin + font_size + 4),
               FOOTER_URL, font=text_font, fill=FOOTER_TEXT_COLOR)
    return one_pil
