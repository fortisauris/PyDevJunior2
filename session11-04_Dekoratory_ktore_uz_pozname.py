'''
DEKORATORY A FUNKCIE VYSSIEHO RADU

@staticmethod  - nevyuziva treidne premenne a je pristupny aj ked nevytvorime instanciu triedy
@classmethod - nevyuziva treidne premenne a je pristupny aj ked nevytvorime instanciu triedy
@property - meni spravanie metody triedy a sprava sa ako premenna triedy

'''


class Nastroje(object):

    def __init__(self):
        print('VZNIKLA TRIEDA NASTROJE')
        self.premenna = 2

    @property
    def krat_dva(self):
        return self.premenna * 2

    @staticmethod
    def vypocet(x, y):
        return x * y * 5463



obj = Nastroje()
print(obj.premenna)
# print(obj.krat_dva())   # volame metodu triedy Nastroje
print(obj.krat_dva)

print(obj.vypocet(5435,6546))
print(Nastroje.vypocet(453,76548))
