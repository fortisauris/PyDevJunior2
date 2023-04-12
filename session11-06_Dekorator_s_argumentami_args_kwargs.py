'''
FUNKCIA DEKORATORA S PARAMETRAMI (*args, **kwargs)
'''

def hello(func):

    def wrapper(*args, **kwargs):
        print('START PROGRAMU - KOD KTORY SKONTROLUJE CI MENO NIE JE V ZOZNAME VULGARIZMOV')  # skontroloval nieco
        result = func(*args, **kwargs)
        print('POZDRAV BOL USPESNE DOKONCENY')  # poupratoval po sebe
        return result

    return wrapper

@hello
def pozdrav(meno: str, pocet: int):
    for i in range(0,pocet):
        print('AHOJ', meno)

pozdrav('Vlado', 5)

