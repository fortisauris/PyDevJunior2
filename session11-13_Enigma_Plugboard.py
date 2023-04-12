
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
