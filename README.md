
# Rest API

## Sobre

API com endpoints CRUD de uma loja de discos

Tecnologias:
- Python
- Flask
- MySQL
- SQLite3


## Requisitos de sistema
  python 3, MySQL Server/SQLite3

## Preparando o ambiente virtual
Na pasta raiz digite os comandos
```
pip install virtualenv

virtualenv ./env

source env/bin/activate
```

## Instalando as dependências
No diretório app, instale as bibliotecas com o pip
```
pip install -r requirements.txt
```

## Rodando os testes
No diretório app, digite os comandos:

```
export FLASK_ENV=testing
pytest -v tests/test_endpoints.py
```

## Criação das tabelas e do banco de dados
```
A criação das tabelas é feita automaticamente puxando um contexto, assim que subimos a API
```

## Subindo a API
```
export FLASK_APP=app/run.py
export FLASK_ENV=development
flask run
```

- Endereço da documentação: http://localhost:5000/api/v1/

