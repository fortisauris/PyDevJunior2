
a = 25464
print(type(a))  #
print(dir(a))  # vsetky moznosti co s tym mozeme robit
print(abs(a))
print(a.bit_length())   # 0101010110101110101  bit = 0 alebo 1   a byte = 0000000 po 11111111
print(a.to_bytes(2, byteorder='little'))
print(a.__hash__())
print(a.__eq__(25464))

a = 'Hello WOrld'
print(type(a))
print(dir(a))
print(a.capitalize())
print(a.casefold())
print(a.center(24, ' '))
print(a.count('l'))
print(a.encode(encoding='utf8', errors='strict'))
print(a.endswith(('d', 'o'),0,5))
print(a+'\tDObre\t'.expandtabs(tabsize=4))
print(a.find('H', 0, len(a)))


print(type([1,2,3]))
print(dir([1,2,3]))


print('Hello', 'World', 'Ako sa mas ?')

# FORMATOVANIE TEXTU MODERNYM SPOSOBOM

a = 'Toto je udaj {0} vlozeny formatovanim textu {1}'
print(a.format('HODNOTA0', "HODNOTA1"))

print(a.index('udaj', 0, len(a)))
# FUNKCIE NA SKUMANIE OBSAHU STRINGU
print('alpha154356'.isalnum())
print('alpha154356'.isalpha())
print(a.isascii())
print('agfd154356'.isdecimal())
print('54356'.isdigit())
print('alpha154356'.isidentifier())  # ze moze byt pouzity ako pomenovanie ...
print('alpha154356!!'.isalnum())

print('alpha154356'.islower())
print('alpha154356'.isnumeric())
print('alpha154356'.isprintable())  # 255
print('alpha154356'.isspace())  # ci je to medzernik

a = 'Hello'
print(a.join(' World'))
print(a.lstrip("H"))
print(a.removeprefix('H'))
print(a.removesuffix('o'))
print(a.swapcase())
print('654'.zfill(8))

vysledok = str()
for i in 'Hello453':
    if i.isalpha():
        vysledok += i
print(vysledok)

# POKROCILE FORMATOVANIE TEXTU

print('Tento %(jazyk)s je uradny jazyk %(obyvatelov)05d na Mauriciu.' % {'jazyk': "francuzsky", 'obyvatelov':5435})
