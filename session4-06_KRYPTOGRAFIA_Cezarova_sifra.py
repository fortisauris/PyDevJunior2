abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def posunuta_abeceda(posun: int):
    """
    Funkcia upravi abecedu pomocou jednoducheho posunu pismen o urcenu hodnotu
    :param posun:: integer
    return:: posunuta_abeceda
    """
    return abeceda[posun:] + abeceda[:posun]

def cezar_enc(text: str, posun: int):
    posunuta = posunuta_abeceda(posun)
    enc_text = str()  # '' definujeme prazdny textovy retazec
    for i in text:  # prechadzame textom na zasifrovanie
        if i == ' ':   # ked je znak medzera tak pridaj do enc tectu medzeru
            enc_text += " "
        else:  # vo vsetkych inych pripadoch
            symbol_pozicia = int(abeceda.index(i))  # hladame poziciu pismena v normalnej abecede
            enc_text += posunuta[symbol_pozicia]  # pridavame do enc_test pismeno z posunutej abecedy
    return enc_text.upper()  # vracia zasifrovany text

print(cezar_enc("AHOJTE VSETCI A PRAJEM VAM VELA USPECHOV V PROGRAMOVANI", 4))

# ELSNXI ZWIXGM E TVENIQ ZEQ ZIPE YWTIGLSZ Z TVSKVEQSZERM

# TODO Spravit program na desifrovanie tejto sifry
