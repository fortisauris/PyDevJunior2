
'''
KOMPLETNA ENIGMA

'''

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

# TRETI ROTOR
i = abeceda.index('F') #  pociatocne nastavenie rotoru
print(i)
nastaveny_valec_3 = abeceda[i:] + abeceda[:i]  # posun v tej abecede.
print(nastaveny_valec_3)

# NASTAVENIE PLUGBOARDU

upravene = {
    'B':'X',
    'D':'K',
    'X':'B',
    'K':'D',
    'H':'Y',
    'Y':'H'
}

def posun_valca(nvalec: str):  # posun valca po kazdom znaku
    valec = nvalec[1:] + nvalec[0]  # odkrojime vsetky pismena okrem prveho a na koniec pripojime prve pismeno
    print(valec)
    return valec


def plugboard(mods: dict, key):
    key = key.upper()
    abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    defaultne_nastavenie = dict(zip(abeceda, abeceda))
    print(defaultne_nastavenie)

    defaultne_nastavenie.update(mods)   # pridavame modifikacie do defaultnej abecedy
    print(defaultne_nastavenie)
    return defaultne_nastavenie[key]


# hlavny program

zasifrovana_sprava = str()  # definujeme prazdny string
posun_valcov = 0
for i in range(0, len(sprava)):   # prtechadzame spravou
    zasifrovany_znak = plugboard(upravene, sprava[i])
    zasifrovany_znak = nastaveny_valec_1[abeceda.index(zasifrovany_znak)]  # vysledok tejto operacie a posunie na druhy valec
    zasifrovany_znak = nastaveny_valec_2[abeceda.index(zasifrovany_znak)]
    zasifrovany_znak = nastaveny_valec_3[abeceda.index(zasifrovany_znak)]
    nastaveny_valec_1 = posun_valca(nastaveny_valec_1)
    if posun_valcov == 26:
        nastaveny_valec_2 = posun_valca(nastaveny_valec_2)
        posun_valcov=0
    # zasifrovany_znak = plugboard(upravene, zasifrovany_znak)
    zasifrovana_sprava += zasifrovany_znak
    posun_valcov += 1


print(sprava, len(sprava))
print(zasifrovana_sprava)
# IZHXOLNCEUKRWLVVBJZBSAQHEGVYOELQFPPVDT  -> bez plugboardu
# IZYBOLNCEUDRWLVVXJZXSAQYEGVHOELQFPPVKT  -> plugboard za rotormi
# EZQXVLNCEUKRDLVVBJZXSJQOEGVYOELXFPPVDT  -> plugboard pred rotormi
