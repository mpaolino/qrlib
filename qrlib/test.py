import qrlib
f = open('/home/mpaolino/cuadraditos.pdf', 'w')
cosa = qrlib.generate_qr_file("cosa", app='exterior', app_size='large', 
                              qr_format='PDF')
f.write(cosa.getvalue())
f.close()

