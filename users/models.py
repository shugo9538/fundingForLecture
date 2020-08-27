from pymongo import MongoClient
from .mongodbconnection import Connect

# Create your models here.
class MongoConnection(object):
    def __init__(self):
        conn = Connect.get_connection()
        MONGO_SESSION_COLLECTION = 'mongo_sessions'
        self.db = conn.get_database('DB')
        self.collection = self.db.get_collection('user')

    def userCheck(self):
        result = self.collection.find_one({'id': self.userId})
        return result

    def createUser(self, createInfo):
        self.collection.insert_one(createInfo)

    def set(self, user_id):
        self.userId = user_id