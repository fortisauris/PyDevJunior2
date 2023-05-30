
from fastapi import FastAPI, HTTPException, status  #
import uvicorn   # pouzijeme tento server na spustanie
from pydantic import BaseModel, Field  #
from typing import Optional  #  aby polozky mohli byt volitelne
from datetime import date


app = FastAPI(debug=True)  # context -

# MOCK DATABAZY
auta_db = {
    'Octavia':{'nazov': 'Octavia', 'vyrobca': 'SKoda', 'datum_vyroby':'1998-10-04', 'miesto':'Malacky'},
    'A4quattro':{'nazov': 'A4quattro', 'vyrobca': 'Audi', 'datum_vyroby':'2005-10-04', 'miesto':'Kosice'},
    'MX5':{'nazov': 'MX5', 'vyrobca': 'Mazda', 'datum_vyroby':'2003-10-04', 'miesto':'Trencin'}
}

# M O D E L S
class Auto(BaseModel):
    nazov: str = Field(min_length=3, max_length=20)
    vyrobca: Optional[str] = None
    datum_vyroby: Optional[date] = None
    miesto: Optional[str] = None

class AutoNew(Auto):
    palivo: Optional[str] = None
    farba: Optional[str] = None

def check_if_auto_existuje(auto: str):
    if auto not in auta_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='AUTO NEEXISTUJE')

# VIEWS
@app.get('/')
def index():
    return {'msg': 200}

# TODO Doplnit metodu...

@app.get('/auta/{auto}')
def get_auto(auto: str):
    try:
        return auta_db[auto]
    except KeyError:
        raise HTTPException(status_code=404, detail=f'AUTO {auto} SA NENASLO V DATABAZE')

@app.get('/auta')
def zoznam_aut(q: str = None, limit: int = 20):
    if q:  # je nejaka otazka na nasu db v GET requeste
        result = list()  # sprav cisty zoznam
        for a in auta_db.keys():  # chod po vsetkych autach
            print(auta_db[a].values())  # vypisovanie do konzoly
            if q in auta_db[a].values():  # ked sa najde kdekolvek v databaze tak
                result.append(auta_db[a])  # pridaj auto do vypisu
        return result[:limit]  # vrat json s vybranymi autami max 20 zaznamov
    else:
        zoznam = list(auta_db.values())  # sprav zoznam vsetkych aut
        return zoznam[:limit]  # vrat json so vsetkymi autami max 20 zaznamov


@app.post('/auta')
def create_auto(auto: AutoNew):
    nazov = auto.nazov
    auta_db[nazov] = auto.dict()
    return {'msg': f'AUTO {nazov} BOLO PRIDANE DO DATABAZY'}


@app.delete('/auta/{auto}')
def vymaz_auto(auto: str):
    check_if_auto_existuje(auto)
    del auta_db[auto]
    return {'msg': f'Auto {auto} bolo vymazane z databazy' }

@app.put('/auta')
def update_auto(auto: AutoNew):
    nazov = auto.nazov
    check_if_auto_existuje(nazov)
    auta_db[nazov] = auto.dict()
    return {'msg': f'Auto {nazov} bolo pozmenene'}


@app.patch('/auta')
def patch_auto(auto: AutoNew):
    nazov = auto.nazov
    check_if_auto_existuje(nazov)
    print(type(auto.dict(exclude_unset=False)))
    prepared_auto = auto.dict(exclude_unset=False)
    auta_db[nazov].update(prepared_auto)  # TODO Domaca uloha NAJST CHYBU V PATCH
    return {'msg': f'Auto {nazov} bolo patchnute'}

if __name__ == '__main__':
    uvicorn.run(app)

