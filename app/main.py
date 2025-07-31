from app.api.routes import router
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Main function to run the FastAPI application
def main():
    
    app = FastAPI()

    origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api")

    uvicorn.run(app, host="0.0.0.0", port=8000)
    

if __name__ == "__main__":
    main()
