import os
import json
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

username = os.getenv("MONGO_USER_NAME")

password = os.getenv('MONGO_PASSWORD')

URI = f"mongodb+srv://{username}:{password}@cluster0.utqb2a0.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(URI)

db = client["userData"]
user_collection = db.user
# result = user_collection.insert_one({'test': 'passed'})
# result = user_collection.find()
# print(list(result)[0]['test'])
