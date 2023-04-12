import http.client
import json

'''
JEDNODUCHY KLIENT
'''
'''
con = http.client.HTTPSConnection('fortisauris.com')  # rozdiel medzi HTTP - HTTPS  -

# zaregistovat tatrabanka.sk   CA
# zaregistorvat ta.trabanka.sk  CA  https

con.request('GET', '/')
r1 = con.getresponse()
headers = r1.getheaders()
print(r1.status, r1.reason)
print('HEADERS:\n', headers)

obsah = r1.read()
print(obsah)


BODY = '*** CONTENT ***'
con = http.client.HTTPSConnection('localhost', 8000)
con.request('PUT', '/file', BODY)
response = con.getresponse()
print(type(response))
print(response.status, response.reason)
'''
# GET, POST
# DELETE, PUT, PATCH

# GET adresu html dokumentu  200

# POST adresu ...

# {'login': 'uzivatel',
#  'password': 'bryndza123'}
'''
con = http.client.HTTPSConnection('www.httpbin.org') # server na testovanie requestov
headers = {'Content-type': 'application/json'}

foo = {'text': 'TOTO JE NAS TEXT'}
json_data = json.dumps(foo)

con.request('POST', '/post', json_data, headers)
res = con.getresponse()
print(res.read().decode())
'''

'''
DEKORATORY A FUNKCIE VYSSIEHO RADU

@staticmethod  - 




'''


class Nastroje(object):

    def __init__(self):
        print('VZNIKLA TRIEDA NASTROJE')
        self.premenna = 2

    @property
    def krat_dva(self):
        return self.premenna * 2

    @staticmethod
    def vypocet(x, y):
        return x * y * 5463



obj = Nastroje()
print(obj.premenna)
# print(obj.krat_dva())   # volame metodu triedy Nastroje
print(obj.krat_dva)

print(obj.vypocet(5435,6546))
print(Nastroje.vypocet(453,76548))

'''
def hello(func):

    def wrapper():  # toto jhe vnutorna funkcia
        print('UROB VOLACO PRED VLOZENO FUNKCIOU')  # skontroloval nieco
        func()
        print('UROB VOLACO PO VYKONANI FUNKCIE')  # poupratoval po sebe

    return wrapper

@hello
def nasa_funkcia():
    print('UROB VOLACO')

nasa_funkcia()
'''
'''
FUNKCIA DEKORATORA S PARAMETRAMI (*args, **kwargs)
'''

def hello(func):

    def wrapper(*args, **kwargs):
        print('START PROGRAMU - KOD KTORY SKONTROLUJE CI MENO NIE JE V ZOZNAME VULGARIZMOV')  # skontroloval nieco
        result = func(*args, **kwargs)
        print('POZDRAV BOL USPESNE DOKONCENY')  # poupratoval po sebe
        return result

    return wrapper

@hello
def pozdrav(meno: str, pocet: int):
    for i in range(0,pocet):
        print('AHOJ', meno)

pozdrav('Vlado', 5)


'''
Dekorator salba - bude sa nas snzait presvedcit ze 2 a 2 nie su 4
'''
def salba(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 1

    return wrapper
@hello
@salba
def spocitaj(x,y):
    return x+y

print(spocitaj(2,2))


def decor1(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper

def decor2(func):
    def wrapper():
        x = func()
        return x * 2
    return wrapper

@decor1
@decor2
def cislo():
    return 10

print(cislo())


USER = 'admin'

def admin(func):

    def wrapper(*args, **kwargs):
        if USER == 'admin':
            func(*args, **kwargs)
            print('NASTAVENIA BOLI ULOZENE')
            return True
        else:
            print('UZIVATEL ', USER, ' NEMA OPRAVNENIE UKLADAT ZMENY')
            return False

    return wrapper
@admin
def ulozenie_nastevenia_servera():
    print('KONFIGURACIA SERVERA BOLA ULOZENA')

ulozenie_nastevenia_servera()

# TODO Spravit jednoduchy dekorator


'''
PALINDROM Slovo, ktore je rovnake odporedu aj odzadu
'''

def palindrome(slovo: str) -> bool:
    for i in range(len(slovo)):
        t = slovo[:i] + slovo[i+1:]
        if t == t[::-1]:
            return True
    return False

s = 'KOROK'
print(palindrome(slovo=s))

# PROGRAM NA DEBUGGOVANIE

def sucet(a,b):
    try:
        result = a + b
    except TypeError:
        result = int(a) + int(b)
    finally:
        return result

def urob_delenie(a,b):
    if b == 0:
        b = 1
    return a / b

def je_cele_cislo(n):
    if n is None or str(n).isalpha():
        return False

    if n == int(n):
        return True
    else:
        return False


print(sucet(5,0))
print(urob_delenie(5,0))
'''
for i in range(25):
    # if i == 20:
        # raise ValueError
    print(i)
'''
# TODO Prestavka do 19:50

# Unittest -
# pytest

'''
def test_urob_sucet():
    assert sucet(2, 2) == 4
    assert sucet('AHOJ ', "SVET") == 'AHOJ SVET'
    assert sucet('54354', 564356) == 618710

def test_urob_delenie():
    assert urob_delenie(100,2) == 50
    assert urob_delenie(100,0) == 100

def test_je_cele_cislo():
    assert je_cele_cislo(50) is True
    assert je_cele_cislo(10.5) == False
    assert je_cele_cislo(-10.5) == False
    assert je_cele_cislo(None) == False
    assert je_cele_cislo('AHOJ') == False

'''

# ENIGMA PLUGBOARD

def plugboard(mods: dict, key):
    key = key.upper()
    abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    defaultne_nastavenie = dict(zip(abeceda, abeceda))
    print(defaultne_nastavenie)

    defaultne_nastavenie.update(mods)
    print(defaultne_nastavenie)
    return defaultne_nastavenie[key]

upravene = {
    'B':'X',
    'D':'K',
    'X':'B',
    'K':'D'
}

text = input('ZADAJ TEXT')
vysledok = str()
for pismeno in text:
    zasifrovane_pismeno = plugboard(upravene, pismeno)
    print(zasifrovane_pismeno)
    vysledok += zasifrovane_pismeno

print(vysledok)


