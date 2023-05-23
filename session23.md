# NONSQL DATABAZY

## REDIS

NonSQL databáza, ktorá ukladá dáta podobne ako
Python slovníky, listy a premenné v pamäti. 

# KONTAJNERIZACIA

## DOCKER = kontajnerizácia programov

Monoliticky kod miliony riadkov kodu

Microservices = každý program žije vo svojom kontajneri a
komunikuje s užívateľom a inými algoritmami pomocou
browseru a API.


### Microservisy - 

Spôsob akým tvoriť jednoduché programy, servery a škálovať ich
či meniť za chodu.

## KUBERNETES
Softvér rozdeľujúci úlohy pre viacero počítačov zapojených 
v cluster computing


# FLASK BLUEPRINTS
Pokračujeme v FL05

Blueprinty sú podaplikácie hlacnej aplikácie Flasku, ktoré
sú samostatné a majú samostatné routy, templaty aj statiku

Možno ich jednoducho medzi Flaskovymi appkami prenasat.

TREBA ICH ZAREGISTROVAT V APP

# TESTY POMOCOU UNITEST A MOCK OBJECT

### Premiestnenie testov do samostatneho balicka

Unittest TestCase trieda 

testy spustame pomocou pytest


# FLASK LOGIN MANAGER
Pokračujeme v FL06


Na vytvorenie bezpečného formulára vo Flasku vytvoríme formulár
pomocou LoginManageru

Tento nám ošetrí proihlasovanie, porovnávanie s databázou-zoznamom
užívateľov a umožní prihlásenému užívateľovi pripojiť sa 
na CHRANENE ROUTy.

POZOR heslá idú v tomto prípade v otvorenom stringu v requeste

Flask nám umožňuje zaheslovať heslá, ktoré ukladáme do DB

Heslo s formulára musí byť zahashované v browseri pomocou javascriptu

V produkcii  server pobeží cez https, ktoré zabezpečí šifrovanie pomocou SSL
certifikatu
