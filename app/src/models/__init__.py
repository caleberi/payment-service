import os
from decouple import config
from pymongo import MongoClient

MONGODB_URI = config('MONGODB_URI')
MONGODB_DATABASE_NAME = config('MONGODB_DATABASE_NAME')

mongo_client = MongoClient(MONGODB_URI)

def database():
    return mongo_client[MONGODB_DATABASE_NAME]