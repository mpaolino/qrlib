import qrsvg
import pyqrcode


qrcode = qrsvg.generate_QR_for_url('http://ideal.com.uy', color='#CC66CC',
                                   style='circle')
f = open('test.svg', 'w')
f.write(qrcode.getvalue())
f.close()

pil = pyqrcode.MakeQRImage('http://ideal.com.uy')
pil.save('test.gif', 'GIF')
