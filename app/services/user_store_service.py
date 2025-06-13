from pymongo import MongoClient
from datetime import datetime
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["user_store"]