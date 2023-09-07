# Pets API

Este pequeno projeto faz parte do MVP do curso de Pós-Gradução em **Engenharia de Software** 

O crescimento do número de cães e gatos em estado de sobrepeso e obesos tem sido uma grande preocupação para Médicos Veterinários especializados em Nutrição e Nutrologia Veterinária que usam tabelas de determinação de Escore de Condição Corporal (ECC).

O produto desenvolvido tem como objetivo facilitar os cálculos de necessidades calóricas destes indivíduos para que o Plano Alimentar seja determinado, caso a caso.

No caso dos cães, o produto irá determinar a taxa de perda de peso em percentagem pois a equação irá utilizar o peso desejado que será calculado de acordo com cada estado no qual o mesmo se encontrar (6 e 7, no sobrepeso; 8 e 9, no obeso). 

Sabendo-se que cada um ponto acima ECC ideal (5) significa 15% a mais de peso, o programa irá utilizar essa informação para determinar a necessidade calórica de cada paciente. 

Para isso é necessário o cálculo do NEM (Necessidade energética de manutenção).

A fórmula para cada animal difere, sendo estabelecida da seguinte forma:

1) cães: NEM = 70 * PC ^ 0.75
2) felinos: NEM 85 x PC ^  0,67
 
Onde PC = Peso Corporal do Animal.

Para a execução do projeto, foram implementados os Endpoint's para a criação / deleção dos pets (dogs/cats). 
Além disso, a ideia foi extender o conceito de orientação a objetos criando uma classe acima das classes dog/cat, chamada de classe Animal.
Desta forma, podemos usar o conceito de herança múltipla, já que as classes dog/cat herdam das classes Base + Animal.

Também como solicitado, foi utilizado o Banco de Dados SQLite.

Por fim, para a documentação da API, foi usado Swagger.
---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

## Docker

docker build --tag api-pet-docker . 

docker run -d --name api-pet-docker -p 5000:5000 api-pet-docker

## Execução local

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenpython -m venv .v.pypa.io/en/latest/).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta lançar o seguinte comando no terminal:

```
(env)$ flask run --host 0.0.0.0 --port 4000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 4000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:4000/#/) no navegador para verificar o status da API em execução.

