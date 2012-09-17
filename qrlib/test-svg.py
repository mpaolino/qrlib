import qrsvg
import pyqrcode

#url = 'http://ilskdjakldjlkadjlkajsdlkajdlkajsdlkajdlkjaldkjalksdjalkdjaslkdjaslkdjaslkdjaslkdjaslkdjsalkdjsalkdjaslkdjaslkdjaslkdjadeal.com.uy'
url = 'http://ideal.com.uy'

qrcode = qrsvg.generate_QR_for_url(url, 
                                   style_color='#193CD4',
                                   style='sieve',
                                   inner_eye_style='sieve',
                                   inner_eye_color='#193CD4',
                                   outer_eye_style='sieve',
                                   outer_eye_color='#1466C4')
f = open('test.svg', 'w')
f.write(qrcode.getvalue())
f.close()

pil = pyqrcode.MakeQRImage(url)
pil.save('test.gif', 'GIF')
