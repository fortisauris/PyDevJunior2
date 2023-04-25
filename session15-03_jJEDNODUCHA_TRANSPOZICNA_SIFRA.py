'''
TRANSPOZICNA SIFRA
'''

def rozdel_dlzku(seq, dlzka):
    return [seq[i:i + dlzka] for i in range(0, len(seq), dlzka)]  # list comprehension

def zakoduj(kluc, sprava):
    poradie = {
        int(val): num for num, val in enumerate(kluc)
    }
    print(poradie)

    enc_txt = ''
    for index in sorted(poradie.keys()):
        for cast in rozdel_dlzku(sprava, len(kluc)):
            try:
                enc_txt += cast[poradie[index]]

            except IndexError:
                continue

    return enc_txt

print(zakoduj('67895', 'HELLO'))


# TODO Skuste k tomuto napisat testy
