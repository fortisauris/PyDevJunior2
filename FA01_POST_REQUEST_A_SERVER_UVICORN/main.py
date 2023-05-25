
from fastapi import FastAPI, HTTPException, status
import uvicorn
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


app = FastAPI(debug=True)

# MOCK DATABAZY - V PRODUKCII TU BUDE DATABAZA NA DB SERVERI
auta_db = {
    'Octavia':{'typ': 'Octavia', 'vyrobca': 'SKoda', 'datum_vyroby':'1998-10-04', 'miesto':'Malacky'},
    'A4quattro':{'typ': 'A4quattro', 'vyrobca': 'Audi', 'datum_vyroby':'2005-10-04', 'miesto':'Kosice'},
    'MX5':{'typ': 'MX5', 'vyrobca': 'Mazda', 'datum_vyroby':'2003-10-04', 'miesto':'Trencin'}
}

# M O D E L S  - Objekty v databaze a ktore polozky obsahuju
class Auto(BaseModel):
    '''
    Zakladna trieda objektu v databaze dediaca metody a parametre od BaseModel klasy
    '''
    nazov: str = Field(min_length=3, max_length=20)
    vyrobca: Optional[str] = None  # optional je typ, ktory moze byt aj nezadany None
    datum_vyroby: date  # objekt datetime.date
    miesto: str

class AutoNew(Auto):
    palivo: str = Field(min_length=6)  # pridame parametre do existujuceho modelu
    farba: Optional[str] = 'cierna'

def check_if_auto_existuje(auto: str):
    '''
    Jednoducha funkcia, ktora nam kontroluje ci sa v databaze nachadza vozidlo
    '''
    if auto not in auta_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='AUTO NEEXISTUJE')

# VIEWS
@app.get('/')
def index():
    '''
    zakladna route, ktora nam vrati kod 200 a povie nam ze nasa API funguje
    '''
    return {'msg': 200}

# TODO Doplnit metodu...

@app.get('/auta/{auto}')
def get_auto(auto: str):
    '''
    jednoducha route ktora nam umozni najst vozidlo z databazy  vracia json
    '''
    try:
        return auta_db[auto]
    except KeyError:
        raise HTTPException(status_code=404, detail=f'AUTO {auto} SA NENASLO V DATABAZE')

@app.post('/auta')
def create_auto(auto: AutoNew):
    '''
    Route ktora nam umozni pridat auto pomocou API odhocikial na svete do nasej databazy
    '''
    nazov = auto.nazov
    auta_db[nazov] = auto.dict()
    return {'msg': f'AUTO {nazov} BOLO PRIDANE DO DATABAZY'}

if __name__ == '__main__':
    uvicorn.run(app)

'''
Vyhoda FASTAPI je ze nam robi automaticky dokumentaciu na route /docs

'''