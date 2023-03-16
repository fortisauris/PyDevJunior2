import re

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


# Vlastne retazce na vyhladavanie mozete vyskusat najprv na webovej stranke   https://regexr.com/