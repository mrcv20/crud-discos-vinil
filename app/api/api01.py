from flask_restx import Namespace, Resource, fields
from flask import jsonify, request, json, sessions
from app.models import VinylDisc, db
from app.api.serializers import discos_schema

ns = Namespace('disco', description='Disco de Vinil')

cria_disco_vinil_request = ns.model(
    'Variáveis para criação do disco', {
        'titulo': fields.String(
            required=True,
            description='Título do disco de vinil',
        ),     
        'genero': fields.String(
            description='Gênero do disco',
            required=True
        ),
        'valor': fields.Float(
            description='Preço do disco',
            required=True
        
        ),
        'artista': fields.String(
            description='Nome do artista',
            required=True
        )
    }
)

cria_disco_vinil_response = ns.model(
    'Resposta da criação do disco',{
        'id': fields.String(
            description="Identifcador único do disco."
        )
    }
)

@ns.route('/', doc={"description": 'Registar um disco de vinil'})
class RegistraDisco(Resource):
    @ns.expect(cria_disco_vinil_request, validate=True)
    def post(self):      
        try:
            data = request.get_json()
            print(type(data['valor']))
            valor = data['valor']
            novo_disco = VinylDisc(titulo=data['titulo'], genero=data['genero'], valor=data['valor'], artista=data['artista'])
            db.session.add(novo_disco)
            db.session.commit()
        except Exception as error:
            print(error)
        finally:
            return jsonify(f"Dados inseridos!")

@ns.route('/', doc={"description": 'Consulta todos os discos de vinil'})
class ConsultaDisco(Resource):
    def get(self):    
        try:  
            discos = VinylDisc.query.all()
            return discos_schema.dump(discos)
        except Exception as error:
            return error
        finally:
            return jsonify("Carregado com sucesso!")

@ns.route('/<id>', doc={"description": 'Deleta um disco da base de dados'})
class Disco(Resource):
    def delete(self, id):   
        try:   
            disco = VinylDisc.query.filter(VinylDisc.id == id).delete()
            db.session.commit()
            return jsonify("Deletado!")
        except Exception as error:
            return error

    def put(self, id):   
        try:   
            data = request.get_json()
            disco = VinylDisc.query.filter(VinylDisc.id == id).first()
            disco.genero = data['genero']
            disco.titulo = data['titulo']
            disco.valor = data['valor']
            disco.artista = data['artista']
            db.session.commit()
            return jsonify("Deletado!")
        except Exception as error:
            return error


def ns_api(api):
    api.add_namespace(ns)
    return None
