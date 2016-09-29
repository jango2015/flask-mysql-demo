from app.services.weather import get_weather
# from app.services.location import get_location
from app.services.zhaopinbaidu import get_jobs
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

# @cityweather.route("/jobs")
# def get_jobs():
#     jobs = get_jobs()
#     return render_template("jobs.html" , jobs = jobs)

