# ROZCVICKA

import random

# Texas je male male mestecko Prague -
# 150 obyvatelov
# priblizne 45% obyvatelov bude volit Republikanov
# 47% bude volit Demokratov
# 8% este su nerozhodni
# obcania = dict()
# Slovnik v ktorom bude 150 klucov a str(21)
# republikani budu 45%
# demokrati 47%
# tych nerozhodnych rozhodneme pomocou random.choice(['Demokrati','Republikani'])

# Spocitame hlasy v slovniku


import urllib.request
import time
import socket

def ping_url(host):
    t1 = time.time()
    urllib.request.urlopen(host+'/index.html').read()
    print(t1,'\t', time.time())
    return ((time.time()-t1)*1000.0)

print(ping_url('https://fortisauris.com'))


def portscanner(ip4):
    vlajka = False
    porty_na_skenovanie = [21, 22, 80, 447, 8000]  # FTP-Nesifrovane, SSH-sifrovane, HTTP, HTTPS
    for port in porty_na_skenovanie:
        obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = obj.connect_ex((ip4, port))
        if result == 0:
            print('ADRESA :', ip4, 'PORT :', port, ' JE AKTIVNY')
            vlajka = True
        else:
            pass
        obj.close()
    return True

# portscanner('188.121.170.77')


'''
STREAMOVACIA SIFRA ZALOZENA NA SBOXE
'''

def sbox_enc(sbox, key):
    # pismena v premennej abeceda 26 znakov
    key = ord(key)
    #print(key)
    enc_znak = int()
    for i in sbox:
        key ^= i
        #print(i, key)
    return key


# TODO Prestavka do 19:50

msg = 'BRYNDZA ZDRAZELA'
sbox = [23,56,89,235,127,90,87,55]

enc_msg = []  # list()
for key in msg:
    enc_key = sbox_enc(sbox, key)
    #print(enc_key)
    enc_msg.append(enc_key)

print(enc_msg)

# TODO SBOX OPACNY -- DESIFROVANIE - funkcia na otacanie SBOXU

'''
ALGORITMUS NAJKRATSIA CESTA
'''

graph = dict()
graph['BA'] = ['TT']
graph['TT'] = ['BA', 'NR', 'PN']
graph['NR'] = ['TT','BB']
graph['PN'] = ['TT', 'TN']
graph['BB'] = ['KE', 'NR']
graph['TN'] = ['ZA', 'PN']
graph['KE'] = ['BB', 'PP']
graph['ZA'] = ['PP', 'TN']
graph['PP'] = ['KE', 'ZA']

def najkratsia_cesta(graph: dict, mesto1: str, mesto2: str):
    cesta_zoznam = [[mesto1]]
    cesta_index = 0

    predchadzajuce_mesto = {mesto1}
    if mesto1 == mesto2:
        return cesta_zoznam[0]

    while cesta_index < len(cesta_zoznam):
        aktualna_cesta = cesta_zoznam[cesta_index]
        posledne_mesto = aktualna_cesta[-1]
        dalsie_mesta = graph[posledne_mesto]

        if mesto2 in dalsie_mesta:
            aktualna_cesta.append(mesto2)
            return aktualna_cesta

        for dalsie_mesto in dalsie_mesta:
            if not dalsie_mesto in predchadzajuce_mesto:
                nova_cesta = aktualna_cesta[:]
                nova_cesta.append(dalsie_mesto)
                cesta_zoznam.append((nova_cesta))

                predchadzajuce_mesto.add(dalsie_mesto)
        cesta_index += 1
    return []

print(najkratsia_cesta(graph, 'BA', 'KE'))
print(najkratsia_cesta(graph, 'BA', 'NR'))


'''
KOMPLETNA ENIGMA

'''

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

# NASTAVENIE PLUGBOARDU

upravene = {
    'B':'X',
    'D':'K',
    'X':'B',
    'K':'D',
    'H':'Y',
    'Y':'H'
}

def posun_valca(nvalec: str):  # posun valca po kazdom znaku
    valec = nvalec[1:] + nvalec[0]  # odkrojime vsetky pismena okrem prveho a na koniec pripojime prve pismeno
    print(valec)
    return valec


def plugboard(mods: dict, key):
    key = key.upper()
    abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    defaultne_nastavenie = dict(zip(abeceda, abeceda))
    print(defaultne_nastavenie)

    defaultne_nastavenie.update(mods)   # pridavame modifikacie do defaultnej abecedy
    print(defaultne_nastavenie)
    return defaultne_nastavenie[key]


# hlavny program

zasifrovana_sprava = str()  # definujeme prazdny string
posun_valcov = 0
for i in range(0, len(sprava)):   # prtechadzame spravou
    zasifrovany_znak = plugboard(upravene, sprava[i])
    zasifrovany_znak = nastaveny_valec_1[abeceda.index(zasifrovany_znak)]  # vysledok tejto operacie a posunie na druhy valec
    zasifrovany_znak = nastaveny_valec_2[abeceda.index(zasifrovany_znak)]
    zasifrovany_znak = nastaveny_valec_3[abeceda.index(zasifrovany_znak)]
    nastaveny_valec_1 = posun_valca(nastaveny_valec_1)
    if posun_valcov == 26:
        nastaveny_valec_2 = posun_valca(nastaveny_valec_2)
        posun_valcov=0
    # zasifrovany_znak = plugboard(upravene, zasifrovany_znak)
    zasifrovana_sprava += zasifrovany_znak
    posun_valcov += 1


print(sprava, len(sprava))
print(zasifrovana_sprava)
# IZHXOLNCEUKRWLVVBJZBSAQHEGVYOELQFPPVDT
# IZYBOLNCEUDRWLVVXJZXSAQYEGVHOELQFPPVKT  -> plugboard za rotormi
# EZQXVLNCEUKRDLVVBJZXSJQOEGVYOELXFPPVDT  -> plugboard pred rotormi

'''
PRIPOJENIE NA POCITAC POMOCOU MODULU SOCKET
'''

# netcat -

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

