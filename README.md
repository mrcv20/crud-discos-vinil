
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

## Iniciando um ambiente virtual
```
pip install virtualenv

python3 -m venv env

source env/bin/activate
```


## Instalando as dependências
```
pip install -r requirements.txt
```

## Criação das tabelas e do banco de dados
```
A criação das tabelas é feita automaticamente puxando um contexto
```

## Subindo a API
```
export FLASK_APP=app/run.py
export FLASK_DEBUG=True
export FLASK_ENV=development
flask run
```

- Endereço da documentação: http://localhost:5000/api/v1/

