import hashlib
import itertools
import functools
import operator

# ROZCVICKA

# PROGRAM KAMEN PAPIER NOZNICE

# nekonecny cyklus

# vyberat z troch moznosti KAMEN PAPIER NOZNICE  pomocou random choice

# ukladat do LISTU, slovnika, suboru.

# TODO TOTO ROBIT NEMUSITE ukladanie vysledku pomaocou FileTools do suboru

# TODO - TOTO ROBIT NEMUSITE funkcia na generovanie nahodnej hodnoty


# JEDNODUCHY LUSKAC HESIEL


def hash_it(text: str):
    h = hashlib.md5()
    data = bytes(text, encoding='utf8')  # ascii
    h.update(data)
    return h.hexdigest()  # hashstring

# BruteForce utok
# Slovnikovy utok -
# SOcialne inzinierstvo

Jozef = ["Kapor", 1986, 'Octavia', 'Slovan', 'Maj', 'COrgon', '12','Chorvatsko', 'Anicka', 'Mirka', 'Saris']

def password_cracker(osoba: list):
    dvojice = itertools.combinations(osoba, 2)
    raw_data = list(dvojice)
    print(raw_data)
    print(len(raw_data))
    result = []
    for cast1, cast2 in raw_data:
        result.append(str(cast1)+str(cast2))  # toto nam spoji obe slova
        result.append(str(cast2) + str(cast1))
        result.append(str(cast1) + '1')
        result.append(str(cast2) + '1')
        result.append(str(cast1).upper() + str(cast2).upper())
        result.append(str(cast1).lower() + str(cast2).lower())
    print(result)
    print(len(result))
    return result



# HLAVNY PROGRAM
vysledok = password_cracker(osoba=Jozef)
for i in vysledok:
    print(i)

# N8vzd7_Sa:Zach0v8VPAM*tI_Stu!kova



# ZAKLADY FUNKCIONALNEHO PROGRAMOVANIA

data = ['A', 'B', 'C', 'D', 'E', 'F']

# proceduralny pristup - tradicny
result = [] # prazdny zoznam
for i in data:
    result.append(i.lower())
print(result)

# funkcionalne programovanie
pismena = list(map(lambda x: x.lower(), data))
print(pismena)

cisla = [3.5,12.65,34.78,11.87]
result = list(map(round, cisla))
print(result)

funkcia = lambda x: round(x/2)
result = list(map(funkcia, cisla))
print(result)

cisla2 = [7.54,7.243,12.87,1.87]
result = list(map(lambda x,y: x/y, cisla, cisla2))
print(result)

viac_ako_tri = list(filter(lambda x: x < 3, result))
print(viac_ako_tri)

mena = ['Gregor', 'Yveta', 'Jozef', 'Frantisek']
obsahuje_pismeno = list(filter(lambda x: 'r' in x, mena))
print(obsahuje_pismeno)

# TODO Domaca uloha spravte si aspon 3 mapy alebo filtre

redukovany_zoznam = list(functools.reduce(lambda x, y: x + y, mena))
print(redukovany_zoznam)

def spojeny_string(string1, string2):
    return string1 + string2

text = ['A', 'H', 'O', 'J']
final_string = functools.reduce(spojeny_string, text)
print(final_string)


nlist = [[1,2,3], [4,5,6], [7,8,9]]
flist = functools.reduce(lambda a,b: a+b, nlist)
print(flist)

# TODO Prestavka do 19:50

a = list(map(operator.add, [1,2,3], [5,6,7]))
print(a)

a = list(map(operator.sub, [1,2,3], [5,6,7]))
print(a)

a = list(map(operator.mul, [1,2,3], [5,6,7]))
print(a)

a,b = 423, 453
res = operator.mul(a, b)
print(res)

a,b = 1423, 453
res = operator.truediv(a, b)
print(res)

a,b = 1423, 453
res = operator.floordiv(a, b)
print(res)

a,b = 12, 34
res = operator.mod(a, b)
print(res)

a,b = 12, 3
res = operator.pow(a, b)
print(res)

# POROVNAVACIE FUNKCIE

a,b = 12, 3
res = operator.lt(a, b)  # Less Than   a < b
print(res)

a,b = 12, 3
res = operator.gt(a, b)  # greater Than   a > b
print(res)

a,b = 12, 12
res = operator.ge(a, b)  # greater or equal    a >= b
print(res)

a, b = 12, 12
res = operator.le(a, b)  # less or equal    a <= b
print(res)

a,b = 12, 12
res = operator.eq(a, b)  # equal    a == b
print(res)

if operator.eq(a, b):   # a == b
    print('ROVNAKE HODNOTY')

a,b = 12, 1
res = operator.ne(a, b)  # non equal    a != b
print(res)

"""
BITWISE OPERACIE - 0b00000000- 0b1111111  - 0x00 do 0xff
"""

a = 255
res = operator.invert(a)  # otocil znamienka
print(res)

res = operator.contains(mena, 'Frantisek')
print(res)

cisla = [5435, 543, 54367, 867, 42, 876, 432, 86]
zoradeny_zoanam = sorted(cisla, reverse=True)
print(zoradeny_zoanam)

text = 'Bryndza zdrazela'
print(sorted(text.lower()))
print(sorted(text.split(' ')))



'''
PASCALOV TROJUHOLNIK
'''
n = 5
for i in range(n):
    print(' ' * (n-1), end='')
    print(' '.join(map(str, str(11**i))))

# XOR   ^
print(1^1)
print(1^0)
# bit 1 alebo 0
# byte 0, 255 - v acsii tabul 65

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def xor_enc(sprava: str, heslo: str) -> str:
    enc_sprava = str()
    prepared_heslo = (100*heslo)[:len(sprava)]
    print(sprava, '\n', prepared_heslo)
    for i in range(0, len(sprava)):
        enc_value = abeceda.index(sprava[i]) ^ abeceda.index(prepared_heslo[i])
        enc_sprava += str(enc_value) + ' '
    return enc_sprava

print(xor_enc(sprava='KONECNEPRISLAJAR', heslo='HOTEL'))

# 13 0 30 0 9 10 10 28 21 3 21 5 19 13 11 22

# TODO Domaca uloha spravit xor_dec

cisla = '12 23 45'
zoznam_cisel = cisla.split(' ')
print(zoznam_cisel)

ciste_cislo = int(zoznam_cisel[0])
print(ciste_cislo)
ciste_cislo2 = eval(zoznam_cisel[0])
print(ciste_cislo2)
print(ciste_cislo+ciste_cislo2)

# print(chr(65))
# print(ord('A'))

# TODO Zamysliet ako kraknut tuto sifru

'''
ZETTELKASTEN  - POZNATKY DO TAKYCH LISTOCKOV 
'''