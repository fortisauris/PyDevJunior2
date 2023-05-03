'''

DIFFIE HELLMAN ALGORITMUS NA VYMENU KRYPTOGRAFICKYCH KLUCOV

Zranitelnost symetrickeho sifrovania je v tom, ze obe strany musia mat rovnaky kluc


Asymetricke sifrovanie tento problem riesi pomocou dvojice klucov Privatne - NIKOMU NIKDY NEDAVAT

a verejny kluc - MOZEME ZAVESIT NA INTERNET.

Tento algoritmus je vsak velmi narocny na vypocty, preto po dohodnuti spolocneho kluca pouzijeme symetricku sifru.



'''

# ALICA
AlicineTajomstvo = 898543

# ROBERT
RobertoveTajomstvo = 909432

# Server
g = 95843854038584432   # nahodne cislo s vysokou entropia
n = 911

A_posiela = (g ** AlicineTajomstvo) % n
print('ALICA POSIELA :', A_posiela)

R_posiela = (g ** RobertoveTajomstvo) % n
print('ROBERT POSIELA :', R_posiela)

# ALICA OTVARA ROBERTOV KLUC
Robertov_kluc = (R_posiela ** AlicineTajomstvo) % n
print('Robertov zdielany kluc :', Robertov_kluc)

# ROBERT OTVARA ALICIN KLUC
Alicin_kluc = (A_posiela ** RobertoveTajomstvo) % n
print('Alicin zdielany kluc :', Alicin_kluc)


   # PRETTY GOOD PRIVACY  - bezpecne sifrovanie emailovej komunikacie a suborov

   # VEREJNY KLUC -

   # PRIVATNY KLUC -