from urllib.request import Request,urlopen
import json
import os
import math
from mongoservice import *
# import io


filepath =os.path.abspath("./baidu_zhaopin_jobs.json")


def convert_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict


def convert_to_dicts(objs):
    '''把对象列表转换为字典列表'''
    obj_arr = []
    for o in objs:
        # 把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
    return obj_arr


def class_to_dict(obj):
    '''把对象(支持单个对象、list、set)转换成字典'''
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            # 把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict

def get_jobs(pagenumber,pagesize,keyword):
    # print(filepath)
    url =  'http://zhaopin.baidu.com/api/async?query='+(keyword if len(keyword) >0 else '.net')+'&salary=&welfare=&education=&sort_key=&sort_type=1&city=%E4%B8%8A%E6%B5%B7&district=&experience=&employertype=&jobfirstclass=&jobsecondclass=&jobthirdclass=&date=&detailmode=close&rn='+str(pagesize)+'&pn='+str(pagenumber)+''
    req = Request(url)
    resp = urlopen(req)
    content = resp.read()
    data = content.decode("utf-8")
    jdata = json.loads(data)
    # j_str = json.dumps(jdata)
    jobsInfos = jdata["data"]["data"]["disp_data"]
    jobs = []
    jobobjs =set()
    for item in jobsInfos:
        org_salary = item["ori_salary"]
        salary = item["salary"]
        if org_salary.find("0000") != -1 or salary.find("000")!=-1:
            jobs.append(item)
            jobobj = jsonitem_to_obj(item)
            jobobjs.add(jobobj)
        else:
            continue
    # print(jobs)
    v = class_to_dict(jobobjs)
    Insert(v)
    print(v)
    f = open(filepath,'a')
    s = str(v)
    f.write(s)
    f.close()
    # s =  json.dumps(v)
    # print(s)
    # jobsdata = str(jobobjs)
    # print(jobsdata)

    # f = open(filepath,'a')
    # f.write(jobsdata)
    # f.close()
    # print(jdata)
    return jdata
def jsonitem_to_obj(item):
    jobobj = Job_item()
    keys =item.keys()
    jobobj.loc = item['loc'] if 'loc' in keys else ''
    jobobj.type = item['type'] if 'type' in keys else ''
    jobobj.enddate = item['enddate'] if 'enddate' in keys else ''
    jobobj.experience = item['experience'] if 'experience' in keys else ''
    jobobj.dgw_trunk = item['dgw_trunk'] if 'dgw_trunk' in keys else ''
    jobobj.build = item['build'] if 'build' in keys else ''
    jobobj.jobwapurl = item['jobwapurl'] if 'jobwapurl' in keys else ''
    jobobj.jobsecondclass = item['jobsecondclass'] if 'jobsecondclass' in keys else ''
    jobobj.dgw_site = item['dgw_site'] if 'dgw_site' in keys else ''
    jobobj.oauthjoburl = item['oauthjoburl'] if 'oauthjoburl' in keys else ''
    jobobj.employerurl = item['employerurl'] if 'employerurl' in keys else ''
    jobobj.companydescripti = item['companydescripti'] if 'companydescripti' in keys else ''
    jobobj.sex = item['sex'] if 'sex' in keys else ''
    jobobj.salary = item['salary'] if 'salary' in keys else ''
    jobobj.secondindustry = item['secondindustry'] if 'secondindustry' in keys else ''
    jobobj.employertype = item['employertype'] if 'employertype' in keys else ''
    jobobj.haswapurl = item['haswapurl'] if 'haswapurl' in keys else ''
    jobobj.joblink = item['joblink'] if 'joblink' in keys else ''
    jobobj.number = item['number'] if 'number' in keys else ''
    jobobj.size = item['size'] if 'size' in keys else ''
    jobobj.welfare = item['welfare'] if 'welfare' in keys else ''
    jobobj.description = item['description'] if 'description' in keys else ''
    jobobj.name = item['name'] if 'name' in keys else ''
    jobobj.title = item['title'] if 'title' in keys else ''
    jobobj.age = item['age'] if 'age' in keys else ''
    jobobj.jobfirstclass = item['jobfirstclass'] if 'jobfirstclass' in keys else ''
    jobobj.url = item['url'] if 'url' in keys else ''
    jobobj.sourcelink = item['sourcelink'] if 'sourcelink' in keys else ''
    jobobj.industry = item['industry'] if 'industry' in keys else ''
    jobobj.StdStg = item['StdStg'] if 'StdStg' in keys else ''
    jobobj.district = item['district'] if 'district' in keys else ''
    jobobj.source = item['source'] if 'source' in keys else ''
    jobobj.depart = item['depart'] if 'depart' in keys else ''
    jobobj.city = item['city'] if 'city' in keys else ''
    jobobj.domain = item['domain'] if 'domain' in keys else ''
    jobobj.startdate = item['startdate'] if 'startdate' in keys else ''
    jobobj.education = item['education'] if 'education' in keys else ''
    jobobj.jobthirdclass = item['jobthirdclass'] if 'jobthirdclass' in keys else ''
    jobobj.commonname = item['commonname'] if 'commonname' in keys else ''
    jobobj.companyaddress = item['companyaddress'] if 'companyaddress' in keys else ''
    jobobj.province = item['province'] if 'province' in keys else ''
    jobobj.location = item['location'] if 'location' in keys else ''
    jobobj.email = item['email'] if 'email' in keys else ''
    return jobobj

def get_jobs_by_pagenums():
    page_num = 1
    list_num = 760
    page_size = 100
    pages =math.ceil(list_num/page_size)
    print(pages)
    while(pages>=page_num):
        get_jobs(page_num,page_size,'')
        print(page_num)
        page_num+=1





class Job_item:
    # def __init__(self):
    def __new__(cls, *args, **kwargs):
        return object.__new__(Job_item,*args,**kwargs)

    loc = ''
    type = ''
    enddate = ''
    experience = ''
    dgw_trunk = ''
    build=''
    jobsecondclass=''
    dgw_site =''
    employerurl=''
    companydescription=''
    sex=''
    salary=''
    secondindustry=''
    employertype=''
    haswapurl=''
    joblink = ''
    number=''
    size=''
    welfare=[]
    description=''
    name=''
    title=''
    age=''
    jobfirstclass=''
    url=''
    sourcelink=''
    industry=''
    StdStg=''
    district=''
    source=''
    depart=''
    city=''
    domain=''
    startdate=''
    education=''
    jobthirdclass=''
    commonname=''
    companyaddress=''
    province=''
    location=''
    email=''


if __name__ == '__main__':
    get_jobs_by_pagenums()