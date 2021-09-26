from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from app.models import Artist, VinylDisc
from app.api.serializers import discos_schema, disco_schema, artista_schema, artistas_schema
from marshmallow import ValidationError

ns_disco = Namespace('discos', description='Disco de Vinil')
ns_artista = Namespace('artistas', description='Artistas')

dados_disco_vinil = ns_disco.model(
    'Variáveis para criação do disco', {
        'titulo': fields.String(
            required=True,
            description='Título do disco',
        ),     
        'genero': fields.String(
            description='Gênero musical disco',
            required=True
        ),
        'valor': fields.Float(
            description='Preço do disco',
            required=True
        ),
        'id_artista': fields.Integer(
            description='Artista do disco'
        )
    }
)


dados_artista = ns_artista.model(
    'Variáveis para criação do artista musical', {
        'artista': fields.String(
            required=True,
        )
    }
)

@ns_disco.route('/')
class DiscList(Resource):
    @ns_disco.doc('list_disc')
    # @ns_disco.marshal_with(dados_disco_vinil, as_list=True)
    @ns_disco.doc(responses={
            200: "Success",
            500: "Internal Server Error",
            404: "Not found in database"
    })
    def get(self): 
        try:  
            discos = VinylDisc.find_all()
            if discos:
                return discos_schema.dump(discos), 200
            return ({"message": "Nenhum disco encontrado"}), 404
        except Exception as error:
            print(error)
            return ({"message": "Error ao consultar"}), 500

    @ns_disco.doc("create_disc")
    @ns_disco.expect(dados_disco_vinil, validate=True)
    @ns_disco.doc(responses={
            201: "Sucessfuly Created",
            500: "Internal Server Error",
            422: "Validation error"
    })
    def post(self):      
        try:
            data = request.get_json()
            disco = disco_schema.load(data)
            disco.save_in_db()
            return ({"message": "Dados salvos com sucesso"}), 201
        except ValidationError as error:
            print(error.messages)
            print(error.valid_data)
            return ({"message": "Error ao salvar informações"}), 422


@ns_disco.route('/<id>')
class Disco(Resource):
    @ns_disco.doc("Deletar um disco")
    @ns_disco.doc(responses={
            200: "Successfully deleted",
            404: "Not found in database",
            500: "Internal Server Error"
    })
    def delete(self, id):   
        try:   
            disco = VinylDisc.find_by_id(id)
            if disco:
                disco.delete_from_db()
                return ({"message": "Deletado!"}), 200
            return ({"message": "Disco não encontrado"}), 404
        except Exception as error:
            print(error)
            return ({"message": "erro ao deletar registro"}), 500

    @ns_disco.doc('Atualizar um disco')
    @ns_disco.expect(dados_disco_vinil)
    @ns_disco.doc(responses={
            200: "Successfully updated",
            404: "Not found in database",
            422: "Validation error",
            500: "Internal Server Error"
    })
    def put(self, id):   
        try:   
            disco = VinylDisc.find_by_id(id)
            if disco:
                data = request.get_json()
                disco.titulo = data['titulo']
                disco.valor = data['valor']
                disco.genero = data['genero']
                disco.save_in_db()
                return ({"message": "Disco atualizado"}), 200
            return ({"message": "Disco não encontrado"}), 404
        except ValidationError as error:
            print(error.messages)
            print(error.valid_data)
            return ({"message": "Error ao salvar informações"}), 422


@ns_artista.route('/')
class ArtistList(Resource):
    # @ns_artista.marshal_list_with(dados_artista, code=200)
    @ns_artista.doc(responses={ 
            200: "Success",
            500: "Internal Server Error",
            404: "Not found in database"
    })
    def get(self):   
        try:   
            artistas = Artist.find_all()
            if not artistas:
                print('na vdd to aq')
                return ({"message": "Nenhum artista encontrado"}), 404
            else:
                print('n sei pq to aq')
                return artistas_schema.dump(artistas), 200
        except Exception as error:
            print(error)
            return ({"message": "Erro ao consultar"}), 500
           


    @ns_artista.expect(dados_artista, validate=True)
    @ns_artista.doc(responses={
            201: "Successfully Created",
            422: "Validation error",
            409: "Artist already exists",
            500: "Internal Server Error"
    })
    @ns_artista.doc(id="Criar um artista")
    def post(self):   
        try:   
            data = request.get_json()
            # deserializes data to application-level data structure
            artista = artista_schema.load(data)
            if Artist.find_by_artist(data['artista']):
                return ({"message": "Artista já existe"}), 409
            artista.save_in_db()
            return ({"message": "Dados salvos com sucesso"}), 201
        except ValidationError as error:
            print(error.messages)
            print(error.valid_data)
            return ({"message": "Error ao salvar informações"}), 422



@ns_artista.route('/<id>')
# artist class to represent resource for restapi
class Artista(Resource):
    @ns_artista.doc(responses={
            200: "Successfully deleted",
            400: "Validation Error",
            404: "Not found in database",
            500: "Internal Server Error"
    })
    @ns_artista.doc("Deletar o artista e seus discos")
    def delete(self, id):   
        try:   
            artista = Artist.find_by_id(id)
            if artista:
                artista.delete_from_db()
                return ({"message": "Deletado!"}), 200
            return ({"message": "Artista não encontrado"}), 404
        except Exception as error:
            print(error)
            return ({"message": "erro ao deletar registro"}), 500


    @ns_artista.expect(dados_artista)
    @ns_artista.doc(responses={ 
            200: "Successfully updated",
            500: "Internal Server Error",
            404: "Not found in database",
            422: "Validation Error"
    })
    @ns_artista.doc("Atualizar o nome de um artista")
    def put(self, id):   
        try:   
            artista = Artist.find_by_id(id)
            if artista:
                data = request.get_json()
                artista.artista = data['artista']
                artista.save_in_db()
                return ({"message": "Artista atualizado"}), 200
            return ({"message": "Artista não encontrado"}), 404
        except Exception as error:
            print(error)
            return ({"message": "error ao atualizar registro"}), 422


def vincula_ns_api(api):
    api.add_namespace(ns_disco)
    api.add_namespace(ns_artista)
    return None
