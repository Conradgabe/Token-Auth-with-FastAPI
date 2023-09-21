from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Person(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True)
    password = Column(String)
    # fav_movie = Column(String(100), ForeignKey("movies.id"))

    # movie = relationship("Movies", back_populates="persons")

class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64))
    protagonist = Column(String(64))
    description = Column(String(10000), nullable=True)
    series_or_movie = Column(String(64))
    genre = Column(String(64), nullable=True)
    rating = Column(Integer, nullable=True)

   # persons = relationship("Person", back_populates="movie")