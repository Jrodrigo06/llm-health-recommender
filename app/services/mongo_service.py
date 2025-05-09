from pymongo import MongoClient
from datetime import datetime
from app.config import MONGO_URI, TESTING

client = MongoClient(MONGO_URI)
db = client["health_logs"]
if TESTING != "1":
    collection = db["user_predictions"]
else:
    collection = db["user_predictions_test"]



def log_prediction(response, user_id, question):
    if TESTING == "1":
        # Return to not messup user_predictions_test collection
        print("TESTING mode, not logging to database.")
        return
    log_entry = {
        "user_id": user_id,
        "question": question,
        "response": response,
        "timestamp": datetime.now()
    }

    collection.insert_one(log_entry)

def get_user_history(user_id):

    
    history = list(collection.find({"user_id": user_id}))
    print("Querying history for user_id:", user_id)
    for record in history:
        # Convert ObjectId to string for JSON serialization
        record["_id"] = str(record["_id"])

    print("History after conversion:", history)
    return list(history)
