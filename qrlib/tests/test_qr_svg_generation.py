# -*- coding: utf-8 -*-
import os
from qrsvg import generate_QR_for_text
import Image
import cairosvg
import zbar
import unittest2 as unittest
import cStringIO
import ipdb

class GenerateSVGTestCase(unittest.TestCase):

    def setUp(self):
        pass        

    def tearDown(self):
        pass

    def test_svg(self):
        generated_svg = generate_QR_for_text(u'JUST TEXT', size=300)
        converted_file = cStringIO.StringIO()
        ipdb.set_trace()
        new_png = cairosvg.svg2png(generated_svg.getvalue(),
                                   write_to=converted_file)
        converted_file.seek(0)
        pil = Image.open(converted_file).convert('L')
        width, height = pil.size
        raw = pil.tostring()
        
        image = zbar.Image(width, height, 'Y800', raw)
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        scanner.scan(image)
        self.assertEqual(len(image.symbols), 1)
        for symbol in image:
            self.assertEqual(symbol.data,'JUST TEXT')

if __name__ == '__main__':
    unittest.main()
