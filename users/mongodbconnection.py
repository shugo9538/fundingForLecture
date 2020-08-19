from pymongo import MongoClient

class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(
            "mongodb+srv://fundforlecture:fundforlecture1234@fundingforlecture.vu2dn.mongodb.net/user?retryWrites=true&w=majority",
            27017)