# -*- coding: utf-8 -*-
import os
from qrlib import generate_qr_file
import Image 
import zbar
import unittest2 as unittest
import ipdb


class GeneratePDFTestCase(unittest.TestCase):

    def setUp(self):
        pass        

    def tearDown(self):
        pass

    def qr_image_format(self, qr_format):
        generated_img = generate_qr_file('JUST SOME TEXT', qr_format=qr_format)
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

#    def test_pdf(self):
#        self.qr_image_format('PDF')

if __name__ == '__main__':
    unittest.main()
