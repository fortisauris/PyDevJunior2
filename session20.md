# SESSION20 - GIT, PRVA FLASK APPKA

## GIT cez príkazový riadok

Je vyhodne spravit prvy repozitar na github.com cez web a potom
ho naklonovat.

### zistenie stavu zmien repozitára

<code>
git status
</code>

### pridanie zmien do nasledujäceho balíčka zmien == commitu

<code>
git add *
</code>

POZOR HVIEZDICKA ZNAMENA PRIDAT VSETKO- MOZETE VSAK PRIDAT AJ SELEKTIVNE

### Zabalenie balicka (commitu) zmien na odoslanie
<code>
git commit -m 'komentare co bolo urobene'
</code>

### Poslanie balicka -- PUSH
<code>
git push
</code>



# Úvod do webaplikacií pomocou frameworku Flask

Po skúsenostiach s PyQt vieme, že dokážeme v Pythone spraviť aplikáciu
s vlastným grafickým interfejsom. No inštalovanie na počítač našeho užívateľa
nie je pre laika jednoduché a je potrebné spraviť viacero krokov.

1. nainštalovať správnu verziu pythona
2. naklonovať kód z githubu alebo stiahnuť cez pip
3. nainštalovať všetky súvisiace moduly, knižnice a frameworky = Dependencies
4. Spustiť program cez konzolu :)

TO EŤE NEMÁME ISTOTU ČI AKO TO BUDE BEŽAŤ NA JEHO ULTRAMODERNOM
ALEBO STARUČKOM POČÍTAČI


Bolo by oveľa jednoduchšie keby naša aplikácia bežala na webserveri.
Náš užívateľ by sa pripájal na ňu cez svoj browser a vôbec
by netušil, že to je python.

# Flask - voľným prekladom Flaška :)

Ultralight framework, ktorý z našej aplikácie spraví webserver
a dáta z Pythonu bude prezentovať na diaľku priamo do užívateľovho 
webrowsera pomocou HTML.

1. všetko beží na našom odladenom hardvéri
2. nič sa nemusí inštalovať
3. server odpovedá na requesty
4. appka má pekný frontend a je dostupná aj pre Eskimákov.

# Prvá Appka sa nachádza v adresári 

<code>
FL01
</code>

a spúštame tzv. Entry Point je:

<code>
FL01/app.py
</code>