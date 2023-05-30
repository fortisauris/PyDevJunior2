from fastapi import FastAPI, HTTPException, status
import uvicorn
import requests

app = FastAPI(debug=True)

BTCUSD = []

@app.get('/')
def index():
    '''
    Tato route nam len ukazuje ze nasa API je pripravena komunikovat
    :return: None
    '''
    return {'msg': 'VSETKO JE OK'}

@app.get('/usd2btc')
def USD_current_price():
    re = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if re.status_code == 200:
        data = re.json()
        USDATA = data['bpi']['USD']
        BTCUSD.append({'key':USDATA['rate']})
        return {'key':USDATA['rate']}
    else:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='DATA NOT FOUND')

@app.get('/gbp2btc')
def GBP_current_price():
    re = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if re.status_code == 200:
        data = re.json()
        GBDATA = data['bpi']['GBP']
        # BTCUSD.append({'key':GBDATA['rate']})
        return {'key':GBDATA['rate']}
    else:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='DATA NOT FOUND')


@app.get('/eur2btc')
def EUR_current_price():
    re = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if re.status_code == 200:
        data = re.json()
        EURDATA = data['bpi']['EUR']
        # BTCUSD.append({'key':EURDATA['rate']})
        return {'key':EURDATA['rate']}
    else:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='DATA NOT FOUND')


# TODO Prestavka do 20:00

if __name__ == '__main__':
    uvicorn.run(app)