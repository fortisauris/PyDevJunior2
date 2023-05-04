'''
LIST a DICT COMPREHENSIONS
'''

# KLASIKA
zoznam = list()
for i in range(6):
    if i * 3.14 != 0:
        zoznam.append(i * 3.14)
print(zoznam)

# MODERNE RIESENIE V PYTHONE

zoznam = [i * 3.14 for i in range(6) if i * 3.14 != 0]   # [funkcia, cyklus, podmienka]
print(zoznam)


# TOTO ISTE MOZEME SPRAVIT AJ SO SLOVNIKOM

meno = 'Milan'
slovnik = {x:meno[x] for x in range(len(meno))}
print(slovnik)
print(slovnik.keys())
print(slovnik.values())