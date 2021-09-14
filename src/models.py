import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'
    mail = Column(String(50), primary_key=True)
    user_name = Column(String(50), ForeignKey("listafavoritos.id"))
    password = Column(String(50))
    relasionUser = relationship("ListaFavoritos")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50))
    height = Column(Integer)
    mass = Column(Float)
    homeworld = Column(String(50), ForeignKey("planeta.name"))
    
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(50))
    relacionPersonaje = relationship("Personaje")

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    pilot_uid = Column(String(50), primary_key=True)
    name = Column(String(50), ForeignKey("personaje.name"), nullable=False)
    relacionVehiculo = relationship("Personaje")
      
class ListaFavoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    mail_usuario = Column(String(50), ForeignKey("usuario.mail"))
    Personaje = Column(String(50) ForeignKey("personaje.name"))
    Planeta = Column(String(50) ForeignKey("planeta.name"))
    Vehiculo = Column(String(50) ForeignKey("planeta.name"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')