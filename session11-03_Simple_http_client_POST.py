'''
JEDNODUCHY HTTP KLIENT - METODA POST


obsahuje tz
'''

import http.client
import json

# NAJCASETEJSIE METODY - GET, POST
# DELETE, PUT, PATCH

# GET adresu html dokumentu  200

# POST adresu ... obsahuje tzv. payload  v podobe jsonu

# {'login': 'uzivatel',
#  'password': 'bryndza123'}

con = http.client.HTTPSConnection('www.httpbin.org') # server na testovanie requestov
headers = {'Content-type': 'application/json'}

foo = {'text': 'TOTO JE NAS TEXT'}  # toto je nas payload
json_data = json.dumps(foo)  # konvertujeme to na json

con.request('POST', '/post', json_data, headers)  # tu posielame request
res = con.getresponse()  # tu je odpoved

print(res.read().decode())