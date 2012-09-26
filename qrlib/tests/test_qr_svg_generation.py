# -*- coding: utf-8 -*-
from qrsvg import generate_QR_for_text
import Image
import cairosvg
import zbar
import unittest2 as unittest
import cStringIO


class GenerateSVGTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def generate_svg(self, text, size):
        generated_svg = generate_QR_for_text(text, size=size)
        converted_file = cStringIO.StringIO()
        cairosvg.svg2png(generated_svg.getvalue(),
                         write_to=converted_file)
        converted_file.seek(0)
        pil = Image.open(converted_file).convert('L')
        width, height = pil.size
        self.assertEqual(width, size)
        self.assertEqual(height, size)
        raw = pil.tostring()

        image = zbar.Image(width, height, 'Y800', raw)
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        scanner.scan(image)
        self.assertEqual(len(image.symbols), 1)
        for symbol in image:
            self.assertEqual(symbol.data, text)

    def test_svg(self):
        self.generate_svg(u'JUST TEXT', size=100)

if __name__ == '__main__':
    unittest.main()
