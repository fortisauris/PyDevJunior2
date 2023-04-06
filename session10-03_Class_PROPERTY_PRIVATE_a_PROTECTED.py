'''
CLASS PROPERTY

@property
metoda sa zmeni a bude sa spravat ako premenna triedy

__premenna - privatna premenna, ktora nebude pristupna mimo triedy - objekt ju zaprie

_premenna - protected - chranena premenna je oznacena a nemala by sa volat mimo kosu triedy

POZOR_ Python nema mechanizmus, ktory by to kontroloval a tak je to na Programatorovi
'''
class Baterka(object):

    __znacka = 'VARTA'  # TOTO JE PRIVATNA PREMENNA TRIEDY
    _znacka = None  # TOTO JE PROTECTED PREMENNA TRIEDY

    def __init__(self):
        self.model = 'Extra Max'
        self.kapacity = 2700 # mah
        self.typ = 'NiMh'

        print('VZNIKLA BATERKA')

    @property
    def vytlac_kapacitu(self):
        kapacita = self.kapacity + 10
        return kapacita


obj = Baterka()  # tu vznika objekt # tu sa zrealizuje nas plan
print(obj.model)
print(obj.kapacity)
print(obj.vytlac_kapacitu)
print(obj._znacka)
obj._znacka = "DURACELL"
print(obj._znacka)   # premenna je oznacena ako chranena a nemalo by sa k nej pristupovat mimo kodu triedy
print(obj.__znacka)  # vyhodi attributeError