
# VIGENEROVA SIFRA

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
posunuta_abeceda = lambda abeceda, posun: abeceda[posun:] + abeceda[:posun]
print(posunuta_abeceda(abeceda=abeceda, posun=3))

pripravene_heslo = lambda heslo, dlzka_spravy: (heslo * 100)[:dlzka_spravy]
print(pripravene_heslo(heslo='hesloveslo', dlzka_spravy=15))

# SPRAVA: BRYNDZAZDRAZELA
# ROVNAKO DLHE HESLO: HALUSKAHALUSKAH

def vigenere_enc(sprava: str, heslo: str) -> str:
    """
    :param1  sprava
    :param2 heslo
    :return zasifrovana sprava
    """
    posuny = pripravene_heslo(heslo=heslo, dlzka_spravy=len(sprava))
    print('pripravene na sifrovanie : ', posuny)

    zasifrovana_sprava = "" # str()  prazdny string kde budeme ukladat zasifrovane znaky

    for i in range(0, len(sprava)):
        shift = abeceda.index(posuny[i])
        enc_alphabet = posunuta_abeceda(abeceda=abeceda, posun=shift)
        symbol_hodnota = enc_alphabet[abeceda.index(sprava[i])]
        zasifrovana_sprava += symbol_hodnota

    return zasifrovana_sprava

text = 'BRYNDZAZDRAZELA'
vigenere = vigenere_enc(sprava=text, heslo='HANDBOOK')
print(vigenere)
print(vigenere_enc.__doc__)

# TODO DOmaca uloha skuste spravit funkciu na desifrovanie Vigenerovej sifry...
