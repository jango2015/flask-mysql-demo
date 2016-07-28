from flask import Blueprint

cityweather = Blueprint('cityweather', __name__)

from . import views
