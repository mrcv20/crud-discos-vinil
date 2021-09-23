from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from . import Base

class Artist(Base):
    __tablename__ = "artista"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(20))
    dt_nascimento = Column(String(50))
    
    

class VinylDisc(Base):
    __tablename__ = "discos"

    id = Column(Integer, primary_key=True, index=True)
    genero = Column(String(20))
    titulo = Column(String(50))
    valor = Column(Float)
    