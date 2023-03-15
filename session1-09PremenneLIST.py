# ZOZNAM
zoznam_potravin = list()
print("VYPIS ZOZNAM POTRAVIN :\t",zoznam_potravin)
zoznam_potravin = ["chlieb", "maslo", "mlieko"]
print("VYPIS ZOZNAM POTRAVIN :\t",zoznam_potravin)
zoznam_potravin.append("kecup")
print("VYPIS ZOZNAM POTRAVIN :\t",zoznam_potravin)
zoznam_potravin.append("maslo")
print("VYPIS ZOZNAM POTRAVIN :\t",zoznam_potravin)
zoznam_potravin.remove("maslo")
print("VYPIS ZOZNAM POTRAVIN :\t",zoznam_potravin)
zoznam_potravin.remove("maslo")
print("VYPIS ZOZNAM POTRAVIN :\t",zoznam_potravin)
# zoznam_potravin.remove("maslo")
# print("VYPIS ZOZNAM POTRAVIN :\t",zoznam_potravin)
print(len(zoznam_potravin))

for potravina in range(0, len(zoznam_potravin)):
    print(potravina, zoznam_potravin[potravina])

print(zoznam_potravin[-1])
print(zoznam_potravin[0])
print(zoznam_potravin[:3])

a = list()
pocitadlo = 0
while pocitadlo < 1000000:
    a.append(pocitadlo)
    pocitadlo += 1
print(a)