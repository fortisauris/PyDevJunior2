
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

# AES 256  Advanced Encryption System (Rjijandel) - kryptovaci standard
# ChaCha  - Novy algoritmus

