import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    # DEBUG = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@localhost/datademo"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@localhost/test"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@localhost/server"

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}