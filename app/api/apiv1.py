from flask_restx import Namespace, Resource, fields
from flask import jsonify, request
from app.models import Artist, VinylDisc, db
from app.api.serializers import discos_schema, disco_schema, artista_schema, artistas_schema
from marshmallow import ValidationError

ns_disco = Namespace('discos', description='Discos de Vinil')
ns_artista = Namespace('artistas', description='Artistas musicais')

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
            description='Artista do disco',
            required=True
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
    # @ns_disco.marshal_with(dados_disco_vinil)
    @ns_disco.doc(responses={
            200: "Success",
            500: "Internal Server Error",
            404: "Not found in database",
            400: "Bad request"
    })
    @ns_disco.doc("list_disc")
    def get(self): 
        try:  
            discos = db.session.query(VinylDisc.id, VinylDisc.titulo, VinylDisc.genero, VinylDisc.valor, Artist.artista).\
                join(Artist).filter(Artist.id == VinylDisc.id_artista).all()
            # joined = []
            # for data in discos:
            #     join_data = {}
            #     join_data['titulo'] = data.titulo
            #     join_data['genero'] = data.genero
            #     join_data['valor'] = data.valor
            #     join_data['artista'] = data.artista
            #     join_data['id'] = data.id
            #     joined.append(join_data)
            if discos:
                return ({"discos": discos_schema.dump(discos)}), 200
            return ({"message": "Disc not found"}), 404
        except Exception as error:
            print(error)
            return ({"message": "Fails to list discs"}), 500


    @ns_disco.doc("create_disc")
    @ns_disco.expect(dados_disco_vinil, validate=True)
    @ns_disco.doc(responses={
            201: "Sucessfuly Created",
            500: "Internal Server Error",
            422: "Validation error"
    })
    def post(self): 
        super()     
        try:
            data = request.get_json()
            artist = Artist.find_by_id(data['id_artista'])
            if artist == None:
                return ({"message": "Incorrect or non-existent id_artista"}), 422
            disco = disco_schema.load(data)
            disco.save_in_db()
            return ({"message": "Successfully saved"}), 201
        except ValidationError as error:
            print(error.messages)
            print(error.valid_data)
            return ({"message": "Failed to create disc"}), 422


@ns_disco.route('/<id>')
class Disco(Resource):
    @ns_disco.doc("delete_disc_by_id")
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
                return ({"message": "Successfully deleted"}), 200
            return ({"message": "Disc not found"}), 404
        except Exception as error:
            print(error)
            return ({"message": "Fails to delete disc"}), 500

    @ns_disco.doc('update_disc_by_id')
    @ns_disco.expect(dados_disco_vinil, validate=True)
    @ns_disco.doc(responses={
            200: "Successfully updated",
            404: "Not found in database",
            422: "Validation error",
            500: "Internal Server Error"
    })
    def put(self, id):   
        try:   
            disco = VinylDisc.find_by_id(id)
            data = request.get_json()
            artist = Artist.find_by_id(data['id_artista'])
            if disco:
                disco.titulo = data['titulo']
                disco.valor = data['valor']
                disco.genero = data['genero']
                disco.id_artista = data['id_artista']
                if artist == None:
                    return ({"message": "Incorrect or non-existent id_artista"}), 404
                if len(data) > 4:
                    raise KeyError(({"unknown fields": list(data.keys())[4:]}))
                else:
                    disco.save_in_db()
                return ({"message": "Successfully disc updated"}), 200
            return ({"message": "Disc not found"}), 404
        except ValidationError as error:
            raise error
            return ({"message": "Failed to update"}), 422


@ns_artista.route('/')
class ArtistList(Resource):
    """ Appears in Title of Swagger
        Authorization: Bearer <auth-key>
    """
    # @ns_artista.marshal_with(dados_artista, code=200)
    @ns_artista.doc(responses={ 
            200: "Success",
            500: "Internal Server Error",
            404: "Not found in database"
    })
    @ns_artista.doc("list_artist")
    def get(self):   
        try:   
            artistas = Artist.find_all()
            print(artistas)
            if not artistas:
                return ({"message": "Artists not found"}), 404
            return artistas_schema.dump(artistas), 200
        except Exception as error:
            print(error)
            return ({"message": "Fails to list artists"}), 500
           


    @ns_artista.expect(dados_artista, validate=True)
    @ns_artista.doc(responses={
            201: "Successfully Created",
            422: "Validation error",
            409: "Artist already exists",
            500: "Internal Server Error"
    })
    @ns_artista.doc("create_artist")
    def post(self):   
        try:   
            data = request.get_json()
            # deserializes data to application-level data structure
            artista = artista_schema.load(data)
            if Artist.find_by_artist(data['artista']):
                return ({"message": "Artist already exists"}), 409
            artista.save_in_db()
            return ({"message": "Successfully saved"}), 201
        except ValidationError as error:
            print(error.messages)
            print(error.valid_data)
            return ({"message": "Fails to create Artist"}), 422



@ns_artista.route('/<id>')
# artist class to represent resource for restapi
class Artista(Resource):
    '''show a test in swagger'''
    @ns_artista.doc(responses={
            200: "Successfully deleted",
            400: "Validation Error",
            404: "Not found in database",
            500: "Internal Server Error"
    })
    @ns_artista.doc("delete_artist_by_id")
    def delete(self, id):   
        try:   
            artista = Artist.find_by_id(id)
            if artista:
                artista.delete_from_db()
                return ({"message": "Sucessfully deleted"}), 200
            return ({"message": "Artist not found"}), 404
        except Exception as error:
            print(error)
            return ({"message": "failed to delete artist"}), 500


    @ns_artista.expect(dados_artista, validate=True)
    @ns_artista.doc(responses={ 
            200: "Successfully updated",
            500: "Internal Server Error",
            404: "Not found in database",
            422: "Validation Error"
    })
    @ns_artista.doc("update_artist_by_id")
    def put(self, id):   
        try:   
            artista = Artist.find_by_id(id)
            if artista:
                data = request.get_json()
                artista.artista = data['artista']
                if len(data) > 1:
                    raise ValidationError("JSON incorreto")
                artista.save_in_db()
                return ({"message": "Sucessfully artist name updated"}), 200
            return ({"message": "Artist not found"}), 404
        except Exception as error:
            print(error)
            return ({"message": "failed to update artist"}), 422


def vincula_ns_api(api):
    api.add_namespace(ns_disco)
    api.add_namespace(ns_artista)
    return None
