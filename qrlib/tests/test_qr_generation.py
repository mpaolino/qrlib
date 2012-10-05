# -*- coding: utf-8 -*-
import os
from qrlib import generate_qr_file
from qrlib.exceptions import (StyleMissing, InnerEyeStyleMissing,
                              OuterEyeStyleMissing)
import Image 
import zbar
import unittest2 as unittest
import ipdb


class GeneratePDFTestCase(unittest.TestCase):

    def setUp(self):
        pass        

    def tearDown(self):
        pass

    def qr_image_format(self, qr_format, style='default',
                        inner_eye_style='default',
                        outer_eye_style='default'):

        generated_img = generate_qr_file('JUST SOME TEXT', qr_format=qr_format,
                                         style=style,
                                         inner_eye_style=inner_eye_style,
                                         outer_eye_style=outer_eye_style)
        generated_img.seek(0)
        pil = Image.open(generated_img).convert('L')
        width, height = pil.size
        raw = pil.tostring()
        image = zbar.Image(width, height, 'Y800', raw)
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        scanner.scan(image)
        self.assertEqual(len(image.symbols), 1)
        for symbol in image:
            self.assertEqual(symbol.data,'JUST SOME TEXT')

    def test_gif(self):
        self.qr_image_format('GIF')

    def test_png(self):
        self.qr_image_format('PNG')

    def test_jpeg(self):
        self.qr_image_format('JPEG')

    def test_fail_style(self):
       self.assertRaises(StyleMissing, self.qr_image_format, 'PNG',
                         style='NONE')

    def test_fail_innereyestyle(self):
       self.assertRaises(InnerEyeStyleMissing, self.qr_image_format, 'PNG',
                         inner_eye_style='NONE')

    def test_fail_outereyestyle(self):
       self.assertRaises(OuterEyeStyleMissing, self.qr_image_format, 'PNG',
                         outer_eye_style='NONE')


if __name__ == '__main__':
    unittest.main()
