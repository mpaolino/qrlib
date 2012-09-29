import qrsvg
import sys

#url = 'http://ilskdjakldjlkadjlkajsdlkajdlkadeal.com.uyasdklajsdkljaasdasdasdasdasdasdasddaskjasdkjhaskdjhajkdhajksdhakjsdhakjshdakjsdhakjsdhaksjdhaskjdhskajdhaksjdhaskdjh'
url = 'http://cuadraditos.uy'
#url = 'http://a'


ec_level = 'L'
if len(sys.argv) > 1:
    ec_level = sys.argv[1]

qrcode = qrsvg.generate_QR_for_text(url, 
                                    style_color='#1C96E8',
                                    style='heavyround',
                                    inner_eye_style='heavyround',
                                    inner_eye_color='#00D644',
                                    outer_eye_style='heavyround',
                                    outer_eye_color='#00D644',
                                    size=330, ec_level=ec_level)
f = open('test.svg', 'w')
f.write(qrcode.getvalue())
f.close()
