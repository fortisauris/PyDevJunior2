# NAJPRV IMPORTY
import hashlib
import re
import pickle

'''
# POTOM FUNKCIE A TRIEDY
def hash_it(text: str):
    h = hashlib.md5()
    data = bytes(text, encoding='utf8')  # ascii
    h.update(data)
    return h.hexdigest()


# HLAVNY PROGRAM
hashstring = hash_it('7567')
print(hashstring)


# BRUTEFORCE
for i in range(0, 10000):  # slabe heslo
    hashstring = hash_it(str(i))
    print(i, hashstring)
    if hashstring == '90ef635b07e4335585e9aa6c7d742e94':
        print('MAM TA JE TO ROZLUSKNUTE. HESLO JE :',i)
        quit()

# janka35

# V!9ra_som_v9c9ral_ryb0

# REGULAR EXPRESSIONS

# modul re
'''
text = 'Vcera som bol v kine a davali uplne nudny film. som.'

vysledok = re.findall(pattern='som', string=text)
print(vysledok)

print(re.search(pattern='som', string=text[9:]))
print(re.match(pattern='som', string=text[6:9]))
print(re.fullmatch(pattern='som', string=text[-4:-1]))
a = re.fullmatch(pattern='som', string=text[-4:-1])
print(a)
print(a.group())
print(a.span())

# klasicka pomenovana funkcia

def sucet(x,y):
    return x + y

print(sucet(5443,6546))

# anonymne funkcie  LAMBDA funkcia
vysledok = lambda x, y: x + y

print(vysledok(10,10))

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


    @classmethod
    def file_exist(cls, filename_w_path: str):
        """

        """
        try:
            f = open(file=filename_w_path, mode='r', encoding='utf8')
            f.read()
        except FileNotFoundError:
            return False
        finally:
            pass
        return True


a = FileTools.file_exist(filename_w_path='session32.py')
print(a)
if a is False:
    print('SUBOR NEEXISTUJE')
else:
    print("SUBOR SA NASIEL A BUDE NACITANY")

# TODO Prestavka do 19:50

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def posunuta_abeceda(posun: int):
    """
    Funkcia upravi abecedu pomocou jednoducheho posunu pismen o urcenu hodnotu
    :param posun:: integer
    return:: posunuta_abeceda
    """
    return abeceda[posun:] + abeceda[:posun]

def cezar_enc(text: str, posun: int):
    posunuta = posunuta_abeceda(posun)
    enc_text = str()  # ''
    for i in text:
        if i == ' ':
            enc_text += " "
        else:
            symbol_pozicia = int(abeceda.index(i))
            enc_text += posunuta[symbol_pozicia]
    return enc_text.upper()

print(cezar_enc("AHOJTE VSETCI A PRAJEM VAM VELA USPECHOV V PROGRAMOVANI", 4))

# ELSNXI ZWIXGM E TVENIQ ZEQ ZIPE YWTIGLSZ Z TVSKVEQSZERM

# TODO Spravit program na desifrovanie tejto sifry

class Auto(object):

    def __init__(self):
        self.farba = 'biela'
        self.palivo = 'diesel'

    def motor(self):
        return 'BRM BRM'



obj = ['Andrej', "Peter", [543,654,757,645,87,], True, False, False]
zavaranina = pickle.dumps(obj=obj)
print(zavaranina)
obj2 = pickle.loads(zavaranina)
print(obj2)

auto = Auto()
auto.farba = 'zelena'
zavaranina = pickle.dumps(obj=auto)
print(zavaranina)
obj2 = pickle.loads(zavaranina)
print(obj2)
print(obj2.palivo)
print(obj2.farba)


with open(file='zavaranina.hex', mode='wb') as f:
    pickle.dump(obj=auto, file=f)

with open(file='zavaranina.hex', mode='rb') as f:  # v tomto riadku nacitavame hexadecimalne data
    auto_obj = pickle.load(file=f)

print(auto_obj)  # TOHOTO SA NECHYTAJ
print(auto_obj.farba)
print(auto_obj.motor)  # TOTO JE MAGIA
print(auto_obj.palivo)  #

def text():
    '''Tato funkcia nerobi nic ale chcem Vam ukazat ako v pythone funguje doctring
    return ::: 'COKOLVEK' String
    '''
    return 'COKOLVEK'

print(text.__doc__)
print(posunuta_abeceda.__doc__)