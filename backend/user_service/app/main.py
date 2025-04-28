from fastapi import FastAPI
import uvicorn

from . import models
from .database import engine
from .routes import router

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="User Authentication Service",
    description="A FastAPI service for user authentication with JWT tokens",
    version="1.0.0"
)

# Include routers
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)