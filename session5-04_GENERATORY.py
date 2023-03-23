
'''
G E N E R A T O R Y
'''

import random

def vrat_farbu():
    zoznam_farieb = ['cervena', 'oranzova','zelena']
    return zoznam_farieb

def semafor():
    yield 'cervena'
    yield 'oranzova'
    yield 'zelena'

svetla = semafor()
print(svetla)
print(next(svetla))
print(next(svetla))
print(next(svetla))
# print(next(svetla))

svetla = semafor()
print(svetla.__next__())  # cervena

def generator_zoznamu():
    hodnoty = ['alpha', 'bravo', 'charlie', 'delta']
    yield random.choice(hodnoty)

while True:
    alphacodes = generator_zoznamu()
    print(alphacodes.__next__())
    break

for _ in generator_zoznamu():
    print(_)

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

x = fib(50)   # startujeme generator
print(x)
# print(list(x))
for _ in x:
    print(next(x))

for i in fib(10):
    print(i)


# TODO DOmaca uloha spravit vlastny generator
