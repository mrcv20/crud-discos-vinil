from flask import Blueprint
from flask_restx import Api
from ..api import api01

blueprint = Blueprint("API - CRUD de uma loja de discos de vinil", __name__, url_prefix="/api/v1")
api = Api(blueprint,
title='API de discos de vinil',
version='1.0',
description='Endpoints CRUD para uma loja de discos de vinil'
)

api01.ns_api(api)


def create_api(app):
    app.register_blueprint(api.blueprint)
    return None