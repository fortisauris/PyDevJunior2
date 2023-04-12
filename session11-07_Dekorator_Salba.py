'''
Dekorator salba - bude sa nas snazit presvedcit ze 2 a 2 nie su 4
'''
def salba(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 1

    return wrapper

@salba
def spocitaj(x,y):
    return x+y

print(spocitaj(2,2))

