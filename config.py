from pymongo import MongoClient

DEBUG = True
client = MongoClient('mongodb://%s:%s@127.0.0.1' % ('myUserAdmin', 'abc123'))
DATABASE = client['Bank']
