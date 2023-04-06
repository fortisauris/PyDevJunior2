# ROZCVICKA

# spravime si prazdny dict.
slovnik = dict()

def pridaj_slovicko(slovnik: dict):
    # 1 budeme pridavat klucove slovo
    kluc = input('ZADAJ KLUC')
    # 2hodnotu v podobe string
    if kluc == 'q':
        print('KONIEC')
        quit()
    hodnota = input('ZADAJ STRING')
    # vlozit do slovnika
    slovnik[kluc] = hodnota
    # zavolam slovnik, urcim klucove slovo = hodnota
    print(slovnik)
    # vyprintovat hodnoty -
    return slovnik

# HLAVNY PROGRAM
# while True:
#     slovnik = pridaj_slovicko(slovnik)

# funkciou ALEBO
# nekonecnym cyklom

global val  # zmenili sme ju na globalnu
val = 4534573  # lokalna premenna

def vytlac_hodnotu(n):
    global val
    hodnota =  n + val  # potrebujeme ju dostat sem
    return hodnota

print(vytlac_hodnotu(543))


class Baterka(object):


    def __init__(self):
        self.model = 'Extra Max'
        self.kapacity = 2700 # mah
        self.typ = 'NiMh'
        # self.__znacka = 'VARTA'  # TOTO JE PRIVATNA PREMENNA TRIEDY
        self._znacka = 'VARTA'  # TOTO JE PROTECTED PREMENNA TRIEDY
        print('VZNIKLA BATERKA')

    @property
    def vytlac_kapacitu(self):
        kapacita = self.kapacity + 10
        print(self._znacka)
        return kapacita


obj = Baterka()  # tu vznika objekt # tu sa zrealizuje nas plan
print(obj.model)
print(obj.kapacity)
print(obj.vytlac_kapacitu)
print(obj._znacka)
obj._znacka = "DURACELL"
# print(obj._znacka)

import http.server
import socketserver  # adresy IP  a PORTU 65535  - 80 http

# lokalna ip adresa je 127.0.0.1
# webservery Apache, Nginx -



# ping 8.8.8.8 # IP adresu
# tracert 8.8.8.8

# DNS - telefonny zoznam internetu
'''
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:  # TCP Protokol -
    print('servujem na porte: ', PORT)
    httpd.serve_forever()
    
# HTML CSS lokalne skripty - Bootstrap, W

# HTML - PHP - DATABAZA - Wordpress

'''
'''
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
# TODO Prestavka do 7:52


'''

from http.server import *
import datetime

PORT=8000

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

'''
sort, sorted
SORTOVANIE BBBLE SORT
'''

def bubble_sort(zoznam: list):
    dlzka = len(zoznam)
    for i in range(dlzka):
        uz_zoradene = True  # flag

        for j in range(dlzka - i - 1):
            if zoznam[j] > zoznam[j+1]:
                zoznam[j], zoznam[j+1] = zoznam[j+1], zoznam[j]  # vymenime poradie
                uz_zoradene = False  # zmenime zastavku na False
        if uz_zoradene:  # uz_zoradene is True
            break
    return zoznam # vratime zoradeny zoznam


z = [543,543,6757,65,7865,876,8765,73,67657,68768,6564]
print(bubble_sort(z))



'''
S T A V I A M E    E N I G M U
'''

# mechanicka cast pohyblive rotory a jeden reverzny rotor  3 rotory - 4 rotorove enigmy
# elektricka cast Plugboard - umoznovala kazde pismeno vymenit za ine pismeno

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # ascii kodov
sprava = 'BRYNDZAOPETZDRAZELABRYNDZAOPETZDRAZELA'

# PRVY ROTOR
i = abeceda.index('K') #  pociatocne nastavenie rotoru
print(i)
nastaveny_valec_1 = abeceda[i:] + abeceda[:i]  # posun v tej abecede.
print(nastaveny_valec_1)

