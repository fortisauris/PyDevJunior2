# SESSION 26 - FASTAPI SECURITY

## FA03 - Api DAJ SI MIKINU
Našou úlohou je vytvoriť aplikáciu pre pubeťákov aby vedeli, či si 
v danom meste majú dať mikinu keď idú von.

Aplikácia sťahuje data z open-meteo api, ktorá potrebuje 
údaj o zemepisnej šírke a dĺžke. Údaje máme uložené v našej
falošnej databáze. Máme zatiaľ uložené dve mestá = iba Bratislavu
a Košice.

údaje z databázy potom vložíme do requestu pre api. 
Poskytnuté údaje z requestu zmeníme a vytiahneme z nich 
údaje o teplote v danom meste.

Logika nastavuje teplotu kedy si treba a kedy netreba 
zobrat mikinu. Informáciu poskytuje prostredníctvom
našej api, ktorú môže využiť ďalšia appka lebo skript.



## FA04 - Modely Pydantic, validator, FIle Upload a

Vo FASTAPI má na starosti vytváranie dátových modelov 
Pydantic. Tento spôsob nám určuje obsah dát poskytovaných
api. Pydantic zabezpečuje množstvo funkcií pri modelovani 
a validovaní vstupov.

Vieme spraviť aj vlastné validátory, ktoré nám kontrolujú
vstup dát do api a z nej.

Ďalšiu route sme spravili jednoduchý formulár na posielanie 
súborov na náš server. Potrebujeme funkciu na ukladanie
súborov v binárnom formáte t.j. bytoch. 



## FA05 Simple Security pomocou API key

Na bezpečné pripojenie k api sa využíva miesto klasického hesla 
tzv. api-key, dlhý jedinečný reťazec, ktorý identifikuje 
užívateľa a je oveľa bezpečnejší ako heslo. 

Kľúč expiruje po určitom čase. Na vygenerovanie api kľúča
využijeme simple_fastapi_security, ktorý nainštalujeme cez pip
pip. je to jednoduchý fastapi router , ktorý nám pridá 
route /auth. 

Pri spustení servera sa nám vygeneruje primárny kľúč, 
ktorý nám umožní cez auth vytvárať užívateľské kľúče pomocou ktorých
môžeme využívať routy api, ktoré sú chránené.



## FA06 Autorizacia pomocou tokenou podľa štandardu Auth0

Ešte lepšie zabezpečenie našej api nám poskytne Login manager,
ktorý zabezpečí autorizovaný vstup do našej api k chráneným
route. 

auth0 je spôsob autentifikácie kde miesto hesla sa použije 
token ktorý vytvorí verejne známa platforma ako GOOGLE, FACEBOOOK a pod
Nemusíte tak zadávať heslá a identifikujete sa pomocou
svojho účtu na inej službe. 

V našom prípade použijeme login a heslo na vytvorenie 
tokenu na prístup k chránenej api.

Heslo je uložené v našej falošnej databáze. Login manager
nám vráti vytvorí token, ktorý si náš browser zapamätá.
Automaticky sa použije keď sa budeme pripájať na chránenú api route.



## Tajomstvo súboru requirements.txt

v requirements.txt sú uložené všetky dependencies našeho
softvéru. Pomocou príkazu:

``` ps
pip.exe --freeze
```

nám pip vypíše všetky veci, ktoré máme uložené v našej virtuálnej obálke.

do requirements nikdy nedávajte čísla verzie použitého softvéru.
Pokiaľ by ste použili requirements.txt tak by Vám nainštaloval staré
verzie softvéru. VŽDY TREBA POUŽIŤ TIE NAJNOVŠIE VERZIE

``` ps
pip.exe install -r requirements.txt
```

Tento príkaz automaticky nainštaluje všetko čo potrebujete
aby ste mohli váš program v pythone spustiť.


# POĎAKOVANIE

Touto lekciou sme ukončili kurz PyDev2023. Ďakujem za Vašu
pozornosť a húževnatosť pri kódení. Prešli sme dlhú cestu
a veľa ste sa naučili. Dúfam, že Vám šťastie bude priať
a python ale aj iné vedomosti Vám v živote pomôžu.

Kurz bol robený tak aby ste sa dozvedeli čo najviac o
vývoji softvéru ale aj o súvisiacich profesiách ako

tester,
dokumentarista,
Dátový analytik,
developer, 
DevOps,
IT Sec,
kryptológ,
hacker

Nech Vás zaujala ktorákoľvek z týchto profesii, prajem Vám 
všetko NAJ.

Andrej - inštruktor