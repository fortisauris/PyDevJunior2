# Rozcvicka - skusanie slovicok z cudyieho jayzka


import random

# DATA  - dal by som to do slovnika

# nekonecny cyklus
# slovicka=list(slovnik.keys())
# random.choice()

# vstup od uzivatela  - input()


# logika IF ELSE

# za spravnu odpoved uzivatel dostane 5 bodov

# pre pokrocilych - slovicko sa zobrazi iba 5 sekund

# time.sleep(5)
# vymazavanie obrazovky


'''
ADVANCED LIST
'''
a= list()
print(type(a))

a.append('Jergus')
print(a)

print(dir(a))

a.extend(['Maros', 'Roman'])
print(a)

a.insert(2, 'Yveta')
print(a)

a.remove('Maros')
print(a)

if "Andrej" in a:  # podmienka nebola splnena
    a.remove('Andrej')
print(a)

# while True:
meno = a.pop(1)
print(meno, a)

a.clear()
# del a
print(a)


fruits = ['Banany', 'Jablka', 'Ananas', 'Kiwi', 'Jablka']
print(fruits.index("Jablka", 0, len(fruits)))  #
if 'Srobovak' in fruits:
    print(fruits.index("Srobovak", 0, len(fruits)))  #
else:
    print('Ziaden srobovak tu nie je')

print(fruits.count('Jablka'))

fruits.sort(reverse=True)  # nemozeme dat do printu lebo sa nam vrati None
print(fruits)

fruits.reverse()  # modifikuje objekt v pamati a vracia None
print(fruits)

fruits2 = fruits.copy()  # shallow copy plytka kopia
print(fruits2)
print(id(fruits))
print(id(fruits2))
print(id(fruits[0]))
print(id(fruits2[0]))

fruits2.insert(0, 'Srobovak')
print(fruits2)
print(id(fruits2[0]))

# stack
stack = [1,2,3,4,5]
print(stack.pop())
print(stack.pop())
stack.append(6)
print(stack)

del stack[:]
print(stack)

from collections import deque, ChainMap

queue = deque(['Anton', 'Jozef', 'Matus'])
queue.append('Yveta')
print(queue)
print(dir(queue))
queue.popleft()
print(queue)
queue.appendleft('Zuzana')
print(queue)

alpha = [1,2,3,4,5,6]
beta = ['Alpha','Beta', 'Gama']
a = ChainMap(alpha, beta)
print(type(a))
print(a)
for i in a:
    print(i)

# TODO Prestavka do 19:50

'''
JSON - 
'''

import json

a = ['Data', {'World': 56746, 'Amerika':6547, 'Europa':[234,654,765]}]
vystup = json.dumps(a)
print(vystup)

vystup = json.dumps(a, separators=(',',':'))
print(vystup)

vystup = json.dumps(a, separators=(',',':'), sort_keys=True)
print(vystup)

vystup = json.dumps(a, separators=(',',':'), sort_keys=True, indent=4)
print(vystup)

vstup = json.loads(vystup)
print(vstup)


'''
def save_json_file(filename_w_path: str, data: dict):
    with open(filename_w_path, mode='w', encoding='utf8') as f:
        json.dump(data, f, indent=4, sort_keys=True)
        return

save_json_file(filename_w_path='skuska.json', data=a)
'''

def load_json_file(filename_w_path: str):
    with open(filename_w_path, mode='r', encoding='utf8') as f:
        loaded_data = json.load(f)
    return loaded_data


data = load_json_file('skuska.json')
print(data)
for i in data:
    print(i)

'''
Je cislo prvocislo ?
'''

def je_prvocislo(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                print('Nie je prvocislo')
                return False
            else:
                return True
    else:
        return False

for i in range(1,100):
    print(i, je_prvocislo(i))


'''
S T A V I A M E    E N I G M U
'''

# mechanicka cast pohyblive rotory a jeden reverzny rotor
# elektricka cast Plugboard - umoznovala kazde pismeno vymenit za ine pismeno

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sprava = 'BRYNDZAOPETZDRAZELA'

i = abeceda.index('K')
print(i)
nastaveny_valec = abeceda[i:] + abeceda[:i]
print(nastaveny_valec)

def posun_valca(nvalec: str):
    valec = nvalec[1:] + nvalec[0]
    print(valec)
    return valec

# hlavny program

zasifrovana_sprava = str()
for i in range(0, len(sprava)):
    zasifrovany_znak = nastaveny_valec[abeceda.index(sprava[i])]
    zasifrovana_sprava += zasifrovany_znak
    nastaveny_valec = posun_valca(nastaveny_valec)
print(sprava)
print(zasifrovana_sprava)
