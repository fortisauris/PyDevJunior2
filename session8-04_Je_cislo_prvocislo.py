
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

