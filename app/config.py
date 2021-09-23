class Config(object):
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URL = "sqlite:////./store.db"


class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True