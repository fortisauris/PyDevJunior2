zoznam = list()  # []
zoznam = ['maslo','maslo']
print(zoznam)

tovar = set(zoznam)
print(tovar)
moj_set = {}  # set()

 # IF ELSE

for i in range(50):
    print(i)
    if i <= 25:
        print("MENSIE")
    if i == 25:
        print('HODNOTA JE 25')
    if i != 25:
        print('HODNOTA NIE JE 25')

vlajocka = True
for i in range(6):
    print(i)
    if i <= 3 and vlajocka is True:
        print("MENSIE")
    else:
        print("NIECO")


# SLOVNIK

zoznam_zoznamov = list()
zoznam_zoznamov.append(['maslo', 'chlieb'])
zoznam_zoznamov.append(['kecup', 'paradajky'])
print(zoznam_zoznamov)

chladnicka = dict()
chladnicka['policka1'] = ['horcica', 'kecup']
chladnicka['policka2'] = ['chren', 'majoneza']
chladnicka['aktualna_teplota'] = 7.05  # stupne celzia
chladnicka['zatvorene_dvere'] = True
print(chladnicka)
print(chladnicka['policka1'])

b = dict()
b['aktualna_teplota'] = 7.35
b['dvere'] = ['mlieko', 4637, 646, 543]
chladnicka.update(b)
print(chladnicka)

print(chladnicka['aktualna_teplota'])
print(chladnicka.get('aktualna_teplota'))

print(chladnicka.keys())
print(chladnicka.values())

# goto cislo_riadku

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

vypis_policku(slovnik=chladnicka, klucove_slovo='policka1')
vypis_policku(slovnik=chladnicka, klucove_slovo='dvere')

zrataj('AHOJ ', 'SVET')

zrataj(str(434), 'svet')

# vypis_policku(chladnicka)  # vypise obsah danej policky

# importy
# triedy a funkcie
# hlavny program


class NasaTrieda(object):

    '''
    Toto je funkcny model objektu skolskej triedy. TOTO JE LEN PLANIK TRIEDY
    '''

    def __init__(self):
        print("VZNIKLA NASA TRIEDA")
        self.menny_zoznam = list()  # zoznam ziakov
        self.pocet_hodin = int()
        self.zoznam_predmetov = list()

    def pocet_ziakov(self):
        '''
        Vrati dlzku menneho zoznamu
        :return: integer
        '''
        return len(self.menny_zoznam)

    def je_ziakom_triedy(self, meno_ziaka):
        '''
        Tato metoda zistuje ci je ziak clenom nasej triedy
        :param meno_ziaka:
        :return: Bool
        '''
        return meno_ziaka in self.menny_zoznam

    def vypis_ziakov(self):
        '''
        vypise menny zoznam ziakov pod seba
        :return: None
        '''
        for i in self.menny_zoznam:
            print(i)
        return


tretiabe = NasaTrieda()  # tu sa narodila nasa trieda
tretiabe.menny_zoznam = ['Peter', 'Jozef', 'Anicka', 'Zuzana']
tretiabe.menny_zoznam.append('Frantisek')
print(tretiabe.pocet_ziakov())
tretiabe.vypis_ziakov()
tretiabe.zoznam_predmetov = ['anglictina', 'matematika']
print(tretiabe.zoznam_predmetov)
print(tretiabe.je_ziakom_triedy('Alan'))
druhace = NasaTrieda()
druhace.menny_zoznam = ['Zuzana',
                        'Jozefina',
                        'Artur']
druhace.menny_zoznam.append('Alan')
print('JE ZIAKOM', druhace.je_ziakom_triedy('Zuzana'))
print(tretiabe.je_ziakom_triedy('Alan'))


class Ryba(object):
    '''
    tato trieda nam ukazuje jednoduchy model ryby
    '''

    def __init__(self, latinsky_nazov: str, voda: str):
        self.nazov = latinsky_nazov
        self.voda = voda
        print('RYBA MENOM', self.nazov, 'ZIJE V', self.voda)

    def plava(self):
        '''
        Jednoducha metoda triedy, ktora umoznuje nasej rybe plavat ked tuto metodu zavolame. Vyuzijeme cyklus FOR
        aby plavala 5x za sebou
        :return:
        '''
        for i in range(5):
            print('PLAVA')
        return


kapor = Ryba(latinsky_nazov='Cyprinus carpio', voda='rybnik')
print(kapor.nazov)
kapor.plava()

class Flasa(object):
    '''
    Trieda je zjednodusenym modelom flase na vodu.
    '''

    def __init__(self, objem, obsah):
        self.farba = 'zelena'  # nastavujeme defaultnu vlstnost flase
        self.objem = objem
        self.obsah = obsah
        self.naplnenost = 0  # v mililitroch defaultne bude prazdna
        print("NOVA FLASA")

    def vylievanie(self, odlej: int):
        '''
        Jednoducha metoda na vylievanie z nasej flase
        :param odlej:
        :return:
        '''
        if self.naplnenost > odlej:
            self.naplnenost -= odlej
        else:
            print("FLASA NEOBSAHUJE DOSTATOK TEKUTINY")  # toto nam vypise ak by sme chceli odliat viac ako je naplnena

    def __repr__(self):
        print('TOTO JE NASA FLASA')
        return

obj = Flasa(objem=1000, obsah='h2o')
print(obj.farba)
print(obj.naplnenost)
obj.farba = 'modra'
print(obj.farba)
obj.naplnenost = 560
print(obj.naplnenost)
obj.vylievanie(odlej=700)
print(obj.naplnenost)

# print(obj)
print(obj.__repr__())
# obj2 = Flasa(500,'olej')
# del obj2
# print(obj2.__repr__())
meno = 'Andrej'
print(meno)
# del meno


# TODO Spravte si nejaky model objektu

class Sardinka(Ryba):

    nazov = 'sardinka atlanticka'

    def __init__(self):
        # self.nazov = 'sardinka atlanticka'
        print('Sardinka')

    def plava(self):
        for i in range(3):
            print(self.nazov, 'PLAVA')

mala_sardinka = Sardinka()
mala_sardinka.plava()
print(mala_sardinka.nazov)