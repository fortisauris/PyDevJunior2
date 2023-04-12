
# PROGRAM NA DEBUGGOVANIE A TESTOVANIE

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

# Unittest -
# pytest

# PRVE TESTY
'''
pytest nainstalujeme cez terminal ->  python.exe -m pip install pytest
spustame bud v pycharme alebo v terminali -> python.exe -m pytest SUBOR.py

PYTEST NAJDE VSETKY funkcie nazvane ako test... a spusti testovanie

'''
def test_urob_sucet():
    assert sucet(2, 2) == 4
    assert sucet('AHOJ ', "SVET") == 'AHOJ SVET'
    assert sucet('54354', 564356) == 618710

def test_urob_delenie():
    assert urob_delenie(100,2) == 50
    assert urob_delenie(100,0) == 100

def test_je_cele_cislo():
    assert je_cele_cislo(50) is True
    assert je_cele_cislo(10.5) == False
    assert je_cele_cislo(-10.5) == False
    assert je_cele_cislo(None) == False
    assert je_cele_cislo('AHOJ') == False


