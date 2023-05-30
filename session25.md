# SESSION25 - FASTAPI 02 a 

pokračujeme s microframeworkom FastAPI a vytvárame rozhrania
, ktoré pomocou http requestov reagujú na naše pokyny a 
požiadavky

## FastAPI POST,DELETE,PUT PATCH

``` path
FA01_POST_REQUEST_A_SERVER_UVICORN
```

Dokončenie z minulej lekcie kde sme začali robiť API pomocou
ktorej vieme vyhľadávať, prezerať našu Mock databázu motorových
vozidiel.

Pridali sme si funkciu, ktoá dokáže vypísať všetky vozidlá
z našej databázy. Funkcia však využíva ďalšiu funkcionalitu 
GET requestu a to jednoduché vyhľadávanie pomocou
q: query a zobrazuje iba max počet záznamou pomocou 
limit: Nastavené to máme na max 20 zobrazených záznamov.

Ukázali sme si tiež automatické robenie api dokumentácie na route

http://127.0.0.1:8000/docs

Pridali sme si funkciu na pridávanie vozidla pomocou http
requestu POST.

Pridali sme si funkciu na vymazávanie vozidla z databázy pomocou
http requestu DELETE


## FASTAPI - BITCOIN USD

``` path
FA02_KURZ_BITCOINU_Z_INEJ_API
```

JE POTREBNÉ NAINŠTALOVAŤ requests do virtuálnej obálky

``` powershell
pip.exe install requests
```

Pomocou requests stahujeme z inej api údaj o aktuálnom 
kurze BITCOINU voči USD, GBP a EUR.

Manipuláciu s týmito údajmi ich pripravujeme na poskytnutie 
cez našu api s troma definovanými routami. 

## FASTAPI METEO s renderovanim do HTML pomocou Jinja2templates

``` path
FA03_FASTAPI_ROUTERS_A_JINJA2TEMPLATES
```

FastApi je postavená na softvéri starlette, ktorý nám poskytuje
pokročilú manipuláciu s requestami a preto miesto requests 
využívame v ďalšom príklade starlette.

Naša appka však nebude poskytovať vústup len v jsone, ale
bude pomocou jinja2templates renderovať html, ktorý nám
umožní api ovládať v browseri.

