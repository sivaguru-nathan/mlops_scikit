import pymongo
from env_loader import mongo_url
from bson.objectid import ObjectId

class Modeldb:
    def __init__(self):
        self.client = pymongo.MongoClient(mongo_url)
        db = self.client["mlops_task"]
        self.reg = db["model_registry"]

    def create_record(self,**kwargs):
        return self.reg.insert_one(kwargs)
    
    def get_record(self,_id):
        _id=ObjectId(_id)    
        return self.reg.find_one({"_id": _id})

