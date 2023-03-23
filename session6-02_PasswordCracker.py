# JEDNODUCHY LUSKAC HESIEL

import hashlib
import itertools

def hash_it(text: str):
    h = hashlib.md5()
    data = bytes(text, encoding='utf8')  # ascii
    h.update(data)
    return h.hexdigest()  # hashstring

# BruteForce utok - vyskusa vsetky kombinacie
# Slovnikovy utok -  vyskusa vsetky pravdepodobne slova zo slovnika
# SOcialne inzinierstvo a OSINT - ziskali sme informacie o Jozefovi z Internetu

Jozef = ["Kapor", 1986, 'Octavia', 'Slovan', 'Maj', 'COrgon', '12','Chorvatsko', 'Anicka', 'Mirka', 'Saris']

def password_cracker(osoba: list):
    '''
    Jednoduchy program, ktory nam vygeneruje zoznam moznych Jozefovych hesiel na zaklade informacii, ktore sme
    ziskali a ulozili do zoznamu osoba
    param1::: osoba -  zoznam moznych poloziek v hesle, zaluby, datumy, osoby, pivo, auto, pes atd..
    return::: result - zoznam kombinacii hesiel
    '''

    dvojice = itertools.combinations(osoba, 2)
    raw_data = list(dvojice)
    print(raw_data)
    print(len(raw_data))
    result = []
    for cast1, cast2 in raw_data:
        result.append(str(cast1)+str(cast2))  # toto nam spoji obe slova
        result.append(str(cast2) + str(cast1))
        result.append(str(cast1) + '1')
        result.append(str(cast2) + '1')
        result.append(str(cast1).upper() + str(cast2).upper())
        result.append(str(cast1).lower() + str(cast2).lower())
    print(result)
    print(len(result))
    return result



# HLAVNY PROGRAM
vysledok = password_cracker(osoba=Jozef)  # vytvarame zoznam pravdepodobnych hesiel
for i in vysledok: # prechadzame nim v cykle
    hashstring = hash_it(i)
    print(i, hashstring)  # tlacime polozky pod seba
    if hashstring == 'a379bf65b522edf354c2188a911bf89b':  # Anicka1
        print("HESLO JE :", i)
        quit()
print('HESLO SA NENASLO')



# SILNE HESLO NAPRIKLAD: N8vzd7_Sa:Zach0v8VPAM*tI_Stu!kova
