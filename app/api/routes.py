from fastapi import APIRouter, FastAPI, HTTPException
from app.models.schema import UserRequest, UserSignUp
from app.services.llm_service import get_response_from_llm, format_prompt
from app.services.mongo_service import log_prediction, get_user_history, get_user_info, create_user, login_user
from fastapi.middleware.cors import CORSMiddleware
from app.services.auth import hash_password, create_access_token
import uvicorn

"""
This module defines the API routes for the application, using FastAPI.
It includes routes for the home page, prediction requests, 
and user history retrieval.
"""

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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

#predict route to handle user requests
@router.post("/predict")
async def predict(userRequest: UserRequest):
    #Response returned from the LLM
    ## Calls the LLM with the formatted prompt and user information
    response = {"recommendation":
        get_response_from_llm(format_prompt(get_user_info(userRequest.user_id).model_dump(), userRequest.question))}
    
    ##Logs the prediction with user_id and question to the database
    log_prediction(response, userRequest.user_id, userRequest.question)

    return response

# Route to get user history
@router.get("/history/{user_id}")
async def get_history(user_id: int):
    print("Fetching history for user_id:", user_id)
    return {"history": get_user_history(user_id)}


# Include the router in the FastAPI app
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)