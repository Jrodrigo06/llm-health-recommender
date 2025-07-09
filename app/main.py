from app.api.routes import app
import uvicorn

# Main function to run the FastAPI application
def main():


    uvicorn.run(app, host="0.0.0.0", port=8000)
    

if __name__ == "__main__":
    main()
