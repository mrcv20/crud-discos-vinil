from flask import Flask
from .config import DevelopmentConfig
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def create_app():
    app = Flask(__name__)
    ma = Marshmallow(app)
    url = DevelopmentConfig.SQLALCHEMY_DATABASE_URL
    engine = create_engine(url, connect_args={"check_same_thread": False})

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    return app
