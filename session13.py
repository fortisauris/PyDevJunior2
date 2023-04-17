'''
OPAKOVANIE ZAKLADNEHO SYNTAXU
'''

# PREMENNE alebo VARIABLES

a = int() # cele cislo
a = 58473756
print(type(a))
print(dir(a))
a += 54
a = a.__add__(54)
print(a)

a = float()
a = 4354.65654

# stringy
text = str()
text = ''
text += 'Ahoj'
print(text)

flag = bool()
flag = True
if flag is False:
    print('F')
print(flag)

a = bytes('hfjdj', encoding='utf8')
print(a)

# input('ZADAJ VOLACO')
# quit()

list()  # mustovatelny
tuple()  # nemutovatelne
set()
dict()

# cykly

for cokolvek in range(6):
    print(cokolvek)

while cokolvek == 5:
    print('CISLO 5 ZIJE')
    break


print('DONE')

# riadenie toku programu pomocou logiky
if a == 'Hello':
    if cokolvek == 5:
        print('PAT')
    elif cokolvek == 6:
        pass
    else:
        pass

def sucet_fn(a,b):
    print( a + b)
    return  a + b

# anonymne funkcie
sucet = lambda a,b: a + b
print(sucet(10,10))

# Triedy

class Ponozka(object):

    def __init__(self):
        self.status = 'cista'
        self.material = 'bavlna'
        print('VZNIKLA NOVA PONOZKA')

    def __del__(self):  # DESTRUCTOR
        print('ZANIKLA NOVA PONOZKA')

    #def __repr__(self):

    def status_setter(self, status):
        self.status = status

obj = Ponozka()
print(obj.status)
obj.status_setter(status='spinava')
print(obj.status)
del obj

# input()

# DEPENDENCIES - pip


# virtualna obalka
# python 3.11
# pip

# TODO Prestavka do 19:50