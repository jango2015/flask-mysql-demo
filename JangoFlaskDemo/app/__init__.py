
from flask import  Flask
from flask_bootstrap import  WebCDN,Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import  config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    app.extensions['bootstrap']['cdns']['jquery'] =  WebCDN(
        '//cdn.bootcss.com/jquery/1.11.3/'
    )
    app.extensions['bootstrap']['cdns']['bootstrap'] = WebCDN(
        '//cdn.bootcss.com/bootstrap/3.3.5/'
    )
    db.init_app(app)
    from .weather import cityweather as weather_blueprint
    app.register_blueprint(weather_blueprint)
    from .wuxidemo import  users as users_blueprint
    app.register_blueprint(users_blueprint)

    return  app
