from pymongo import MongoClient
from datetime import datetime
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["health_logs"]
collection = db["user_predictions"]

def log_prediction(response, user_id, question):

    log_entry = {
        "user_id": user_id,
        "question": question,
        "response": response,
        "timestamp": datetime.now()
    }

    collection.insert_one(log_entry)

def get_user_history(user_id):
    history = collection.find({"user_id": user_id})
    for record in history:
        # Convert ObjectId to string for JSON serialization
        record["_id"] = str(record["_id"])
    return list(history)
