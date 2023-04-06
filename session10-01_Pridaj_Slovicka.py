# ROZCVICKA

# spravime si prazdny dict.
slovnik = dict()

def pridaj_slovicko(slovnik: dict):
    # 1 budeme pridavat klucove slovo
    kluc = input('ZADAJ KLUC')
    # 2hodnotu v podobe string
    if kluc == 'q':
        print('KONIEC')
        quit()
    hodnota = input('ZADAJ STRING')
    # vlozit do slovnika
    slovnik[kluc] = hodnota
    # zavolam slovnik, urcim klucove slovo = hodnota
    print(slovnik)
    # vyprintovat hodnoty -
    return slovnik

# HLAVNY PROGRAM
while True:
    slovnik = pridaj_slovicko(slovnik)

# funkciou ALEBO
# nekonecnym cyklom