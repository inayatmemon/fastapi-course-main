from pymongo import MongoClient
from config.config import mongodb_db, mongodb_url

conn = MongoClient(mongodb_url)
mydb = conn[mongodb_db]
