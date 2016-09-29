import  os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    @staticmethod
    def init_app(app):
        pass
class DevConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:123456@localhost/datademo"
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@localhost/TestDemo"
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@localhost/server"

config = {
    'dev': DevConfig,
    'test': TestConfig,
    'production': ProductionConfig,
    'default': DevConfig
}
