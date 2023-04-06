
'''
ZETTELKASTEN  - ukladanie a nacitavanie karticiek do a z jsonu
'''

import random
import json

baza_dat = dict()  # tu sa nam ukladaju data
idecka = set()  # tu riesime duplicitu id cisel
nazvy_karticiek = set()
def generuj_id():
    id = random.randint(0, 10000000)
    povodna_dlzka_ideciek = len(idecka)
    idecka.add(id)
    if povodna_dlzka_ideciek == len(idecka):  # existuje duplicita
        return None
    else:
        id = str(id).zfill(7) #0000656
        return id

def nova_karticka():
    print('ZADAJ NOVU KARTICKU DO SYSTEMU ZETTELKASTEN')
    nazov_karticky = input("NAZOV KARTICKY : ")
    # TU KONTROLUJEME CI UZ TAKA KARTICKA NEEXISTUJE

    povodna_dlzka_karticiek = len(nazvy_karticiek)
    nazvy_karticiek.add(nazov_karticky)
    if len(nazvy_karticiek) == povodna_dlzka_karticiek:
        print('DUPLICITA V NAZVOCH KARTICIEK !!!')
        # raise ValueError

    # TODO sprav funkciu na kontrolu nazvu karticky  # DUPLICITU VYLUCIT
    id_cislo = None  # defaultna hodnota

    while id_cislo is None:
        id_cislo = generuj_id()
    linky = list()  # prepojenia medzi kartickami
    # TODO linky = zadaj_linky()
    tagy = list()  # mnoziny pomocou tagov
    # TODO tagy = zadaj_tagy()
    obsah_karticky = input('TEXT KARTICKY :')
    baza_dat[id_cislo] = [nazov_karticky, linky, tagy, obsah_karticky]  # tu sa uklada nova karticka do slovnika
    uloz_karticky_do_json()  # ulozi karticky do jsonu

def zadaj_link_alebo_tag():
    pass

def uloz_karticky_do_json():
    with open('index.json', mode='w', encoding='utf8') as file:
        json.dump(baza_dat, file, sort_keys=True, indent=4)
    return

def nacitaj_karticky_z_json():
    vysledok = dict()
    with open('index.json', mode='r', encoding='utf8') as file:
        vysledok = json.load(file)
    return vysledok




# HLAVNY PROGRAM
while True:
    baza_dat = nacitaj_karticky_z_json()
    #TODO Pridaj id karticiek do setu
    #TODO Pridaj nazvy karticiek do Setu
    print(baza_dat)
    nova_karticka()
    print(baza_dat)
    print(idecka)
