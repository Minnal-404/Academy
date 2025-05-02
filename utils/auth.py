from pydantic_settings import BaseSettings
import jwt

import bcrypt
from fastapi import Request,HTTPException, status
from sqlmodel import select
from modules.users.user_models import UserDAO
from datetime import datetime, timedelta, timezone



Algorithm='HS256'
class Secret_key(BaseSettings):
    secret_key:str
    class Config:
        env_file = ".env"
secret_key=Secret_key()
def jwt_token_encrypt(UserDetial, expires_delta: timedelta = timedelta(days=1)):
    expire = datetime.now(timezone.utc) + expires_delta

    payload={
        "email":UserDetial.email,
        "exp": expire,
        "iat": datetime.now(timezone.utc)
    }
    token=jwt.encode(payload,secret_key.secret_key,algorithm=Algorithm)
    
    return token

def jwt_token_decrypt(jwt_token):
    try:
        payload = jwt.decode(jwt_token, secret_key.secret_key, algorithms=[Algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

def authenticate(request: Request):
    from modules.users.user_validator import UserValidator
    UserValidator.validate_request(request)
    bearer_token=request.headers.get("Authorization")
    jwt_token=bearer_token.split(" ")[1]
    payload=jwt_token_decrypt(jwt_token)
    email=payload["email"]
    user = UserDAO.get_user_by_email(email)
    return user

def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(password: str, stored_hashed_password: str):
    return bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password)

