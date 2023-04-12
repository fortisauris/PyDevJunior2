'''
JEDNODUCHY HTTP KLIENT - METODA POST
'''

import http.client
import json

# NAJCASETEJSIE METODY - GET, POST
# DELETE, PUT, PATCH

# GET adresu html dokumentu  200

# POST adresu ... obsahuje tzv. payload

# {'login': 'uzivatel',
#  'password': 'bryndza123'}

con = http.client.HTTPSConnection('www.httpbin.org') # server na testovanie requestov
headers = {'Content-type': 'application/json'}

foo = {'text': 'TOTO JE NAS TEXT'}
json_data = json.dumps(foo)

con.request('POST', '/post', json_data, headers)
res = con.getresponse()

print(res.read().decode())