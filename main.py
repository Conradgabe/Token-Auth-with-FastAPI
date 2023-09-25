from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta 

from utils import (create_user, get_db, get_current_user,
                   create_access_token, authenticate_user)

from models import Base, Person, Movies
from schema import UserCreate, MovieBaseCreate
from database import SessionLocal, engine
import os

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")


# Signup to get you token
@app.post("/api/signup", description="Register with your username and password to get a token to use the API")
async def signup(user: UserCreate):
    try:
        db_user = create_user(user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Username already registered",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    key_dict = dict()

    for key, value in db_user.items():
        key_dict[key] = value

    key_dict["token_type"] = "bearer"
    return key_dict

# Login to get a new token the previous one epires
@app.post("/api/login", description="Login again to get a new token as previous token will expire", tags=['User'])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db: Session = next(get_db())

    user = authenticate_user(db, username=form_data.username, password=form_data.password)
    if not user:
        db.close()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Username and Password2")
    
    data = {
        "access_token": create_access_token(user.username),
        "token_type": "bearer"
    }

    return data

# Get all Movies in the database
@app.get("/api/movie", tags=['Movies'], description="Get all the movies and its detail")
async def get_movies(limit: int = Depends(get_current_user)):
    db: Session = next(get_db())

    return db.query(Movies).offset(0).limit(100).all()


# Add a new Movie to the database
@app.post("/api/movie", tags=['Movies'], response_model=MovieBaseCreate, description="Add your favourite movie and its detail")
async def add_movies(movie: MovieBaseCreate, sub: str = Depends(get_current_user)):
    db: Session = next(get_db())
    
    db_movie = Movies(title=movie.title, protagonist=movie.protagonist,
                       description=movie.description,series_or_movie=movie.series_or_movie,
                        genre=movie.genre, rating=movie.rating)
    
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie
