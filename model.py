from database import Database
from uuid import uuid4
import datetime

def getData(DataObject):
    for data in DataObject:
        return data



class LionheartUser(object):
    Database.inittailize()
    COLLECTION = "user"
    def __init__(self, firstname:str, lastname:str, email:str, category:str, phone:str, address:str):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.category = category
        self.address = address
        self.phone = phone
         

    def json(self):
        return {
            "_id":uuid4().hex,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "email":self.email,
            "category":self.category,
            "address":self.address,
            "phone":self.phone,
            "date":datetime.datetime.now()
        }
    

    def save(self):
        Database.save(collection=LionheartUser.COLLECTION, data=self.json())

    @staticmethod
    def find(data) -> dict:
        data = Database.find(collection=LionheartUser.COLLECTION, data=data)
        return getData(data)

    @staticmethod
    def all(data) -> dict:
        data = Database.find(collection=LionheartUser.COLLECTION, data=data)
        return data

    @staticmethod
    def update(old_data:dict, new_data:dict) -> dict:
        data = Database.update(collection=LionheartUser.COLLECTION, old_data=old_data, new_data=new_data)
        return getData(data)

    @staticmethod
    def delete(data:dict) -> None:
        return Database.delete(collection=LionheartUser.COLLECTION, data=data)
        



class LionheartContact(object):
    Database.inittailize()
    COLLECTION = "contact"
    def __init__(self, name:str, email:str, message:str):
        self.name = name
        self.email = email
        self.message = message

    def json(self):
        return {
            "_id":uuid4().hex,
            "name":self.name,
            "email":self.email,
            "message":self.message
            
        }
    

    def save(self):
        return Database.save(collection=LionheartContact.COLLECTION, data=self.json())

    @staticmethod
    def find(self, data) -> dict:
        data = Database.find(collection=LionheartContact.COLLECTION, data=data)
        return getData(data)

    @staticmethod
    def update(old_data:dict, new_data:dict) -> dict:
        data = Database.update(collection=LionheartContact.COLLECTION, old_data=old_data, new_data=new_data)
        return getData(data)

    @staticmethod
    def delete(self, data:dict) -> None:
        return Database.delete(collection=LionheartContact.COLLECTION, data=data)


class LionheartAdmin(object):
    Database.inittailize()
    COLLECTION = "account"
    def __init__(self, email:str, password:str):
        self.email = email
        self.password = password

    def json(self):
        return {
            "_id":uuid4().hex,
            "email":self.email,
            "password":self.password,
            "active":True,
            "admin":True
            
        }
    

    def save(self) -> None:
        Database.save(collection=LionheartAdmin.COLLECTION, data=self.json())

    @staticmethod
    def find(email:str, password:str) -> dict:
        data = Database.find(collection=LionheartAdmin.COLLECTION, data={"email":email, "password":password})
        return getData(data)

    @staticmethod
    def update(self, old_data:dict, new_data:dict) -> dict:
        data = Database.update(collection=LionheartAdmin.COLLECTION, old_data=old_data, new_data=new_data)
        return getData(data)

    @staticmethod
    def delete(self, data:dict) -> None:
        return Database.delete(collection=LionheartAdmin.COLLECTION, data=data)

    

    
        

        

