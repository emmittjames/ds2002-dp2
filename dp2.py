from pymongo import MongoClient, errors
from bson.json_util import dumps
import os, json
from dotenv import load_dotenv

load_dotenv()
MONGOPASS = os.getenv('MONGOPASS')

uri = "mongodb+srv://cluster0.gomignk.mongodb.net/"
client = MongoClient(uri, username='gwu8ek', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client.testDB
collection = db.testCollection

with open('./data/generated00.json') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    collection.insert_many(file_data)  
else:
    collection.insert_one(file_data)