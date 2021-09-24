from flask import json, request
import pytest
from app.run import app


@pytest.fixture
def client():
    with app.app_context():
        with app.test_client() as client:
            yield client

def test_for_sucessfully_api_doc(client):
    response = client.get('http://127.0.0.1:5000/api/v1/')
    assert b'API' in response.data 


def test_for_not_allowed_api(client):
    response = client.post('http://127.0.0.1:5000/api/v1/')    
    assert b'The method is not allowed for the requested URL' in response.data


def test_for_sucessfully_payload_post(client):
    response = client.post('http://localhost:5000/api/v1/disco-registra', 
    json={"titulo": "string",
    "genero": "string",
    "valor": 0.0,
    "artista": "string"})
    assert b'Dados inseridos!' in response.data 


# def test_for_not_allowed_payload_get(client):
#     response = client.get('http://127.0.0.1:5000/api/v1/credito/',
#     json={"CPF": "string",
#     "idade": 18,
#     "nome": "marcos",
#     "valor_solicitado": 1000})
#     assert b'The method is not allowed for the requested URL' in response.data