# DRUHY ROTOR
i = abeceda.index('S') #  pociatocne nastavenie rotoru
print(i)
nastaveny_valec_2 = abeceda[i:] + abeceda[:i]  # posun v tej abecede.
print(nastaveny_valec_2)

# TRETI ROTOR
i = abeceda.index('F') #  pociatocne nastavenie rotoru
print(i)
nastaveny_valec_3 = abeceda[i:] + abeceda[:i]  # posun v tej abecede.
print(nastaveny_valec_3)

def posun_valca(nvalec: str):  # posun valca po kazdom znaku
    valec = nvalec[1:] + nvalec[0]  # odkrojime vsetky pismena okrem prveho a na koniec pripojime prve pismeno
    print(valec)
    return valec

# hlavny program

zasifrovana_sprava = str()  # definujeme prazdny string
posun_valcov = 0
for i in range(0, len(sprava)):   # prtechadzame spravou
    zasifrovany_znak = nastaveny_valec_1[abeceda.index(sprava[i])]  # vysledok tejto operacie a posunie na druhy valec
    zasifrovany_znak = nastaveny_valec_2[abeceda.index(zasifrovany_znak)]
    zasifrovany_znak = nastaveny_valec_3[abeceda.index(zasifrovany_znak)]
    nastaveny_valec_1 = posun_valca(nastaveny_valec_1)
    if posun_valcov == 26:
        nastaveny_valec_2 = posun_valca(nastaveny_valec_2)
        posun_valcov=0
    zasifrovana_sprava += zasifrovany_znak
    posun_valcov += 1


print(sprava, len(sprava))
print(zasifrovana_sprava)


'''
ZETTELKASTEN  - ukladanie a nacitavanie karticiek do a z jsonu
'''

import random
import json

baza_dat = dict()  # tu sa nam ukladaju data
idecka = set()  # tu riesime duplicitu id cisel
nazvy_karticiek = set()
def generuj_id():
    id = random.randint(0, 10000000)
    povodna_dlzka_ideciek = len(idecka)
    idecka.add(id)
    if povodna_dlzka_ideciek == len(idecka):  # existuje duplicita
        return None
    else:
        id = str(id).zfill(7) #0000656
        return id

def nova_karticka():
    print('ZADAJ NOVU KARTICKU DO SYSTEMU ZETTELKASTEN')
    nazov_karticky = input("NAZOV KARTICKY : ")
    povodna_dlzka_karticiek = len(nazvy_karticiek)
    nazvy_karticiek.add(nazov_karticky)
    if len(nazvy_karticiek) == povodna_dlzka_karticiek:
        print('DUPLICITA V NAZVOCH KARTICIEK !!!')
        # raise ValueError

    # TODO sprav funkciu na kontrolu nazvu karticky  # DUPLICITU VYLUCIT
    id_cislo = None  # defaultna hodnota

    while id_cislo is None:
        id_cislo = generuj_id()
    linky = list()  # prepojenia medzi kartickami
    # TODO linky = zadaj_linky()
    tagy = list()  # mnoziny pomocou tagov
    # TODO tagy = zadaj_tagy()
    obsah_karticky = input('TEXT KARTICKY :')
    baza_dat[id_cislo] = [nazov_karticky, linky, tagy, obsah_karticky]  # tu sa uklada nova karticka do slovnika
    uloz_karticky_do_json()  # ulozi karticky do jsonu

def zadaj_link_alebo_tag():
    pass

def uloz_karticky_do_json():
    with open('index.json', mode='w', encoding='utf8') as file:
        json.dump(baza_dat, file, sort_keys=True, indent=4)
    return

def nacitaj_karticky_z_json():
    vysledok = dict()
    with open('index.json', mode='r', encoding='utf8') as file:
        vysledok = json.load(file)
    return vysledok




# HLAVNY PROGRAM
while True:
    baza_dat = nacitaj_karticky_z_json()
    print(baza_dat)
    nova_karticka()
    print(baza_dat)
    print(idecka)
