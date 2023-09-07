from sqlalchemy import Column, Integer
from model import Base
from model.animal import Animal

class Dog(Base, Animal):
    __tablename__ = 'dog'

    id = Column("pk_dog", Integer, primary_key=True)
    ##Override dos atributos da para cada classe filha
    fator_nem = 70
    fator_expoente = 0.75



