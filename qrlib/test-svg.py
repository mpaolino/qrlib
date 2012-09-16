import qrsvg
import pyqrcode

#url = 'http://ilskdjakldjlkadjlkajsdlkajdlkajsdlkajdlkjaldkjalksdjalkdjaslkdjaslkdjaslkdjaslkdjaslkdjsalkdjsalkdjaslkdjaslkdjaslkdjadeal.com.uy'
url = 'asadsdasdasd'

qrcode = qrsvg.generate_QR_for_url(url, 
                                   style_color='#CC66CC',
                                   style='circle',
                                   inner_eye_style='circle',
                                   inner_eye_color='green',
                                   outer_eye_style='stylish',
                                   outer_eye_color='purple')
f = open('test.svg', 'w')
f.write(qrcode.getvalue())
f.close()

pil = pyqrcode.MakeQRImage(url)
pil.save('test.gif', 'GIF')
