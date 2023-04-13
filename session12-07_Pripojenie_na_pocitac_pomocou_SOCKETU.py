
'''
PRIPOJENIE NA POCITAC POMOCOU MODULU SOCKET
'''

import socket
import time

# netcat - sietovy nastroj na diagnostiku sietoveho spojenia

s = socket.socket()
ADRESA = '188.121.170.77'  # STATICKA VEREJNA - nasadomena.sk  DNS
PORT = 80   # http
try:
    print('SKUSAME SA NAPOJIT NA ADRESU', ADRESA, PORT)
    t1 = time.time()
    s.connect((ADRESA,PORT))
    print((time.time()-t1)*1000)
    print('BINGO')
except Exception as e:
    print(e.__repr__(), e)
finally:
    pass

