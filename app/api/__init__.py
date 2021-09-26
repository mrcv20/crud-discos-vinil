from flask import Blueprint
from flask_restx import Api
from ..api import apiv1

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint,
    title='Loja de discos de vinil',
    version='1.0',
    description='Simples API com endpoints CRUD para uma loja ficticia de discos de vinil'
)

apiv1.vincula_ns_api(api)

def create_api(app):
    app.register_blueprint(api.blueprint)
    return None