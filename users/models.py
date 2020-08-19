from pymongo import MongoClient
from bson.son import SON
from .mongodbconnection import Connect

# Create your models here.
class MongoConnection(object):
    def __init__(self):
        conn = Connect.get_connection()
        self.db = conn.get_database('DB')
        self.collection = self.db.get_collection('user')

    def user_check(self):
        result = self.collection.find_one({'id': self.userId})
        return result

    def set(self, user_id):
        self.userId = user_id