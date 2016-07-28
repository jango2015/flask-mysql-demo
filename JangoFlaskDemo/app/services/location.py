import json
from urllib.request import Request,urlopen

def get_location():
    url = 'http://apis.baidu.com/lbs_repository/wifi/query?mac=24%3Ade%3Ac6%3A76%3A4c%3A10&coord=wgs84'
    req = Request(url)
    req.add_header("apikey", "183818060be492d5e010580c75322622")
    resp = urlopen(req)
    content = resp.read()

    data = content.decode('utf-8')
    jdata = json.loads(data)
    return jdata