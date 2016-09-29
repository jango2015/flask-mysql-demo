from urllib.request import Request,urlopen
import json


def get_jobs():
    url = 'http://zhaopin.baidu.com/api/async?query=.net&salary=&welfare=&education=&sort_key=&sort_type=1&city=%E4%B8%8A%E6%B5%B7&district=&experience=&employertype=&jobfirstclass=&jobsecondclass=&jobthirdclass=&date=&detailmode=close&rn=30&pn=30'
    req = Request(url)
    resp = urlopen(req)
    content = resp.read()

    data = content.decode("utf-8")
    jdata = json.loads(data)
    return jdata

