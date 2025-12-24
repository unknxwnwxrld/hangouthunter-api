from fastapi import FastAPI
from app.routers import health, predict, gemini, users

app = FastAPI()
app.include_router(health.router)
app.include_router(users.router)
# app.include_router(predict.router, prefix="/api/v1")
app.include_router(gemini.router)