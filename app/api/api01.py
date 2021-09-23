from flask_restx import Namespace, Resource, fields, Api
from flask import jsonify, request, json, sessions
from myapp.models import VinylDisc

ns = Namespace('loja vinil', description='API - CRUD de uma loja de disco de vinil')

disco_vinil = ns.model(
    'Cadastro do disco de vinil', {
        'nome': fields.String(
            description='Nome do artista',
            required=True,
            min_length=5
        ),
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
        )
    }
)

@ns.route('/disco', doc={"description": 'Registar um disco de vinil'})
class RegistraDisco(Resource):
    @ns.expect(disco_vinil, validate=True)
    def post(self):      
        try:
            data = request.get_json()
            return "ok"
        except Exception as error:
            print(error)
        finally:
            return jsonify(f"Consulte o status")

def ns_api(api):
    api.add_namespace(ns)
    return None
