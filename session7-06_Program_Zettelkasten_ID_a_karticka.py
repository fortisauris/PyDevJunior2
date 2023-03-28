
'''
ZETTELKASTEN
'''

import random

baza_dat = dict()
idecka = set()
def generuj_id():
    id = random.randint(0, 10000000)
    povodna_dlzka_ideciek = len(idecka)
    idecka.add(id)
    if povodna_dlzka_ideciek == len(idecka):
        return None
    else:
        id = str(id).zfill(7)
        return id

def nova_karticka():
    print('ZADAJ NOVU KARTICKU DO SYSTEMU ZETTELKASTEN')
    nazov_karticky = input("NAZOV KARTICKY : ")
    # TODO sprav funkciu na kontrolu nazvu karticky
    id_cislo = None  # defaultna hodnota
    # TODO id cislo nesmie byt None
    while id_cislo is None:
        id_cislo = generuj_id()
    linky = list()
    # TODO linky = zadaj_linky()
    tagy = list()
    # TODO tagy = zadaj_tagy()
    obsah_karticky = input('TEXT KARTICKY :')
    baza_dat[id_cislo] = [id_cislo, linky, tagy, obsah_karticky]  # tu sa uklada nova karticka do slovnika




# HLAVNY PROGRAM
nova_karticka()
print(baza_dat)
print(idecka)
