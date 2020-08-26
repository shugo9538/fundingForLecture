from pymongo import MongoClient
from bson.son import SON
from .mongodbconnection import Connect

# Create your models here.
class User(object):

    pass

class MongoConnection(object):
    def __init__(self):
        conn = Connect.get_connection()
        MONGO_SESSION_COLLECTION = 'mongo_sessions'
        self.db = conn.get_database('DB')
        self.collection = self.db.get_collection('user')

    def user_check(self):
        result = self.collection.find_one({'id': self.userId})
        print(result)
        # if self.collection.find_one({'id': self.userId}) is not None:
        #     result = self.collection.find_one({'id': self.userId})
        # else:
        #     result = '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요'
        return result

    def set(self, user_id):
        self.userId = user_id