# ROZCVICKA

# PROGRAM NA HOD KOCKOU

import random
import hashlib
import time

print('AHOJ')
# meno = input("NAPIS MENO")  # vysledkom inputu je vzdy print
# print('AHOJ', meno)
# input()

def fibonacci(n):
    if n < 0:
        print('Nespravny vstup')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(0, 3):
    print(fibonacci(i))

# benchmark pocitaca

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def vzorka():
    vysledok = list()
    for _ in range(0, 1000000):
        retazec = str()  # ""
        for znak in range(0,10):
            retazec += random.choice(abeceda)
        vysledok.append(retazec)
    return vysledok

def hash_it(text):
    h = hashlib.md5()
    data = bytes(text, encoding='utf8')
    h.update(data)  # mixer
    return h.hexdigest()

'''
t1 = time.time()
vygenerovane_retazce = vzorka()
for i in vygenerovane_retazce:
    hash_it(i)
t2 = time.time()
print(t1,'\t\t', t2)
print('VYSLEDNY CAS V SEC: ', t2-t1)
'''

# Andrej 3.68 sec  i5-11400H
# Vlado 4.8 sec   i5 - 8300H
# Veronika 2.72 sec  i7
# Peter 2.55 sec  M1 Pro
# Eniko 4.04 sec i5


'''
G E N E R A T O R Y
'''

def vrat_farbu():
    zoznam_farieb = ['cervena', 'oranzova','zelena']
    return zoznam_farieb

def semafor():
    yield 'cervena'
    yield 'oranzova'
    yield 'zelena'

svetla = semafor()
print(svetla)
print(next(svetla))
print(next(svetla))
print(next(svetla))
# print(next(svetla))

svetla = semafor()
print(svetla.__next__())

def generator_zoznamu():
    hodnoty = ['alpha', 'bravo', 'charlie', 'delta']
    yield random.choice(hodnoty)

while True:
    alphacodes = generator_zoznamu()
    print(alphacodes.__next__())
    break

for _ in generator_zoznamu():
    print(_)

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

x = fib(50)
# print(list(x))
for _ in x:
    print(next(x))

for i in fib(10):
    print(i)


# TODO DOmaca uloha spravit vlastny generator

# VIGENEROVA SIFRA

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
posunuta_abeceda = lambda abeceda, posun: abeceda[posun:] + abeceda[:posun]
print(posunuta_abeceda(abeceda=abeceda, posun=3))

pripravene_heslo = lambda heslo, dlzka_spravy: (heslo * 100)[:dlzka_spravy]
print(pripravene_heslo(heslo='hesloveslo', dlzka_spravy=15))

# SPRAVA: BRYNDZAZDRAZELA
# ROVNAKO DLHE HESLO: HALUSKAHALUSKAH

def vigenere_enc(sprava: str, heslo: str) -> str:
    """
    :param1  sprava
    :param2 heslo
    :return zasifrovana sprava
    """
    posuny = pripravene_heslo(heslo=heslo, dlzka_spravy=len(sprava))
    print('pripravene na sifrovanie : ', posuny)

    zasifrovana_sprava = "" # str()  prazdny string kde budeme ukladat zasifrovane znaky

    for i in range(0, len(sprava)):
        shift = abeceda.index(posuny[i])
        enc_alphabet = posunuta_abeceda(abeceda=abeceda, posun=shift)
        symbol_hodnota = enc_alphabet[abeceda.index(sprava[i])]
        zasifrovana_sprava += symbol_hodnota

    return zasifrovana_sprava

text = 'BRYNDZAZDRAZELA'
vigenere = vigenere_enc(sprava=text, heslo='HANDBOOK')
print(vigenere)
print(vigenere_enc.__doc__)

# TODO DOmaca uloha skuste spravit funkciu na desifrovanie Vigenerovej sifry...

# TODO Prestavka do 19:50

import itertools

a = iter('ABCD')  # vstavany prikaz pythonu
print(a)
print(list(a))

zipsujeme = zip([1,2,3], ['Martin', 'Vlado', 'Jozef'])
print(zipsujeme)
print(list(zipsujeme))

zipsujeme = zip([1,2,3], ['Pomaranc', 'Mandarinka', 'Pomelo', 'Limetka'])
print(zipsujeme)
print(list(zipsujeme))

zipsujeme = itertools.zip_longest([1,2,3], ['Pomaranc', 'Mandarinka', 'Pomelo', 'Limetka'], fillvalue=0)
print(zipsujeme)
print(list(zipsujeme))

bankovky = [10,50,5,100,20]
print(list(itertools.combinations(bankovky,4)))
print(list(itertools.combinations_with_replacement(bankovky,4)))

a = 'ABC'
print(list(itertools.permutations(a)))

counter = itertools.count()
while True:
    c = counter.__next__()
    print(c)
    time.sleep(.5)
    if c == 6:
        break

c = itertools.count(start=.2, step=-.3)
print(list(next(c) for _ in range(5)))  # pythonisticky sposob ako vypisat 5 hodnot z pocitadla

opakovanie = itertools.repeat(True, 10)
print(list(opakovanie))

opakuj_cyklus = itertools.cycle('ABCDEF')
print(opakuj_cyklus)
for i in range(10):
    print(next(opakuj_cyklus))

a = [1,2,3,4,5]
print(list(itertools.accumulate(a)))
print(list(itertools.accumulate(a, lambda x, y: (x+y)*2)))

a = itertools.product([1,2],["A","B"], [True, False])
print(a)
print(list(a))

a, b = 1, 2
iterator1, iterator2, iterator3 =  itertools.tee('ABCDEF', 3)
print(list(iterator1))
print(list(iterator2))
print(list(iterator3))


'''
JEDNODUCHY PROGRAM LIGA
'''

teams = ['Liverpool', 'FC Barcelona', 'Manchester United', 'AJAX Amsterdam']
zapasy = itertools.combinations(teams, 2)
# print(list(zapasy))

liga = dict()  # slovnik
for i in zapasy:
    zapas = next(zapasy)
    print(zapasy, zapas)
    key = zapas[0] + ':' + zapas[1]
    print(key)
    liga[key] = [0,0]

print(liga)

# TODO Vyhladat chybu v programe

def je_cislo_parne(n: int) -> bool:
    if n/2 == int(n/2):
        return True
    else:
        return False


for i in range(50):
    print(i, je_cislo_parne(i))
