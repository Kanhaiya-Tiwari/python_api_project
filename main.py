from app.api import app 
import uvicorn# Importing the FastAPI application instance from the app.api module
if __name__ == "__main__":
    uvicorn.run(
        #ASGI server to run the FastAPI application
        "app.api:app", # Specifying the module and application instance to run
        host="0.0.0.0",
        port=8000,
        reload=True # Enabling auto-reload for development
    )
