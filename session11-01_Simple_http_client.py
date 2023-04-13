
'''
JEDNODUCHY KLIENT - METODA GET
'''

import http.client

con = http.client.HTTPSConnection('fortisauris.com')  # rozdiel medzi HTTP - HTTPS  -

# zaregistovat tatrabanka.sk   CA
# zaregistorvat ta.trabanka.sk  CA  https

con.request('GET', '/')  # defaultne je nastaveny index.html alebo main.html
r1 = con.getresponse()
headers = r1.getheaders()  # hlavicka dokumentu
print(r1.status, r1.reason)
print('HEADERS:\n', headers)

obsah = r1.read()
print(obsah)