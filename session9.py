# Mazacka suborov

# kazdy disk MBR - zoznam ulozenych suborov

# delete subor -- vyskrtne ho zo zozanmu... jeho obsah zostava na disku.
'''
# pouzijeme open na otvorenie suboru mode='r'
with open('skuska.txt', mode='r', encoding='utf8') as f:
    text = f.read()

# potrebujeme zistit dlzku textu - len(text)
print(text, len(text))
# vygenerujeme si rovnako dlhy string zloczeny z 1tiek
mazaci_text = str()
for i in range(len(text)):
    mazaci_text += '1'
print(mazaci_text, len(text))
# 5x za sebou zapisat do suboru
for i in range(5):
    with open('skuska.txt', mode='w', encoding='ascii') as f:
        f.write(mazaci_text)
        print(i, 'PREMAZAL SOM TEXT')

print('DONE')
'''

'''
MODUL DATETIME
'''
import datetime
import zoneinfo
# import tzdata



d1 = datetime.date(year=2023, month=1, day=1)
print(d1)
print(type(d1))
print(dir(d1))
print(d1.year)
print(d1.timetuple())
print(d1.toordinal())
print(d1.weekday())  # anglicka
print(d1.isoweekday())  # nase
print(d1.isocalendar())
print(d1.isoformat())
print(d1.ctime())

d2 = datetime.date(year=1989, month=11, day=17)
print(d2.toordinal())
print(d2.ctime())
print(d2.strftime("%A %d.%B %Y %z"))

d_final = d1-d2
print(type(d_final))  # timedelta - objekt v ktorom uchovavame casovy usek.
print(d_final)

t1 = datetime.time(11,2,30,0)
print(type(t1))
print(t1)

#zone = zoneinfo.ZoneInfo('')
# zone = zoneinfo.ZoneInfo('Europe/Bratislava')
cet = datetime.timedelta(hours=1)  # Central European Time
tz = datetime.timezone(offset=cet)
dt = datetime.datetime(year=2023, month=4, day=3, hour=18, minute=31, second=15, microsecond=0, tzinfo=tz)
print(dt)

dt2 = datetime.datetime(year=2022, month=3, day=1, hour=12, minute=31, second=15, microsecond=0, tzinfo=tz)
print(dt2)

d_final = dt-dt2
print(d_final)
print(type(d_final))
print(d_final.total_seconds())

print(zoneinfo.available_timezones())


dn = datetime.datetime.now()
print(dn)

zajtra = datetime.datetime.now() + datetime.timedelta(hours=24)
print(zajtra)

# TODO vytvorte dva datetime.datetime objekty a potom ich zratajte alebo odratajte

dt = datetime.timedelta(hours=1) + datetime.timedelta(minutes=60)
print(dt)


'''
ADVANCED DICTIONARY - SLOVNIK
'''


a = dict()
a = dict(one=1, two=2, three=3)
print(a)

b = {'one':1,
     'two':2,
     'three':3
     }

print(b)
print(type(b['one']))

c = dict(zip(['one', 'two', 'three'], [1,2,3]))
print(c)
print(list(c))
print(len(c))

print(c['one'])


c['Srobovak'] = None
print(c['Srobovak'])
c['four'] = 4
print(c)

del c['four']
print(c)

print('one' in c)
print('Srobovak' not in c)

a = iter(c)
for i in range(0, len(c)):
    key = next(a)
    print(i, key, c[key])


c.clear()
print(c)

c = b.copy()  # plytka kopia
print(c)
vystup = c.fromkeys(c.keys())
print(vystup)

print(c['one'])
print(c.get('one'))
print(c)

print(c.keys())
print(c.values())
print(c.items())

for i in c.items():
    print(i[0], i[1])

c.pop('one')
print(c)

val = c.popitem()
print(val, '\t', c)
val = c.popitem()
print(val, '\t', c)

c = b
print(c)
c_it = reversed(c)  # otoceny iterator
# print(c_it)
print(next(c_it))
print(c_it.__next__())
print(c_it.__next__())
# print(c_it.__next__())  # vyhodi chybu stop iteration

c.update(b)
print(c)


# dictview objects
print(len(c.items()))

# TODO Prestavka do 19:50

a = iter(c.keys())
for i in range(0, len(c.keys())):
    print(next(a))

print('one' in c.keys())
print(False in c.values())  # TODO preskumame preco to tak robi
print(c)

a = reversed(c.items())
print(next(a))

# nastavenia
# TODO Otvaranie kurnika
# while True:
#     print(str(datetime.datetime.now()))

# Arduino
# Micropython

print(next(a))
print(next(a))

'''
Premena decimalneho cisla na binarne
'''
print(bin(64))
print(hex(64))

def dec2bin(n: int):
    vysledok = str()
    if n == 0:
        return 0
    while n:
        vysledok += str(n&1)
        n = n >> 1
        print(n, vysledok)
    vysledok = vysledok[::-1]
    return vysledok

print(dec2bin(6))
print(bin(6))
print(hex(60))
print(oct(60))

for i in range(0, 255):
    print(i, chr(i))

for i in 'AHOJ':
    print(i, ord(i))


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


def posun_valca(nvalec: str):  # posun valca po kazdom znaku
    valec = nvalec[1:] + nvalec[0]  # odkrojime vsetky pismena okrem prveho a na koniec pripojime prve pismeno
    print(valec)
    return valec

# hlavny program

zasifrovana_sprava = str()  # definujeme prazdny string
posun_valcov = 0
for i in range(0, len(sprava)):   # prtechadzame spravou
    if posun_valcov <= 26:
        zasifrovany_znak = nastaveny_valec_1[abeceda.index(sprava[i])]
        nastaveny_valec_1 = posun_valca(nastaveny_valec_1)
    if posun_valcov > 26 and posun_valcov < 52:
        zasifrovany_znak = nastaveny_valec_2[abeceda.index(sprava[i])]
        nastaveny_valec_2 = posun_valca(nastaveny_valec_2)

    # TODO DOmaca uloha zamysliet sa ako to spravit na dlhsej sprave ako 52 znakov
    zasifrovana_sprava += zasifrovany_znak
    posun_valcov += 1
print(sprava, len(sprava))
print(zasifrovana_sprava)

# LCKA ROQF HXNU ZOYY EMC

# AES 256  Advanced Encryption System
# ChaCha


'''
ZETTELKASTEN
'''

import random
import json

baza_dat = dict()  # tu sa nam ukladaju data
idecka = set()  # tu riesime duplicitu id cisel
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
baza_dat = nacitaj_karticky_z_json()
print(baza_dat)
nova_karticka()
print(baza_dat)
print(idecka)
