
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
