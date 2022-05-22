from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from models.user import Example
from mongoengine import connect



api_keys = [
    "akljnv13bvi2vfo0b0bw"
]

API_KEY = api_keys[0]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )


app = FastAPI()

# connect(db="number", host="localhost", port=27017)

app.add_middleware(CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],)


bisection = {
    "Bisection": {
        "eq": 'f(x)=1 - \\frac{x}{\\sqrt[4]{13}}',
        "xl": 1.5,
        "xr": 2,
        "ans": 1.8988
    },
}

falsepotion = {
    "Falsepotion": {
        "eq": 'f(x)={ x}^{3}- x-1',
        "xl": 1,
        "xr": 2,
        "ans": 1.3247
    },
}

onepoint = {
    "Onepoint": {
        "eq1": "f(x)=2~{ x}^{3}-2~ x-5",
        "eq2": "f(x)={\\left(\\frac{\\left(2~ x+5\\right)}{2}\\right)}^{\\left(\\frac{1}{3}\\right)}",
        "ans": 1.6005
    },
}

secant = {
    "Secant": {
        "eq": 'f(x)={ x}^{3}+2~{ x}^{2}+ x-1',
        "x1": 0,
        "x2": 1,
        "ans": 0.6823
    },
}

newraph = {
    "Newraph": {
        "eq": 'f(x)={ x}^{3}+2~{ x}^{2}+ x-1',
        "x0": 0,
        "ans": 0.4655
    },
}


@app.get('/api')
def root():
    return {"msg": "hello worlwd"}


@app.get('/req/api/key')
def genAPIkey():
    return api_keys


@app.get('/bisection/')
def Bisection(token: str = None):
    if token not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
    else:
        return bisection


@app.get('/falsepotion/')
def Falseposition(token: str = None):
    if token not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
    else:
        return falsepotion


@app.get('/onepoint/')
def Onepoint(token: str = None):
    if token not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
    else:
        return onepoint


@app.get('/secant/')
def Secant(token: str = None):
    if token not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
    else:
        return secant


@app.get('/newraph/')
def Newraph(token: str = None):
    if token not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )
    else:
        return newraph
