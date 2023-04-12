
# PROGRAM NA DEBUGGOVANIE

def sucet(a,b):
    try:
        result = a + b
    except TypeError:
        result = int(a) + int(b)
    finally:
        return result

def urob_delenie(a,b):
    if b == 0:
        b = 1
    return a / b

def je_cele_cislo(n):
    if n is None or str(n).isalpha():
        return False

    if n == int(n):
        return True
    else:
        return False


print(sucet(5,0))
print(urob_delenie(5,0))
'''
for i in range(25):
    # if i == 20:
        # raise ValueError
    print(i)
'''
# TODO Prestavka do 19:50
