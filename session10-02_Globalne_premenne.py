'''
GLOBALNA PREMENNA
'''



def vytlac_hodnotu(n):
    # global val  # <--- TU PREPNI  vravime pythonu, ze premenna val ma byt globalna a pristupna aj mimo funkcie vytlac_hodnotu
    val = 5454
    hodnota =  n + val  # potrebujeme ju dostat sem
    return hodnota

print(vytlac_hodnotu(543))
print(val)  # ak val nie je glabalna premenna vyhodi NameError
