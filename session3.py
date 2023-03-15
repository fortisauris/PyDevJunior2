# importy
import random
import time
import sys
import os


# Triedy a funkcie
class Teplomer(object):
    """
    Trieda Teplomer je jednoducha trieda na uchovavanie teploty
    """
    def __init__(self):
        self.teplota = 21  # stupne celsia

    def get_teplota(self):  # getter
        return self.teplota

    def set_teplota(self, stupne_celsia: float):  # setter
        self.teplota = stupne_celsia
        return


def no_zero(n: int):
    if n == 0:
        return False
    else:
        return True


class Rodic(object):

    def __init__(self):
        self.temperament = 'cholerik'
        print('SOM CHOLERIK')

    def get_temperament(self):
        return self.temperament


class Dieta(Rodic):

    def __init__(self):
        super().__init__()  # preberame __init__ rodica


'''
SNIPPET FileTools
'''


class FileTools(object):

    @staticmethod
    def file_save(filename_w_path: str, plaintext: str):  # 'C:\ADRESAR\SUBOR'
        f = open(file=filename_w_path, mode='w', encoding='utf8')  # mode w znamena write zapisovanie  # latin2
        f.write(plaintext)
        print('SUBOR SA ULOZIL')
        f.close()
        return

    @classmethod
    def file_load(cls, filename_w_path: str):
        f = open(file=filename_w_path, mode='r', encoding='utf8')  # mode r znamena read
        nacitany_text = f.read()
        print(nacitany_text)
        f.close()
        return nacitany_text

# S C Y T A L E

def scytale_enc(text: str, hrubka_palice: int):
    zasifrovana_sprava = str()  # ""
    for pismeno in text:
        zasifrovana_sprava += pismeno
        for _ in range(0, hrubka_palice):
            nahodny_znak = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            zasifrovana_sprava += nahodny_znak
    return zasifrovana_sprava





''' MAIN - hlavny program sa vykonava  '''
teplota_v_obyvacke = Teplomer()  #
print(teplota_v_obyvacke)
print(teplota_v_obyvacke.get_teplota())
teplota_v_obyvacke.set_teplota(22.5)
print(teplota_v_obyvacke.get_teplota())

print(no_zero(45356))
print(no_zero(0))

obj = Dieta()

FileTools.file_save(filename_w_path='skuska.txt', plaintext='ALe nic nedavaju')
FileTools.file_load(filename_w_path='skuska.txt')

# MODUL RANDOM
for i in range(10):
    print(random.random()*1000)

print(random.randint(1,9999))
zoznam_mien = ['Andrej', 'Tomas', 'Veronika', 'Peter']
vybrane_nahodne_meno = random.choice(zoznam_mien)
print(vybrane_nahodne_meno)
print(random.randbytes(256))  # byte je hodnota od 00 do ff v hexadecimalnom kode   0 do 256

# MODUL TIME
print(time.time())   #  UNIX cas od 1.1.1970
print(time.localtime())
t = time.localtime()
print(str(t[0]) + "." + str(t[1])+'.'+str(t[2]))
print(t[2],t[1],t[0])
print(t[0:])
nas_cas = str(t[:6])
FileTools.file_save("nas_cas.txt", nas_cas)

print(time.strftime("%H:%M:%S"))


'''  ZACHYTAVANIE CHYB V KODE POMOCOU BLOKU try:except:finally'''
n = 0
try:
    vysledok = 4563634/n
except ZeroDivisionError:
    print('NEDA SA DELIT NULOU')
    n = 1
    vysledok = 4563634/n
    # quit()
finally:
    print(vysledok)
    pass


# TODO PRestavka do 19:50

if "nieco" != "nieco_ine":
    pass

moje_heslo = 'veslo'  #

# SCYTALE  - dve rovnako hrube palice.
sprava_pre_nacelnika = 'BRYNDZAZDRAZELA'
zasifrovane = scytale_enc(sprava_pre_nacelnika, hrubka_palice=5)
print(zasifrovane)

# TODO Desifrovanie SCYTALE

for i in range(10):
    print(i)
    print("Nieco")

print(sys.platform)
if sys.platform == 'win32':
    print('AHOJ WINDOWS')
    osystem = 'W'
else:
    print('AHOJ UNIX')
print(osystem)

print(sys.version_info)

print(random in sys.modules.keys())

for i in sys.modules.keys():
    if i == 'random':
        print(i)

print(sys.path)

print(sys.argv)


#if sys.argv[1] == 'POSLI_EMAIL':
    # print('POSLAL SOM EMAIL NA ADRESU', sys.argv[2])

os.system(command='cls')
print(os.listdir())
os.chdir('C:')
print(os.listdir())