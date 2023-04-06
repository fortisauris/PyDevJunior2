# ROZCVICKA  - Mazacka suborov

# kazdy disk MBR - zoznam ulozenych suborov

# delete subor -- vyskrtne ho zo zozanmu... jeho obsah zostava na disku.

# pouzijeme open na otvorenie suboru mode='r'
with open('skuska.txt', mode='r', encoding='utf8') as f:  # otvorili sme si subor na citanie
    text = f.read()  # nacitali sme jeho obsah

# potrebujeme zistit dlzku textu - len(text)
print(text, len(text))  # vypocitame dlzku obsahu 
# vygenerujeme si rovnako dlhy string zloczeny z 1tiek
mazaci_text = str()
for i in range(len(text)):  #
    mazaci_text += '1'
print(mazaci_text, len(text))
# 5x za sebou zapisat do suboru
for i in range(5):  # cyklus kde 5x za sebou
    with open('skuska.txt', mode='w', encoding='ascii') as f:  # otvorime
        f.write(mazaci_text)  # zapiseme
        print(i, 'PREMAZAL SOM TEXT')  # info ze bolo vymazane

print('DONE')  # koniec

