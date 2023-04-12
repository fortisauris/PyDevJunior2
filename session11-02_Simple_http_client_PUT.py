'''

JEDNODUCHY HTTP CLIENT METODA PUT
'''

import http.client

BODY = '*** CONTENT ***'
con = http.client.HTTPSConnection('localhost', 8000)
con.request('PUT', '/file', BODY)
response = con.getresponse()
print(type(response))
print(response.status, response.reason)
