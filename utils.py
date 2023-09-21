import os
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
from typing import Optional

from models import Person
from database import SessionLocal
from schema import UserCreate

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new user and generate a token
def create_user(user: UserCreate):
    db: Session = next(get_db())

    existing_user = db.query(Person).filter(Person.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Username in DB", 
                            headers={"WWW-Authenticate": "Bearer"})
    else:
        try:
            hashed_pwd = get_password_hash(user.password)
            db_user = Person(username=user.username, password=hashed_pwd)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)

            payload = {
                "username": db_user.username, 
                "access_token": create_access_token(sub=db_user.username)
            }
        except:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Format")
        
        return payload

# verify users password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# hash the password
def get_password_hash(password):
    return pwd_context.hash(password)
    

# authenticate user
def authenticate_user(db: Session, username: str, password: str) -> Optional[Person]:
    user = db.query(Person).filter(Person.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

# generate token
def create_access_token(sub: str):
    expires = datetime.utcnow() + timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))

    payload = dict()

    payload["type"] = "bearer"
    payload["exp"] = expires
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)

    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# get the current user and decode token
def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    db: Session = next(get_db())

    try:
        payload = verify_token(token=token)
        username: str = payload.get("sub")
    except JWTError:
        raise credentials_exception
    
    user = db.query(Person).filter(Person.username == username).first()
    if user is None:
        raise credentials_exception
    return {"id": user.id, "username": user.username}

# Decode Token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return payload
