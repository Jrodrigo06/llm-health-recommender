from pymongo import MongoClient
from datetime import datetime
from app.config import MONGO_URL
from app.models.schema import UserInfo
from app.services.auth import verify_password

"""
This module is responsible for interacting with the MongoDB database.
It provides functions to log predictions and retrieve user history."""

client = MongoClient(MONGO_URL)
db = client["health_logs"]
user_logs_collection = db["user_predictions"]
users_collection = db["users"]

# Function to determine if a user exists in the database based on user_id
def user_exists(user_id: int) -> bool:
    user = users_collection.find_one({"user_id": user_id})
    exists = user is not None
    return exists

# This function creates a new user in the database with the provided user_id, password, and user_info.
def create_user(user_id : int, password : str, user_info : UserInfo):
    if user_exists(user_id):
        raise ValueError(f"User with user_id {user_id} already exists.")
    log_user = {
        "user_id": user_id,
        "password": password,
        "user_info": user_info.model_dump(),
        "created_at": datetime.now()
    }
    users_collection.insert_one(log_user)

# Login function to verify user credentials
def login_user(user_id: int, password: str) -> bool:
    if(user_exists(user_id) == False):
        raise ValueError(f"User with user_id {user_id} does not exist.")
    user = users_collection.find_one({"user_id": user_id})
    hashed_pass = user.get("password")
    if verify_password(password ,hashed_pass):
        return True
    else:
        return False
    
# Get user information based on user_id
def get_user_info(user_id: int) -> UserInfo:
    if not user_exists(user_id):
        raise ValueError(f"User with user_id {user_id} does not exist.")
    
    user = users_collection.find_one({"user_id": user_id})
    user_info = UserInfo(**user["user_info"])
    return user_info
    


# This function logs the prediction response, user_id, and question to the database
def log_prediction(response, user_id, question):
    log_entry = {
        "user_id": user_id,
        "question": question,
        "response": response,
        "timestamp": datetime.now()
    }

    user_logs_collection.insert_one(log_entry)

# This function retrieves the history of predictions for a given user_id
def get_user_history(user_id):

    
    history = list(user_logs_collection.find({"user_id": user_id}))
    print("Querying history for user_id:", user_id)
    for record in history:
        # Convert ObjectId to string for JSON serialization
        record["_id"] = str(record["_id"])

    print("History after conversion:", history)
    return list(history)
