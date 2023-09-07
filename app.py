from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Dog, Cat
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="PetDiet Pets API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
dog_tag = Tag(name="Dog", description="Adição, visualização e remoção de Cães à base")
cat_tag = Tag(name="Cat", description="Adição, visualização e remoção de Gatos à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

## Sistema PetDiet
##Rotas para os Dogs
@app.post('/dog', tags=[dog_tag],
          responses={"200": DogViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_dog(body: DogSchema):
    """Adiciona um novo cão à base de dados

    Retorna uma representação dos cães.
    """
    data = request.json

    dog = Dog(
        nome=data.get('nome'),
        peso=data.get('peso'),
        raca = data.get('raca'))
    logger.debug(f"Adicionando dog de nome: '{dog.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando cão
        session.add(dog)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado Cão de nome: '{dog.nome}'")
        return apresenta_dog(dog), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cão de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar cão '{dog.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cão '{dog.nome}', {error_msg}")
        return {"message": error_msg}, 400

@app.delete('/dog', tags=[dog_tag],
            responses={"200": DogDelSchema, "404": ErrorSchema})
def del_dog(query: DogBuscaSchema):
    """Deleta um cão a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    dog_id = query.id
    print(dog_id)
    logger.debug(f"Deletando dados sobre o cão: #{dog_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Dog).filter(Dog.id == dog_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado o cão: #{dog_id}")
        return {"message": "Cão deletado", "id": dog_id}
    else:
        # se o cão não foi encontrado
        error_msg = "Cão não encontrado na base :/"
        logger.warning(f"Erro ao deletar o cão: #'{dog_id}', {error_msg}")
        return {"message": error_msg}, 404

@app.put('/dog', tags=[dog_tag],
            responses={"200": DogDelSchema, "404": ErrorSchema})
def put_dog(body: DogViewSchema):
    """Atualiza um cão a partir do id informado

    Retorna os dados do cão atualizado.
    """
    dog_id = body.id

    try:
        # criando conexão com a base
        session = Session()
        # adicionando cão
        dog = session.query(Dog).filter(Dog.id == dog_id).first()
        dog.nome = body.nome
        dog.peso = body.peso
        dog.raca = body.raca
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado Cão de nome: '{dog.nome}'")
        return apresenta_dog(dog), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cão de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar cão '{dog.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cão '{dog.nome}', {error_msg}")
        return {"message": error_msg}, 400

@app.get('/dogs', tags=[dog_tag],
             responses={"200": ListagemDogsSchema, "404": ErrorSchema})
def get_dogs():
        """Faz a busca por todos os cães cadastrados

        Retorna uma representação da listagem de Cães.
        """
        logger.debug(f"Coletando dogs ")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        dogs = session.query(Dog).all()

        if not dogs:
            # se não há dogs cadastrados
            return {"dogs": []}, 200
        else:
            logger.debug(f"%d rodutos econtrados" % len(dogs))
            # retorna a representação de produto
            print(dogs)
            return apresenta_dogs(dogs), 200

##Rotas para os Cats
@app.post('/cat', tags=[cat_tag],
          responses={"200": CatViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_cat(form: CatSchema):
    """Adiciona um novo gato à base de dados

    Retorna uma representação dos gatos.
    """
    cat = Cat(
        nome=form.nome,
        peso=form.peso)
    logger.debug(f"Adicionando gato de nome: '{cat.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando cão
        session.add(cat)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado gato de nome: '{cat.nome}'")
        return apresenta_cat(cat), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Gato de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar gato '{cat.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar gato '{cat.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.delete('/cat', tags=[cat_tag],
            responses={"200": CatDelSchema, "404": ErrorSchema})
def del_cat(query: CatBuscaSchema):
    """Deleta um gato a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    cat_id = query.id
    print(cat_id)
    logger.debug(f"Deletando dados sobre o gat: #{cat_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Cat).filter(Cat.id == cat_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado o gato: #{cat_id}")
        return {"message": "Gato deletado", "id": cat_id}
    else:
        # se o gato não foi encontrado
        error_msg = "Gato não encontrado na base :/"
        logger.warning(f"Erro ao deletar o cão: #'{cat_id}', {error_msg}")
        return {"message": error_msg}, 404

@app.get('/cats', tags=[cat_tag],
         responses={"200": ListagemCatsSchema, "404": ErrorSchema})
def get_cats():
    """Faz a busca por todos os gatos cadastrados

    Retorna uma representação da listagem de gatos.
    """
    logger.debug(f"Coletando gatos")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cats = session.query(Cat).all()

    if not cats:
        # se não há dogs cadastrados
        return {"cats": []}, 200
    else:
        logger.debug(f"%d gatos econtrados" % len(cats))
        # retorna a representação de gato
        print(cats)
        return apresenta_cats(cats), 200
