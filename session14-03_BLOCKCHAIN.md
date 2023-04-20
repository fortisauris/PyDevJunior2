# BLOCKCHAIN - koncept


technologia retazenia dat a ich decentralizovane ukladanie sposobom aby nemohlo ist k 
neopravnenej manupulacii s nimi


##  BitCoin a kryptomeny

Vacsina ludi ma spojenu tuto technologiu s kryptomenami, ktore maju 
svoje vyhody aj nevyhody. BLOCKCHAIN je vsak ovela viac. 


## PRIKLAD NA ZAMYSLENIE

### Tradicny model v Banke
Tradicne riesenie bolo mat SQL server s udajmi a chranit ho aby niekto nemohol
udaje pozmenit

#### UDAJ1 andrej ma 7eur  <- hacker ho zmeni na 7000EUR
#### UDAJ2 vlado ma 50eur

### BLOCKCHAIN retaz blokov
Blockchain uklada data v tomto pripade stav uctu a informacie o 
transakciach do tzv. blokov.

Pomocou hashovacieho algoritmu vypocita hashstring dat

Prvy blok sa nazyva seed:
#### h1 = hash(UDAJ1)  # seed

Pri vypocte druheho blocku prida hash seedu k druhemu blocku
a tym ich pripoji k retazi blokov: 
#### h2 = h1+UDAJ2
Postupne pripaja dalsie a dalsie bloky
#### h3 = h2 + UDAJ3

## NAS PROGRAM
1. Program na vkladanie dat a zverejnovanie blokov
2. Miner - program kontrolujuci bloky


