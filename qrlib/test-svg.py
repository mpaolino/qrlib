import qrlib
import pyqrcode


qrcode = qrlib.generate_QR_for_url('http://ideal.com.uy')
#archivo = qrlib._qrcode_to_svg(qrcode, style='stylish', color='blue')
archivo = qrlib._qrcode_to_svg(qrcode, color='#CC66CC', style='stylish')
f = open('test.svg', 'w')
f.write(archivo.getvalue())
f.close()

pil = pyqrcode.MakeQRImage('http://ideal.com.uy')
pil.save('test.gif', 'GIF')
