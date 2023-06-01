from fastapi import FastAPI, Depends
from fastapi_login import LoginManager
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

import os
import uvicorn

app = FastAPI(debug=True)
SECRET = os.urandom(32)
manager = LoginManager(SECRET, token_url='/auth/token')

db = {'jozko@email.com': {'heslo': 'marienka2'}}

@manager.user_loader()
def load_user(email: str):
    user = db.get(email)
    return user

@app.post('/auth/token')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password
    user = load_user(email)
    if not user:
        raise InvalidCredentialsException
    elif password != user['heslo']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data= dict(sub=email))

    return {'access_token': access_token, 'token_type': 'bearer'}

@app.get('/protected')
def protected(user=Depends(manager)):
    return {'data': 200}
