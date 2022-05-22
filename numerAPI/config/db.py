from pymongo import MongoClient
import os

connString = os.environ['mongodb://localhost:27017']
conn = MongoClient(connString)