from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HomePage"}

@app.get("/predict")
async def predict(data: userInfo_and_question):
    return {"message": "Predict"}