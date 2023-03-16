import pickle

# Modul na zavaranie objektov
class Auto(object):
    '''
    Jednoducha trieda urcena na demonstraciu zavarania objektov v pythone
    '''

    def __init__(self):
        self.farba = 'biela'
        self.palivo = 'diesel'

    def motor(self):
        return 'BRM BRM'


# HLAVNY PROGRAM
obj = ['Andrej', "Peter", [543,654,757,645,87,], True, False, False]
zavaranina = pickle.dumps(obj=obj)
print(zavaranina)
obj2 = pickle.loads(zavaranina)
print(obj2)

auto = Auto()
auto.farba = 'zelena'
zavaranina = pickle.dumps(obj=auto)
print(zavaranina)
obj2 = pickle.loads(zavaranina)
print(obj2)
print(obj2.palivo)
print(obj2.farba)


with open(file='zavaranina.hex', mode='wb') as f:
    pickle.dump(obj=auto, file=f)

with open(file='zavaranina.hex', mode='rb') as f:  # v tomto riadku nacitavame hexadecimalne data
    auto_obj = pickle.load(file=f)

print(auto_obj)  # TOHOTO SA NECHYTAJ
print(auto_obj.farba)
print(auto_obj.motor)  # TOTO JE MAGIA
print(auto_obj.palivo)  #
