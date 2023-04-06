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
import socketserver  # adresy IP  a PORTU 65535  - 80 http

# lokalna ip adresa je 127.0.0.1
# webservery Apache, Nginx -


# ping 8.8.8.8 # PINGUJEME adresu googlu aby sme zistili ci sme na internete
# tracert 8.8.8.8  # Sledujeme cestu balickov po internete smerom ku googlu


# DNS - telefonny zoznam internetu

PORT = 8000  # port sme nastavili na 8000 lebo tam pocitac nic nepouziva
Handler = http.server.SimpleHTTPRequestHandler  # handler je nieco ako recepcia, prijima poziadavky od hosti

with socketserver.TCPServer(('', PORT), Handler) as httpd:  # TCP Protokol -
    print('servujem na porte: ', PORT)
    httpd.serve_forever()

'''
TREBA OTVORIT BROWSER a ZADAT ADRESU http://127.0.0.1:8000
'''

# HTML CSS lokalne skripty - Bootstrap ak je lokalne stiahnuty v css
# NEFUNGUJE NA TOM - PHP - DATABAZA - Wordpress

