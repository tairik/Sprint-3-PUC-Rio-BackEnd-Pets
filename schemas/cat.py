from pydantic import BaseModel
from typing import List
from model.cat import Cat

class CatSchema(BaseModel):
    """ Define como um novo gato a ser inserido deve ser representado
    """
    nome: str = "Chico"
    peso: float = 3

class CatViewSchema(BaseModel):
    """ Define como um gato será retornado
    """
    id: int = 1
    nome: str = "Chico"
    peso: float = 12.50
    nem: float = 70.10

def apresenta_cat(cat: Cat):
    """ Retorna uma representação do gato seguindo o schema definido em
        CatViewSchema.
    """
    return {
        "id": cat.id,
        "nome": cat.nome,
        "peso": cat.peso,
        "nem": cat.calcula_nem(),
    }

class ListagemCatsSchema(BaseModel):
    """ Define como uma listagem de gatos será retornada.
    """
    cats:List[CatSchema]

class CatBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do gato.
    """
    id: int = 1

class CatDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: str

def apresenta_cats(cats: List[Cat]):
    """ Retorna uma representação do gato seguindo o schema definido em
        CatViewSchema.
    """
    result = []
    for cat in cats:
        result.append({
            "id": cat.id,
            "nome": cat.nome,
            "peso": cat.peso,
            "nem": cat.calcula_nem(),
        })

    return {"cats": result}