'''
LIST a DICT COMPREHENSIONS
'''

# KLASIKA
zoznam = list()
for i in range(6):
    if i * 3.14 != 0:
        zoznam.append(i * 3.14)
print(zoznam)

# MODERNE RIESENIE V PYTHONE

zoznam = [i * 3.14 for i in range(6) if i * 3.14 != 0]   # [funkcia, cyklus, podmienka]
print(zoznam)

meno = 'Milan'
slovnik = {x:meno[x] for x in range(len(meno))}
print(slovnik)
print(slovnik.keys())
print(slovnik.values())

# ROZCVICKA  KONVERZIA RIMSKYCH CISLIC NA ARABSKE

def zmen_na_cislo(rimske_cislo: str) -> int:

    vysledok = int()
    if len(rimske_cislo) == 1:
        if rimske_cislo == 'I':
            return 1
        if rimske_cislo == 'V':
            return 5
        if rimske_cislo == 'X':
            return 10

    elif len(rimske_cislo) == 2:
        pass
        # I V X  a kto chce tak MDCL
        # od I do X

    return vysledok

print(zmen_na_cislo('X'))

# TODO Domaca uloha spravit komplet konverziu na z rimskych cisel na arabske


# KRYPTOGRAFIA  BITOVY POSUN - BITWISE

a = bin(65)
print(a)

a = 65 << 3
print(bin(a))
print(a)

a = a >> 9
print(a, bin(a))


msg = 'BRYNDZAOPATZDRAZELA'
enc = []
for pismeno in msg:
    posun = ord(pismeno) << 3
    print(ord(pismeno), posun, bin(posun))
    enc.append(posun)
print(enc)

decr = ''
for pismeno in enc:
    spatny_posun = pismeno >> 3
    print(pismeno, chr(spatny_posun), bin(spatny_posun))
    decr += chr(spatny_posun)

print(decr)

# TODO Domaca uloha spravit posun podobne ako pri Enigme
# string = '00001'
# cyklus kolko treba posunut
# posun string[1:] + string[0]