from pymongo import MongoClient

class messageLoader():

    def __init__(self, db_name):
        mgclient = MongoClient()
        db = mgclient[db_name]
        self.collection = db["queued_messages"]

    def add_to_queue(self, message):
        response = self.collection.insert({"message": message})
        print(response)

    def purge_queue(self):
        response = self.collection.delete_many({})
        print(response)
