from fastapi import APIRouter, FastAPI, HTTPException
from app.models.schema import UserRequest, UserSignUp
from app.services.llm_service import get_response_from_llm, format_prompt
from app.services.mongo_service import log_prediction, get_user_history, get_user_info, create_user, login_user
from fastapi import Depends
from app.services.auth import hash_password, create_access_token, get_current_user

"""
This module defines the API routes for the application, using FastAPI.
It includes routes for the home page, prediction requests, 
and user history retrieval.
"""




router = APIRouter()






# Home route
@router.get("/")
async def root():
    return {"message": "HomePage"}

# Post route to handle user creation
@router.post("/create_user")
async def make_user(payload: UserSignUp):

    user_id = payload.user_id
    password = payload.password
    user_info = payload.user_info

    hashed_password = hash_password(password)
    
    create_user(user_id, hashed_password, user_info)

    return {"message": "User created successfully"}

# Login route to handle user authentication
@router.post("/login")
async def login(payload: dict):
    user_id = payload.get("user_id")
    password = payload.get("password")
    try:
        login_user(user_id, password)
        token = create_access_token({"user_id": user_id})       
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Route to validate token
@router.get("/validate_token")
async def validate_token(user_id: int = Depends(get_current_user)):
    return {"valid": True, "user_id": user_id}


#predict route to handle user requests
@router.post("/predict")
async def predict(
    userRequest: UserRequest,
    user_id: int = Depends(get_current_user),
):
    profile = get_user_info(user_id)
    prompt   = format_prompt(profile.model_dump(), userRequest.question)
    answer   = get_response_from_llm(prompt)

    log_prediction({"recommendation": answer}, user_id, userRequest.question)

    return {"recommendation": answer}

# Route to get user history
@router.get("/history")
async def get_history(user_id: int = Depends(get_current_user)):
    print("Fetching history for user_id:", user_id)
    return {"history": get_user_history(user_id)}







