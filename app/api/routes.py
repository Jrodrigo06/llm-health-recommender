from fastapi import APIRouter
from app.models.schema import UserRequest
from app.services.llm_service import get_response_from_llm, format_prompt
from app.services.mongo_service import log_prediction, get_user_history


router = APIRouter()

# Home route
@router.get("/")
async def root():
    return {"message": "HomePage"}

#predict route to handle user requests
@router.post("/predict")
async def predict(data: UserRequest):
    #Response returned from the LLM
    ## Calls the LLM with the formatted prompt and user information
    response = {"recommendation":
        get_response_from_llm(format_prompt(data.user_info.model_dump(), data.question))}
    
    ##Logs the prediction with user_id and question to the database
    log_prediction(response, data.user_id, data.question)

    return response

# Route to get user history
@router.get("/history/{user_id}")
async def get_history(user_id: int):
    return {"history": get_user_history(user_id)}
