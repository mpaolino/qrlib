# -*- coding: utf-8 -*-
import os
from qrlib import generate_qr_file
import Image 
import zbar
import unittest2 as unittest


class GeneratePDFTestCase(unittest.TestCase):

    def setUp(self):
        pass        

    def tearDown(self):
        pass

    def qr_image_format(self, img_format):
        generated_img = generate_qr_file('JUST TEXT', qr_format=img_format)
        #pdb.set_trace()
        generated_img.seek(0)
        pil = Image.open(generated_img).convert('L')
        #pil = Image.open(generated_gif)
        width, height = pil.size
        raw = pil.tostring()
        image = zbar.Image(width, height, 'Y800', raw)
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        scanner.scan(image)
        self.assertEqual(len(image.symbols), 1)
        for symbol in image:
            self.assertEqual(symbol.data,'JUST TEXT')

    def test_gif(self):
        self.qr_image_format('GIF')

    def test_png(self):
        self.qr_image_format('PNG')

    def test_jpg(self):
        self.qr_image_format('JPG')

    def test_pdf(self):
        generated_pdf = generate_qr_file(u'JUST TEXT', qr_format='PDF')

if __name__ == '__main__':
    unittest.main()
