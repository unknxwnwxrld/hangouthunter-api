from fastapi import FastAPI
from app.routers import health, gemini

app = FastAPI()
app.include_router(health.router)
app.include_router(gemini.router)