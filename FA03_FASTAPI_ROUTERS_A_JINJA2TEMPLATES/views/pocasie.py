import fastapi

from models.location import Location, DajSiMikinu
import httpx

router = fastapi.APIRouter()

mesta= {
    'Bratislava':{'lat': 48.08, 'lon': 17.06},
    'Kosice':{'lat': 48.69, 'lon': 21.098}
}

@router.get('/api/pocasie', response_model=DajSiMikinu)
async def pocasie(location: Location = fastapi.Depends()):
    if location.mesto in mesta.keys():
        print('MESTO NAJDENE')
        lat, lon = float(), float()
        lat = mesta[location.mesto]['lat']
        lon = mesta[location.mesto]['lon']
        print(lat, lon)
    else:
        return {'msg':'take mesto nepoznam'}

    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

        data = response.json()
        print(type(data), data)

        temp = data['current_weather']['temperature']
        if temp > 23:
            daj_si_mikinu = False
        else:
            daj_si_mikinu = True


    return {'daj_si_mikinu': daj_si_mikinu, 'temp': temp}



