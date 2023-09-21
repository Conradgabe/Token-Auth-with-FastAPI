from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True

# Database schema for Movie model
class MovieBaseCreate(BaseModel):
    title: str
    protagonist: str
    description: str
    series_or_movie: str
    genre: str
    rating: int

    class Config:
        from_attributes = True
