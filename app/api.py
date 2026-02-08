from fastapi import FastAPI 
from routers import metrics, aws

app = FastAPI (
    title="My FastAPI Application",
    description="This is a simple FastAPI application.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")

@app.get("/")
def hello():
    """
    this is my api aplication by kanha
    """
    return {"message":"Hello, World"} # Defining a function that returns a JSON response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
