'''
http.server a socket server

Pomocou moduli http.server vytvorime jednoduchy webovy server, ktory spristupni cez browser obsah adresara

socketserver je modul, ktory nam umozni pripojit nas server k socketu pomocou protokolu TCP

TCP - Autorizovany protokol internetu pre pripojenie a nadviazanie komunikacie dvoch pocitacov

Socket sa sklada z IP adresy - v nasom pripade je to 127.0.0.1 --- localhost - lokalna ip adresa PC sameho seba
                    PORTU - jedneho z 65535 sietovych portov

!!!! POZOR - tento server nie je vhodny na pouzitie na Internete - pouzite Apache alebo Nginx s vysokym nastavenim bezpecnosti

'''

import http.server
import socketserver

PORT = 8000

class MojHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.path = 'index.html'  # presmeruje ho na tento subor
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MojHttpRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:  # TCP Protokol -
    print('servujem na porte: ', PORT)
    httpd.serve_forever()

'''
TREBA OTVORIT BROWSER a ZADAT ADRESU http://127.0.0.1:8000

AK VAM SERVER V KONZOLE VYPISUJE 404 - nemate vytvoreny subor index.html
'''