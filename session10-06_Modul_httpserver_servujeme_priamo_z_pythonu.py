'''
http.server a socket server

Pomocou moduli http.server vytvorime jednoduchy webovy server, ktory spristupni cez browser obsah adresara

socketserver je modul, ktory nam umozni pripojit nas server k socketu pomocou protokolu TCP

TCP - Autorizovany protokol internetu pre pripojenie a nadviazanie komunikacie dvoch pocitacov

Socket sa sklada z IP adresy - v nasom pripade je to 127.0.0.1 --- localhost - lokalna ip adresa PC sameho seba
                    PORTU - jedneho z 65535 sietovych portov

!!!! POZOR - tento server nie je vhodny na pouzitie na Internete - pouzite Apache alebo Nginx s vysokym nastavenim bezpecnosti

'''

from http.server import *
import datetime

PORT = 8000

class NasServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)  # Uspech
        self.send_header("content-type", "text/html")
        self.end_headers()

        datum = '<h1>' + str(datetime.datetime.now()) + '</h1>'

        self.wfile.write('<h1> TOTO JE NAS PERFEKTNY SERVER </h1>'.encode())
        self.wfile.write('<p> Toto je nas text na nasu webovu stranku </p>'.encode())
        self.wfile.write(datum.encode())


server = HTTPServer(('', 8000), NasServer)
server.serve_forever()


'''
Servuje priamo z kodu aj premennu datum. TCP robi automaticky a nepotrebujeme ho kodit cez socketserver
'''
