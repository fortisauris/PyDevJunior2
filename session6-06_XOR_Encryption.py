
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
