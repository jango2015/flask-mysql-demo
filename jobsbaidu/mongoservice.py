from pymongo import MongoClient
client = MongoClient(host='localhost',port=27017)
db = client.get_database('JangoMp')
collection = db.get_collection('spider_baidu_jobs')

def Insert(items):
    collection.insert(items)

# def Update(item):
#      collection.update(item)