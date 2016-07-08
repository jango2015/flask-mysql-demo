from flask import render_template
from . import  wuxithat
from ..main.weather import get_weather

@wuxithat.route("/wuxi")
def wuxiwether():
    wuxi = get_weather("wuxi")
    return render_template('index.html', weather= wuxi)
