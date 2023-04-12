
USER = 'admin'  # <- tu zmen uzivatela

def admin(func):

    def wrapper(*args, **kwargs):
        if USER == 'admin':
            func(*args, **kwargs)
            print('NASTAVENIA BOLI ULOZENE')
            return True
        else:
            print('UZIVATEL ', USER, ' NEMA OPRAVNENIE UKLADAT ZMENY')
            return False

    return wrapper
@admin
def ulozenie_nastevenia_servera():
    print('KONFIGURACIA SERVERA BOLA ULOZENA')

ulozenie_nastevenia_servera()

# TODO Spravit jednoduchy dekorator

