import itertools
import time

a = iter('ABCD')  # vstavany prikaz pythonu
print(a)
print(list(a))

zipsujeme = zip([1,2,3], ['Martin', 'Vlado', 'Jozef'])
print(zipsujeme)
print(list(zipsujeme))

zipsujeme = zip([1,2,3], ['Pomaranc', 'Mandarinka', 'Pomelo', 'Limetka'])
print(zipsujeme)
print(list(zipsujeme))

zipsujeme = itertools.zip_longest([1,2,3], ['Pomaranc', 'Mandarinka', 'Pomelo', 'Limetka'], fillvalue=0)
print(zipsujeme)
print(list(zipsujeme))

bankovky = [10,50,5,100,20]
print(list(itertools.combinations(bankovky,4)))
print(list(itertools.combinations_with_replacement(bankovky,4)))

a = 'ABC'
print(list(itertools.permutations(a)))

counter = itertools.count()
while True:
    c = counter.__next__()  # next(counter)
    print(c)
    time.sleep(.5)
    if c == 6:
        break

c = itertools.count(start=.2, step=-.3)
print(list(next(c) for _ in range(5)))  # pythonisticky sposob ako vypisat 5 hodnot z pocitadla

opakovanie = itertools.repeat(True, 10)
print(list(opakovanie))

opakuj_cyklus = itertools.cycle('ABCDEF')
print(opakuj_cyklus)
for i in range(10):
    print(next(opakuj_cyklus))

a = [1,2,3,4,5]
print(list(itertools.accumulate(a)))
print(list(itertools.accumulate(a, lambda x, y: (x+y)*2)))

a = itertools.product([1,2],["A","B"], [True, False])
print(a)
print(list(a))

a, b = 1, 2
iterator1, iterator2, iterator3 =  itertools.tee('ABCDEF', 3)
print(list(iterator1))
print(list(iterator2))
print(list(iterator3))

