from fastapi import APIRouter
from app.models.schema import UserRequest

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "HomePage"}

@router.post("/predict")
async def predict(data: UserRequest):
    return {"message": "Dummy response"}