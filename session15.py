# ROZCVICKY - ODPOCET DATUMU A CASU DO NAJBLIZSIEHO SPLNU MESIACA


import datetime

# terajsi datum a cas => datetime.datetime.now()
teraz = datetime.datetime.now()

# termin najblizsieho splnu   5.5.2023 19:34  #
spln = datetime.datetime(year=2023, month=5, day=5, hour=19, minute=34)

# datetime.timedelta() # zobrazovat na obrazovke  # CASOVY USEK
cas_do_splnu = spln - teraz
# odpocet sa nam zobrazi ako timedelta object
print(cas_do_splnu)


# ADVANCED... vypocitat dalsi spln ... 29.5 dna od posledneho splnu
'''
while True:
    try:
        print('VOLACO')
    except KeyboardInterrupt:
        cmd = input('ZADAJ PRIKAZ PROGRAMU :')
        if cmd == 'q':
            quit()
    finally:
        pass

'''

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

import hmac

def vypocitaj_hash_bloku(hashstring_predchadzajuceho_bloku: str, data: dict):

    key = bytes(hashstring_predchadzajuceho_bloku, encoding='utf8')
    msg = bytes(str(data), encoding='utf8')
    h = hmac.new(key=key, msg=msg, digestmod='md5')
    result = h.hexdigest()
    print(result)
    return result



databaza = []


# toto je zaciatok nasej retaze
seed = '843b614237935cfbbc9c1a2386e69724'

# toto je prvy vypocitany block naseho blokchainu
prva_transakcia = {'ucet1': 5643765, 'ucet2': 6574654, 'suma': 43}
hashstring = vypocitaj_hash_bloku(hashstring_predchadzajuceho_bloku=seed, data=prva_transakcia)

# toto je druhy blok naseho blockchainu
druha_transakcia = {'ucet1': 674576565, 'ucet2': 6574654, 'suma': 16.10}
hashstring = vypocitaj_hash_bloku(hashstring_predchadzajuceho_bloku=hashstring, data=druha_transakcia)

# toto je druhy blok naseho blockchainu
tretia_transakcia = {'ucet1': 4582358943, 'ucet2': 6574654, 'suma': 128}
hashstring = vypocitaj_hash_bloku(hashstring_predchadzajuceho_bloku=hashstring, data=tretia_transakcia)