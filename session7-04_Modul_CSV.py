# Modul csv -- Comma separated Variables

a = [12, True, 'Jolana', 564.564]
b = [14, False, 'Jozef', 65.76]

import csv  # comma separated values

# zapis do csv suboru
with open('data.csv', mode='w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, dialect='excel', delimiter=' ')
    print(type(datawriter))
    datawriter.writerow(a)
    datawriter.writerow(b)
    print('DONE')

with open('data.csv', mode='r', newline='') as csvfile:  # read
    datareader = csv.reader(csvfile, delimiter=' ')
    print(type(datareader))
    for riadok in datareader:
        print(riadok)
    print('DONE')

with open("names.csv", mode="w", newline="") as csvfile:
    fieldnames = ["meno", 'priezvisko']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"meno": "Jozef", "priezvisko": "Mrkvicka"})
    writer.writerow({"meno": "Bohuslav", "priezvisko": "Kovac"})
    writer.writerow({"meno": "Roman", "priezvisko": "Kristof"})

with open("names.csv", mode="r", newline="") as csvfile:
    datareader = csv.DictReader(csvfile)
    for riadok in datareader:
        print(riadok['meno'], riadok['priezvisko'])

print(csv.list_dialects())