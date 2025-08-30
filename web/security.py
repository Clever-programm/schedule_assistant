from datetime import timedelta, datetime, UTC
from os import getenv

from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt


load_dotenv()
SECRET_KEY = getenv("JWT_SECRET_KEY")
ALGORITHM = getenv("JWT_ALGORYTHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class Token(BaseModel):
    access_token: str
    token_type: str

class UserData(BaseModel):
    username: str

def create_access_token(data: dict, expires_delta: timedelta | None = timedelta(minutes=15)) -> str:
    to_encode = data.copy()
    expire = datetime.now(UTC) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return UserData(username=username)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")