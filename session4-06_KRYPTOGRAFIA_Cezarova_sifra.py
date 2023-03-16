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
    enc_text = str()  # ''
    for i in text:
        if i == ' ':
            enc_text += " "
        else:
            symbol_pozicia = int(abeceda.index(i))
            enc_text += posunuta[symbol_pozicia]
    return enc_text.upper()

print(cezar_enc("AHOJTE VSETCI A PRAJEM VAM VELA USPECHOV V PROGRAMOVANI", 4))

# ELSNXI ZWIXGM E TVENIQ ZEQ ZIPE YWTIGLSZ Z TVSKVEQSZERM

# TODO Spravit program na desifrovanie tejto sifry
