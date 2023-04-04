'''
S T A V I A M E    E N I G M U
'''

# mechanicka cast pohyblive rotory a jeden reverzny rotor  3 rotory - 4 rotorove enigmy
# elektricka cast Plugboard - umoznovala kazde pismeno vymenit za ine pismeno

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # ascii kodov
sprava = 'BRYNDZAOPETZDRAZELA'

i = abeceda.index('K') #  pociatocne nastavenie rotoru
print(i)
nastaveny_valec = abeceda[i:] + abeceda[:i]  # posun v tej abecede.
print(nastaveny_valec)

def posun_valca(nvalec: str):  # posun valca po kazdom znaku
    valec = nvalec[1:] + nvalec[0]  # odkrojime vsetky pismena okrem prveho a na koniec pripojime prve pismeno
    print(valec)
    return valec

# hlavny program

zasifrovana_sprava = str()  # definujeme prazdny string
for i in range(0, len(sprava)):   # prtechadzame spravou
    zasifrovany_znak = nastaveny_valec[abeceda.index(sprava[i])]
    zasifrovana_sprava += zasifrovany_znak
    nastaveny_valec = posun_valca(nastaveny_valec)
print(sprava)
print(zasifrovana_sprava)

# LCKA ROQF HXNU ZOYY EMC