from app.services.weather import get_weather
# from app.services.location import get_location
from flask import render_template
from . import cityweather

@cityweather.route('/')
def index():
    city_weather = get_weather('shanghai')
    return render_template('index.html',weather=city_weather)

@cityweather.route('/<cityname>')
def g_weather(cityname):
    city_weather = get_weather(cityname)
    return render_template('index.html',weather=city_weather)


