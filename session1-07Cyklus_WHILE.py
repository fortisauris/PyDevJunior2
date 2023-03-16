cislo = 5
while cislo < 100:  # nekonecny cyklus
    cislo *= 2
    print(cislo)
# tu pokracuje nas program

text = "AHOJ"
while True:  # nekonecny cyklus
    for i in range(0,10,2):
        print(i, text)
    break
print("DONE")
