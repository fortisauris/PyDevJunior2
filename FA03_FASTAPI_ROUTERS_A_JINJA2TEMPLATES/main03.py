import fastapi
import uvicorn
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from views import nasa_stranka
from views import pocasie

app = fastapi.FastAPI(debug=True)

app.include_router(nasa_stranka.router)
app.include_router(pocasie.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
