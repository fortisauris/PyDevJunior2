import random

slovnik = dict()
slovnik = {'pes': 'dog',
           'macka': 'cat',
           'prasa': 'pig'
           }

slovicka = list(slovnik.keys())
while True:
    slovicko = random.choice(slovicka)
    print(slovicko)
    odpoved = input('ODPOVED :')
    if odpoved == slovnik[slovicko]:
        print('SPRAVNE')
    else:
        print('NESPRAVNE')