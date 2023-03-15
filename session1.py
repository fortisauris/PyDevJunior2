print("Hello World")  # tento prikaz nam vypise obsah zatvorky do vystupu

cele_cislo = 5
rychlost_rotora_tretieho_motora = 3500  # otacky za minutu
nejaka_ina_premenna = 10
print(cele_cislo, rychlost_rotora_tretieho_motora)
cele_cislo += 56476
print(cele_cislo)  # INTEGER
# cele_cislo = int()  #
print(cele_cislo)
cele_cislo = cele_cislo + 5
print(cele_cislo)
a = int()
cele_cislo += 5
cele_cislo *= nejaka_ina_premenna
print(cele_cislo)

cele_cislo = 'TEXT'  # STRING
print(cele_cislo)
vysledok = cele_cislo * 5
print(vysledok)

cele_cislo = 5
# vysledok = cele_cislo / 0

cislo_s_desatinnou_ciarkou = float()  # 0.46325764537  a 452356437.0543
print(cislo_s_desatinnou_ciarkou)
cislo_s_desatinnou_ciarkou = 2.584
print(cislo_s_desatinnou_ciarkou + .3)
vypocet = int(cislo_s_desatinnou_ciarkou)
print(vypocet)


# Logicka hodnota
vlajocka = bool()  # True alebo False
print(vlajocka)  # defaultne je False
vlajocka = True
print(vlajocka)

# Textovy retazec STRING

text = str()
print(text)
text = ""
text += "Toto som teraz vymyslel. teraz"
print(text)
print('teraz' in text)
vysledok = "teraz" in text
print(vysledok)
print(len(text))  # dlzka textoveho retazca - STRINGU

print(text.upper())
print(text.lower())
print(text.islower())

print(text.count("teraz"))
print(text.split('.'))  #   Vystup z tohoto bude ZOZNAM v Python list  []

text += "\n\t" + "Ahojte" + " Andrej"
print(text)

# text -= "teraz"  # TODO TOTO NEFUNGUJE
print(text[0])
print(len(text))
print(text[0:5])
print(text[10:15])
print(text[15])
print(text[-6:])

# TODO PRESTAVKA DO 19:50

# FOR cyklus
for _ in range(0, 10, 2):
    print("Hello World")
    print(435)

vysledok = str()
for i in text:
    vysledok += i
    print(vysledok)

for i in range(0, len(text)):
    print(i, text[i], text[i].isspace())

cislo = 5
while cislo < 100:  # nekonecny cyklus
    cislo *= 2
    print(cislo)

while True:
    for i in range(0,10,2):
        print(i, text)
    break
print("DONE")


# OZUBENE KOLIESKO
pocitadlo = 0
for i in range(0, 32):
    print(i, pocitadlo, "UROB VOLACO")
    pocitadlo += 1

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

konstanty = tuple()
konstanty = ("A", "B", "C")
print(konstanty.count("A"))