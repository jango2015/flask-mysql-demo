from pymongo import MongoClient

client = MongoClient(host='localhost',port=27017)
db =client.get_database('JangoMp')
#db =client['JangoMp']
collection = db.get_collection('MpAccount')
# collection = db.MpAccount;
def get_accounts():
   items= collection.find()
   results =[]
   for item in items:
       print(item)
       results.append(item)
       print(results)
   # print(items)
   print(results)
   return results

def get_account_by_appid(appid):
    #appid:wx410bd3fe3afd168c
    item = collection.find_one({'AppId':appid})
    print(item)
    return  item