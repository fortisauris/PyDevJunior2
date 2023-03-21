
'''
JEDNODUCHY PROGRAM LIGA
'''

import itertools


teams = ['Liverpool', 'FC Barcelona', 'Manchester United', 'AJAX Amsterdam']
zapasy = itertools.combinations(teams, 2)
# print(list(zapasy))

liga = dict()  # slovnik
for i in zapasy:
    # zapas = next(zapasy)  # < -- Tu bola chyba - mali sme volat i a nie vytahovat zaznamy zo zapasov
    # print(i)
    key = i[0] + ':' + i[1]
    print(key)
    liga[key] = [0,0]

print(liga)
print(len(liga))

# TODO Vyhladat chybu v programe
