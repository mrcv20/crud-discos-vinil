from flask import json, request
from tests.fixtures.context import client

def test_doc_url_deve_retornar_200_quando_rebecer_get(client):
    response = client.get('http://127.0.0.1:5000/api/v1/')
    assert response.status_code == 200


def test_doc_url_deve_retornar_405_quando_receber_post(client):
    response = client.post('http://127.0.0.1:5000/api/v1/')    
    assert response.status_code == 405


def test_endpoint_artistas_deve_retornar_404_no_primeiro_get(client):
    response = client.get('http://127.0.0.1:5000/api/v1/artistas/')
    assert response.status_code == 404


def test_endpoint_discos_deve_retornar_404_no_primeiro_get(client):
    response = client.get('http://127.0.0:5000/api/v1/discos/')
    assert response.status_code == 404


def test_post_no_endpoint_artistas_deve_retornar_201_ao_criar_artista(client):
    response = client.post('http://127.0.0.1:5000/api/v1/artistas/',
    json={
        "artista": "new_artista"
    })
    assert response.status_code == 201


def test_post_no_endpoint_artistas_deve_retornar_400_quando_enviar_json_com_chaves_incorretas(client):
    response = client.post('http://127.0.0.1:5000/api/v1/artistas/',
    json={
        "artistwa": "new_artista"
    })
    assert response.status_code == 400


def test_post_no_endpoint_artistas_deve_retornar_409_ao_criar_artista_existente(client):
    response = client.post('http://127.0.0.1:5000/api/v1/artistas/',
    json={
        "artista": "new_artista"
    })
    assert response.status_code == 409


def test_put_no_endpoint_artistas_deve_retornar_200_ao_atualizar_artista_pelo_id(client):
    response = client.put('http://127.0.0.1:5000/api/v1/artistas/1',
    json={
        "artista": "new_artista_updated"
    })
    assert response.status_code == 200


def test_post_no_endpoint_discos_deve_criar_disco_e_retornar_201_e_successfully_saved_quando_payload_for_valido(client):
    response = client.post('http://localhost:5000/api/v1/discos/', 
    json={
        "titulo": "Titulo inventado",
        "genero": "Rock",
        "valor": 100.0,
        "id_artista": 1
    })
    assert response.status_code == 201
    assert b'Successfully saved' in response.data 


def test_put_no_endpoint_discos_deve_atualizar_e_retornar_200_e_successfully_updated_quando_payload_for_valido(client):
    response = client.put('http://localhost:5000/api/v1/discos/1', 
    json={
        "titulo": "Titulo inventado atualizado",
        "genero": "Pop",
        "valor": 150.0,
        "id_artista": 1
    })
    assert response.status_code == 200
    assert b'Successfully disc updated' in response.data 


def test_post_no_endpoint_discos_deve_retornar_400_e_error_msgs_quando_enviar_payload_invalido(client):
    response = client.post('http://localhost:5000/api/v1/discos/', 
    json={
        "titulo-errado": "Titulo inventado",
        "genero-errado": "Rock",
        "valor-errado": 101.0,
        "id_artista-errado": 1
    })
    assert response.status_code == 400
    assert b'"Input payload validation failed"' in response.data

def test_get_no_endpoint_artistas_deve_retornar_200_quando_houver_artistas_na_base_de_dados(client):
    response = client.get('http://localhost:5000/api/v1/artistas/')
    assert response.status_code == 200


def test_get_no_endpoint_discos_deve_retornar_200_quando_houve_discos_na_base_de_dados(client):
    response = client.get('http://localhost:5000/api/v1/artistas/')
    assert response.status_code == 200


def test_delete_no_endpoint_discos_deve_retornar_200_ao_deletar_disco_pelo_id(client):
    response = client.delete('http://localhost:5000/api/v1/discos/1')
    assert response.status_code == 200


def test_delete_no_endpoint_artistas_deve_retornar_200_ao_deletar_artista_pelo_id(client):
    response = client.delete('http://127.0.0.1:5000/api/v1/artistas/1')
    assert response.status_code == 200
    assert b'Deleted'

