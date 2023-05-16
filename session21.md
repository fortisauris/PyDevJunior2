# SESSION20 - FLASK DRUHA APPKA a PRIPOJENIE POMOCOU ssh na REMOTE SERVER


## FLASK POST REQUEST

Súčasťou POST requestu je tzv. PAYLOAD, ktorý obsahuje dáta užívateľa
smerujúce na náš Server.

Vňčšinou sa posielajú na server pomocou formulára v HTML

Prvý formulár sme vytvorili pomocou HTML tagov, input a label

V druhej aplikácii ho však budeme vytvárať pomocou triedy
MojFormular() a renderovať pomocou Jinja2

### WTForms

Budeme na to potrebovať doinštalovať do obálky WTF_FORMS

pomocou PyCharmu alebo príkazového riadku cez pip

<code>
pip install WTForms
</code>

Tieto nám umožnia spraviť model formulára a priamo vo funkcií
s route ho vyrenderovať na určenej stránke.

Dáta vieme načítať z formulára do Pythonu a uložiť do zoznamu

Tento zoznam sa však vymaže pri každom reštarte servera

### Validacia Formulara

Okrem toho môžeme nastaviť Validátory, ktoré kontrolujú obsah polí
formulára a nedovolia ho poslať keď je prázdny


### Riešime tiež základnú ochranu proti CSRF
 
Cross SIte Request Forgery = 
je to útok v ktorom útočník
sfalšuje obsah formulára a pokúša sa obalamutiť usera a náš server.

Zhrabne napríklad dáta z falošného formulára a potom nič netušiaceho
užívateľa presmeruje na pravý server.

Aby k tomu nemohlo dojsť, generujeme csrf token... kryptoretazec,
ktorý keď nesedí tak server vie, že došlo k manipulácii
s formulárom a upozorní na to obe strany. 


## SSH - Secure Shell

Vytvorí šifrovaný tunel na REMOTE server a umožní nám ho ovládať pomocou
príkazového riadku.


Počítače si musia vymeniť šifrovacie kľúče a zároveň uložiť, že sa poznajú

ssh USER@IP

zadáme heslo - HESLO NEVIDIME (ochrana)

Objaví sa nám meno užívateľa a počítača. Môžeme zadávať príkazy iba v rozsahu
svojich povolení PERMISSIONS

### Základné príkazy:
<code>
ls = list
mkdir MENOADRESARA = vytvori novy adresar  <br>
cd MENOADRESARA = PREJDE DO ADRESARA  <br>
cd .. = vyskoci z adresara o uroven vyssie  <br>
cat MENOSUBORU  = vypise obsah suboru  <br>
nano MENOSUBORU = spusti editor kde mozeme pisat programy Ctrl X odideme  <br>
python3 menoscriptu.py = spusti program v pythone3  <br>
</code>



