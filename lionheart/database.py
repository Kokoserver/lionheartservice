from pymongo import MongoClient
from starlette.config import Config
from .settings import DATABASE_URL


class Database(object):
    DATABASE = None

    @staticmethod
    def inittailize():
       __client = MongoClient(DATABASE_URL)
       Database.DATABASE =  __client

    @staticmethod
    def find(collection:str, data:dict):
        return Database.DATABASE[collection].find(data)

    @staticmethod
    def save(collection:str, data:dict):
        return Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def update(collection:str, old_data:dict, new_data:dict):
        return Database.DATABASE[collection].update_one(old_data, {"$set":new_data})

    @staticmethod
    def delete(collection:str, data:dict):
        return Database.DATABASE[collection].delete_one(data)

   



