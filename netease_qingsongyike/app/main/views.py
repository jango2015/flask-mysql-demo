# -- coding: UTF-8 --
from flask import render_template
from . import main
from .weather import get_weather, get_location


@main.route('/')
def index():
    weather = get_weather('shanghai')
    loc = get_location()
    return render_template('index.html', weather=weather,loc=loc)

