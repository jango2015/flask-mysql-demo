import json
from urllib.request import Request, urlopen


def get_weather(city):
    url = 'http://apis.baidu.com/heweather/weather/free?city=%s' % city
    req = Request(url)
    req.add_header("apikey", "ebfc3a7186254a37fc715d2f9d4c4049")
    resp = urlopen(req)
    content = resp.read()
    data = content.decode('utf-8')
    j = json.loads(data)
    weather = j["HeWeather data service 3.0"][0]
    return weather


def get_location():
    url = 'http://apis.baidu.com/lbs_repository/wifi/query?mac=24%3Ade%3Ac6%3A76%3A4c%3A10&coord=wgs84'
    req = Request(url)
    req.add_header("apikey", "183818060be492d5e010580c75322622")
    resp = urlopen(req)
    content = resp.read()

    data = content.decode('utf-8')
    j = json.loads(data)
    return j
