# ROZCVICKA  - Mazacka suborov

# kazdy disk MBR - zoznam ulozenych suborov

# delete subor -- vyskrtne ho zo zozanmu... jeho obsah zostava na disku.

# pouzijeme open na otvorenie suboru mode='r'
with open('skuska.txt', mode='r', encoding='utf8') as f:
    text = f.read()

# potrebujeme zistit dlzku textu - len(text)
print(text, len(text))
# vygenerujeme si rovnako dlhy string zloczeny z 1tiek
mazaci_text = str()
for i in range(len(text)):
    mazaci_text += '1'
print(mazaci_text, len(text))
# 5x za sebou zapisat do suboru
for i in range(5):
    with open('skuska.txt', mode='w', encoding='ascii') as f:
        f.write(mazaci_text)
        print(i, 'PREMAZAL SOM TEXT')

print('DONE')

