# FUNKCIA
def zrataj(a, b):
    vysledok = a + b
    print(vysledok)
    return vysledok

sucet = zrataj(4324,6545)
print(sucet)

# TODO Domaca uloha spravit funkcie aspon dve

def vypis_policku(slovnik :dict, klucove_slovo: str):
    '''
    Tato funkcia nam vypise obsah policky nasej chladnicky
    :param slovnik: dict
    :param klucove_slovo: string
    :return: None
    '''
    print('OBSAH POLICKY NASEJ CHLADNICKY: ')
    for i in chladnicka[klucove_slovo]:
        print(i)
    return


chladnicka = {'policka1':['maslo','mlieko'],'dvere':['kecup','horcica']}
vypis_policku(slovnik=chladnicka, klucove_slovo='policka1')
vypis_policku(slovnik=chladnicka, klucove_slovo='dvere')

zrataj('AHOJ ', 'SVET')  # nasa funkcia funguje aj so stringami

zrataj(str(434), 'svet')  # funkcia zratej nevie zratat cislo a string... musime cislo pomocou str() zmenit na string