from flask import Flask
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_object(DevelopmentConfig)
    if getenv('FLASK_ENV') in ['testing']:
        app.config.from_object(TestingConfig)
    elif getenv('FLASK_ENV') in ['development']:
        app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        
        db.create_all()

        return app

app = create_app()
ma = Marshmallow(app)
