 # IF ELSE

for i in range(50):
    print(i)
    if i <= 25:
        print("MENSIE")
    if i == 25:
        print('HODNOTA JE 25')
    if i != 25:
        print('HODNOTA NIE JE 25')

vlajocka = True
for i in range(6):
    print(i)
    if i <= 3 and vlajocka is True:
        print("MENSIE")
    else:
        print("NIECO")

