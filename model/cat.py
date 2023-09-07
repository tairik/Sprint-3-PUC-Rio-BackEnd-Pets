from sqlalchemy import Column, Integer
from model.animal import Animal
from model import Base

class Cat(Base, Animal):
    __tablename__ = 'cat'

    id = Column("pk_cat", Integer, primary_key=True)
    ##Override dos atributos da para cada classe filha
    fator_nem = 85
    fator_expoente = 0.67