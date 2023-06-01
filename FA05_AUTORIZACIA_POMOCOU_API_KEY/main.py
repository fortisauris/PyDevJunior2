from fastapi import FastAPI, Depends, Form
from fastapi_simple_security import api_key_router, api_key_security
import os
import uvicorn

app = FastAPI(debug=True)
os.environ['FASTAPI_SECURITY_SECRET'] = 'BRYNDZOVEHALUSKY'

db = {
    'tajomstvo1': {'heslo k wifi': 'halabala'},
    'tajomstvo2': {'pin ku karte': 1111}
}
'''
@app.post('/login')
def login(username: str = Form(), password: str = Form()):
    return {'username': username, 'password': password}
'''

app.include_router(api_key_router, prefix='/auth', tags=['auth'])

@app.get('/secured/{tajomstvo}', dependencies=[Depends(api_key_security)])
async def secure_endpoint(tajomstvo: str = None):
    if tajomstvo:
        return db[tajomstvo]
    return {'msg':'TOTO JE ZABEZPECENA STRANKA !!!'}


if __name__ == '__main__':
    uvicorn.run(app)