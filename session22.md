# SESSION22- FLASK TRETIA APPKA, ÚVOD DO SQL a pythonanywhere.com

## session a Session()



V tretej appke si vytvoríme Session, ktorá neukladá veci 
u užívateľa v Brwseri ae priamo u nás na serveri


Stále sme však nevyriešili problém s ukladaním dát zasielaných 
našimi užívateľmi.

### Máme tieto možnosti:

1. ukladať veci zo session do súboru napr json (pokiaľ bude informácii naraz veľa server ich nebude stíhať zapisovať a čítať)
2. ukladať informácie do databázy sqlite3, ktorá má databázu uloženú v jednom súbore (jednoduché a lepšie riešenie)
3. Použijeme databáyový server SQL alebo NonSQL databázy (Toto je preferované a profesionálne riešenie umožňujúce zapisovať a čítať naraz množsstvu užívateľom)

!!! POZOR: Inštalovanie Databázového servera na Windows nie je optimálnym riešením.

### Preto budeme databázu skúšať:
1. na stránke pythonanywhere.com kde je MySQL
2. na našom serveri kde je Redis, MariaDb a sqlite3
3. môžeme vytvoriť VM = virtuálnu mašinu s linuxom

## SQL = Standard Query Languague
Jazyk pre zadávanie príkazov relačným databázam. Relačné databázy ukladajú informácie do tabuliek a prepájajú 
ich tzv. reláciami

Tutorial je v adresári FL04

