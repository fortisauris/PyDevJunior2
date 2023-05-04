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