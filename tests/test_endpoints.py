from flask import json, request
from app.config import TestingConfig
import pytest
from app.run import app


@pytest.fixture
def client():
    """
    initialize a context for testing and initialize a database
    
    """
    with app.app_context():
        with app.test_client() as client:
            yield client


def test_for_sucessfully_api_doc(client):
    response = client.get('http://127.0.0.1:5000/api/v1/')
    response.status_code = 200
    assert b'Loja de discos de vinil' in response.data 


def test_for_not_allowed_api_doc(client):
    response = client.post('http://127.0.0.1:5000/api/v1/')    
    assert response.status_code == 405
    assert b'The method is not allowed for the requested URL' in response.data


def test_for_sucessfully_payload_post(client):
    response = client.post('http://localhost:5000/api/v1/discos/', 
    json={
        "titulo": "string",
        "genero": "string",
        "valor": 0.0,
        "id_artista": 1
    })
    assert response.status_code == 201
    assert b'Dados salvos com sucesso' in response.data 

def test_for_sucessfully_get_all_disc(client):
    response = client.get('http://localhost:5000/api/v1/discos/')
    assert response.status_code == 200

def test_for_sucessfuly_update_disc(client):
    response = client.put('http://localhost:5000/api/v1/discos/1',
    json={
        "titulo": "new_string",
        "genero": "new_string",
        "valor": 0.0,
    })
    assert response.status_code == 200


def test_for_sucessfully_delete_disc(client):
    response = client.delete('http://localhost:5000/api/v1/discos/1')
    assert response.status_code == 200
    assert b'Deletado!' in response.data