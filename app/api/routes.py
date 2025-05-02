from fastapi import APIRouter
from app.models.schema import UserRequest
from app.services.llm_service import get_response_from_llm, format_prompt

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "HomePage"}

@router.post("/predict")
async def predict(data: UserRequest):
    return {"message":
             get_response_from_llm(format_prompt(data.user_info.model_dump(), data.question))}

@router.get("/history/{user_id}")
async def get_history(user_id: int):
    return {"message": "Dummy response"}
