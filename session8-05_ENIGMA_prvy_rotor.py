'''
S T A V I A M E    E N I G M U
'''

# mechanicka cast pohyblive rotory a jeden reverzny rotor
# elektricka cast Plugboard - umoznovala kazde pismeno vymenit za ine pismeno

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sprava = 'BRYNDZAOPETZDRAZELA'

i = abeceda.index('K')
print(i)
nastaveny_valec = abeceda[i:] + abeceda[:i]
print(nastaveny_valec)

def posun_valca(nvalec: str):
    valec = nvalec[1:] + nvalec[0]
    print(valec)
    return valec

# hlavny program

zasifrovana_sprava = str()
for i in range(0, len(sprava)):
    zasifrovany_znak = nastaveny_valec[abeceda.index(sprava[i])]
    zasifrovana_sprava += zasifrovany_znak
    nastaveny_valec = posun_valca(nastaveny_valec)
print(sprava)
print(zasifrovana_sprava)
