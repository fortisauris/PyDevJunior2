# ROZCVICKA - PROGRAM NA SKUSANIE OTAZOK
# TODO nezabudnite nainportovat modul
import random


# DATA - otazky, moznosti a spravne odpovede
# kazda otazka bude mat 3 mnoznosti a, b,  c  # TODO pouzil by som slovnik
otazky = {'akej farby je nebo':['a-zelene', 'b-modre', 'c-zlte', 'b'],
          'co je python': ['a-programovaci jazyk', 'b-jednotka lenivosti', 'c-neviemco', 'a']
          }

# HLAVNY PROGRAM

kluce = list(otazky.keys())  # vytahujeme kluce rozumej otazky zo slovnika
while True:  # nekonecny cyklus
    otazka = random.choice(kluce)  # vyberame nahodny kluc
    print(otazka)  # tlacime otazku

    for i in range(0,3):  # tlaci nam moznosti
        print(otazky[otazka][i])

    odpoved = input('zadaj odpoved abc: ')  # vstup od uzivatela
    # logika
    if odpoved == otazky[otazka][3]:  # tu vytahujeme spravnu odpoved a porovnavame ju.
        print('SPRAVNE')
    else:
        print('NESPRAVNE')


# nekonecny cyklus

# Otazky sa budu vyberat nahodne
# TODO pouzite random.choice()
# odpovedat budeme pomocou prikazu input()

# odpoved spravne alebo nespravne
# TODO jednoducha logika na porovnanie spravnych odpovedi a odpovedi
