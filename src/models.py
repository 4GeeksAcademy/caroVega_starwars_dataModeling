import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False )
    climate = Column(String(100))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)



class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False )
    model = Column(String(100))
    manufacturer = Column(String(100))
    max_atmosphering_Speed = Column(Integer)
    cargo_Capacity = Column(Integer)
    

class Characters(Base):
    __tablename__ = 'characters'
        # Here we define columns for the table address.
        # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False )
    gender = Column(String(100))
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    Birth_Year = Column(String(100))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships = relationship(Starships)                  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
