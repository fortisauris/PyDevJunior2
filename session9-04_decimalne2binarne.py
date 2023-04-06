
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

print(dec2bin(6))  # vysledok je 110 v binarnom kode
print(bin(6))
print(hex(60))
print(oct(60))

for i in range(0, 255):  # chr
    print(i, chr(i))

for i in 'AHOJ':
    print(i, ord(i))  # ord

