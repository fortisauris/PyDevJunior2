cislo = 5
while cislo < 100:  # nekonecny cyklus
    cislo *= 2
    print(cislo)


text = "AHOJ"
while True:
    for i in range(0,10,2):
        print(i, text)
    break
print("DONE")
