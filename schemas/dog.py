from pydantic import BaseModel
from typing import List
from model.dog import Dog

class DogSchema(BaseModel):
    """ Define como um novo cão a ser inserido deve ser representado
    """
    nome: str = "Fluffy"
    peso: float = 4.50
    raca: str = "Pastor"

class DogViewSchema(BaseModel):
    """ Define como um cão será retornado
    """
    id: int = 1
    nome: str = "Fluffy"
    peso: float = 4.50
    nem: float = 70.10
    raca: str = "Pastor"

def apresenta_dog(dog: Dog):
    """ Retorna uma representação do cão seguindo o schema definido em
        DogViewSchema.
    """
    return {
        "id": dog.id,
        "nome": dog.nome,
        "peso": dog.peso,
        "nem": dog.calcula_nem(),
        "raca": dog.raca,
    }

class ListagemDogsSchema(BaseModel):
    """ Define como uma listagem de cães será retornada.
    """
    dogs:List[DogSchema]

class DogBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do dog.
    """
    id: int = 1

class DogDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: str

def apresenta_dogs(dogs: List[Dog]):
    """ Retorna uma representação do cão seguindo o schema definido em
        DogViewSchema.
    """
    result = []
    for dog in dogs:
        result.append({
            "id": dog.id,
            "nome": dog.nome,
            "peso": dog.peso,
            "nem": dog.calcula_nem(),
            "raca": dog.raca,
        })

    return {"dogs": result}