# ROZCVICKA - PROGRAM NA SKUSANIE OTAZOK
# TODO nezabudnite nainportovat modul
import random
import time
# DATA - otazky, moznosti a spravne odpovede
# kazda otazka bude mat 3 mnoznosti a, b,  c  # TODO pouzil by som slovnik
otazky = {'akej farby je nebo':['a-zelene', 'b-modre', 'c-zlte', 'b'],
          'co je python': ['a-programovaci jazyk', 'b-jednotka lenivosti', 'c-neviemco', 'a']
          }

# HLAVNY PROGRAM
'''
kluce = list(otazky.keys())
while True:
    otazka = random.choice(kluce)
    print(otazka)
    for i in range(0,3):  # tlaci nam moznosti
        print(otazky[otazka][i])
    odpoved = input('zadaj odpoved abc: ')  # vstup od uzivatela
    # logika
    if odpoved == otazky[otazka][3]:
        print('SPRAVNE')
    else:
        print('NESPRAVNE')
'''

# nekonecny cyklus

# Otazky sa budu vyberat nahodne
# TODO pouzite random.choice()
# odpovedat budeme pomocou prikazu input()

# odpoved spravne alebo nespravne
# TODO jednoducha logika na porovnanie spravnych odpovedi a odpovedi

a = 25464
print(type(a))
print(dir(a))  # vsetky moznosti co s tym mozeme robit
print(abs(a))
print(a.bit_length())   # 0101010110101110101
print(a.to_bytes(2, byteorder='little'))
print(a.__hash__())
print(a.__eq__(25464))

a = 'Hello WOrld'
print(type(a))
print(dir(a))
print(a.capitalize())
print(a.casefold())
print(a.center(24, ' '))
print(a.count('l'))
print(a.encode(encoding='utf8', errors='strict'))
print(a.endswith(('d', 'o'),0,5))
print(a+'\tDObre\t'.expandtabs(tabsize=4))
print(a.find('H', 0, len(a)))


print(type([1,2,3]))
print(dir([1,2,3]))


print('Hello', 'World', 'Ako sa mas ?')

# FORMATOVANIE TEXTU MODERNYM SPOSOBOM

a = 'Toto je udaj {0} vlozeny formatovanim textu {1}'
print(a.format('HODNOTA0', "HODNOTA1"))

print(a.index('udaj', 0, len(a)))

print('alpha154356'.isalnum())
print('alpha154356'.isalpha())
print(a.isascii())
print('agfd154356'.isdecimal())
print('54356'.isdigit())
print('alpha154356'.isidentifier())
print('alpha154356!!'.isalnum())

print('alpha154356'.islower())
print('alpha154356'.isnumeric())
print('alpha154356'.isprintable())  # 255
print('alpha154356'.isspace())

a = 'Hello'
print(a.join(' World'))
print(a.lstrip("H"))
print(a.removeprefix('H'))
print(a.removesuffix('o'))
print(a.swapcase())
print('654'.zfill(8))

vysledok = str()
for i in 'Hello453':
    if i.isalpha():
        vysledok += i
print(vysledok)

# POKROCILE FORMATOVANIE TEXTU

print('Tento %(jazyk)s je uradny jazyk %(obyvatelov)05d na Mauriciu.' % {'jazyk': "francuzsky", 'obyvatelov':5435})


# Collatz Conjecture

def collatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1

collatz(255)

# TODO Prestavka do 19:50


# Modul csv -- Comma separated Variables

a = [12, True, 'Jolana', 564.564]
b = [14, False, 'Jozef', 65.76]

import csv

# zapis do csv suboru
with open('data.csv', mode='w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, dialect='excel', delimiter=' ')
    print(type(datawriter))
    datawriter.writerow(a)
    datawriter.writerow(b)
    print('DONE')

with open('data.csv', mode='r', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=' ')
    print(type(datareader))
    for riadok in datareader:
        print(riadok)
    print('DONE')

# TODO Doplnit DictWriter

import os

# TPM - Trusted Platform Module

print(os.urandom(12))
abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vernam_enc(sprava: str):
    kluc = os.urandom(len(sprava))
    pripraveny_kluc = list()
    enc_sprava = list()
    for i in kluc:  #
        pripraveny_kluc.append(i)
    print(kluc, pripraveny_kluc)
    for i in range(0, len(sprava)):
        enc_znak = abeceda.index(sprava[i]) ^ pripraveny_kluc[i]
        print(enc_znak)
        enc_sprava.append(enc_znak)
    return enc_sprava

print(vernam_enc('BRYNDZAZOPATDRAZELA'))

# TODO spravit Decrypt
# TODO BruteForce Vernam

'''
ZETTELKASTEN
'''

import random

baza_dat = dict()
idecka = set()
def generuj_id():
    id = random.randint(0, 10000000)
    povodna_dlzka_ideciek = len(idecka)
    idecka.add(id)
    if povodna_dlzka_ideciek == len(idecka):
        return None
    else:
        id = str(id).zfill(7)
        return id

def nova_karticka():
    print('ZADAJ NOVU KARTICKU DO SYSTEMU ZETTELKASTEN')
    nazov_karticky = input("NAZOV KARTICKY : ")
    # TODO sprav funkciu na kontrolu nazvu karticky
    id_cislo = None  # defaultna hodnota
    # TODO id cislo nesmie byt None
    while id_cislo is None:
        id_cislo = generuj_id()
    linky = list()
    # TODO linky = zadaj_linky()
    tagy = list()
    # TODO tagy = zadaj_tagy()
    obsah_karticky = input('TEXT KARTICKY :')
    baza_dat[id_cislo] = [id_cislo, linky, tagy, obsah_karticky]  # tu sa uklada nova karticka do slovnika




# HLAVNY PROGRAM
nova_karticka()
print(baza_dat)
print(idecka)
