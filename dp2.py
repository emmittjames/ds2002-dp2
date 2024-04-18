from pymongo import MongoClient, errors
from bson.json_util import dumps
from dotenv import load_dotenv
import os, json

load_dotenv()
MONGOPASS = os.getenv('MONGOPASS')

uri = "mongodb+srv://cluster0.gomignk.mongodb.net/"
client = MongoClient(uri, username='gwu8ek', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
db = client.testDB
collection = db.testCollection

data_dir = "./data"

complete_documents = 0
could_not_import = 0
corrupted_documents = 0

for filename in os.listdir(data_dir):
    file_path = os.path.join(data_dir, filename)
    try:
        with open(file_path) as file:
            file_data = json.load(file)
            if isinstance(file_data, list):
                collection.insert_many(file_data)
            else:
                collection.insert_one(file_data)
            complete_documents += len(file_data)
    except Exception as e:
        print(f"error importing {filename}: {str(e)}")
        could_not_import += len(file_data)
        corrupted_documents += 1

print(f"complete documents: {complete_documents}")
print(f"could not import: {could_not_import}")
print(f"corrupted documents: {corrupted_documents}")