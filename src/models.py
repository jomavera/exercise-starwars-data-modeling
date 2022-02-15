import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

favorites_people = Table('user_favorites_people', Base.metadata,
    Column('left_id', ForeignKey('user.uid'), primary_key=True),
    Column('right_id', ForeignKey('people.uid'), primary_key=True)
)

favorites_planets = Table('user_favorites_planets', Base.metadata,
    Column('left_id', ForeignKey('user.uid'), primary_key=True),
    Column('right_id', ForeignKey('planet.uid'), primary_key=True)
)
class User(Base):
    __tablename__ = 'user'
    uid = Column(Integer, primary_key = True)
    username = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    child1 = relationship(
        "PeopleFavorites",
        secondary=favorites_people,
        back_populates="parents")
    child2 = relationship(
        "PlanetsFavorites",
        secondary=favorites_planets,
        back_populates="parents")

class People(Base):
    __tablename__ = 'people'
    uid = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    gender = Column(String(10),nullable=True)
    eye_color = Column(String(10), nullable=True)
    hair_color = Column(String(10), nullable=True)
    skin_color = Column(String(10), nullable=True)
    birth_year = Column(String(20), nullable=True)
    height = Column(Integer)
    mass = Column(Integer)
    homeworld_uid = Column(Integer, ForeignKey('plantet.uid'))
    url = Column(String(250),nullable=False)
    parent = relationship(
        "User",
        secondary=favorites_people,
        back_populates="parents"
    )

class Planet(Base):
    __tablename__ = 'planet'
    uid = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    climate = Column(String(20))
    terrain = Column(String(20),nullable=True)
    population = Column(Integer, nullable=True)
    surface_water = Column(Integer)
    gravity = Column(Integer)
    url = Column(String(250),nullable=False)
    parent = relationship(
        "User",
        secondary=favorites_planets,
        back_populates="parents"
    )


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')