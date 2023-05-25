# GIT kolaboracia

Vytvorime repozitar na githube
MAJITEL repozitara prida ludi, s ktorymi chceme spolupracovat na projekte.

### !!! POZOR Ludia to musia odsuhlasit !!!

Repozitar si mozeme naklonovat na lokalnu masinu

POSTUP PRE SPOLUPRACOVNIKOV>

1. Najprv spravime PULL aby sme mali najcerstvejsiu verziu

git pull

2. Vytvorime vlastnu vetvu {akokeby paralelnu kolaj}

git checkout -b uprava_sifrovacieho_algoritmu

3. Programujeme ako o zivot
4. Zistime co sme pomenili

git status

5. Pridame zmeny do pripraveneho commitu

git add *

6. Spravime commit na lokalnej masine

git commit -m 'upravil som algoritmus sifrovania'

7. Poslem commit pomocou git push na github do mojej vetvy.

## !!! POZOR NIKDY NEROBTE PUSH DO VETVY **main**

git push origin uprava_sifrovacieho_algoritmu

8. Prejdem do browseru a skontrolujem ci vetva vznikla

9. Vytvorim PULL REQUEST aby som poprosil MAJITELA repozitara aby moje zmeny zlucil 
vo vetve **main**

10. Cakam na objektivnu kritiku od kolegov

11. Ak su zmeny prijate a MAJITEL nevymazal vetvu uprava_sifrovacieho_algoritmu tak ju vymazem

## !!! GRATULUJEME VAS KOD BOL PRIJATY DO PROJEKTU !!!


OPAKUJTE


## POKRACUJEME INSTALACIOU FASTAPI DO NOVEHO PROJEKTU

Budeme potrebovat:

pip.exe install fastapi, uvicorn,  pydantic

alebo

python.exe -m pip install fastapi pydantic uvicorn

# FASTAPI

Mikroframework v Pythone na rychlu tvorbu API

### API - Application Programming Interface

Aplikacne rozhranie pomocou ktoreho komunikuje s dalsim programom
alebo clovekom.

