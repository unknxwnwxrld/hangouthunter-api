from fastapi import APIRouter, status

router = APIRouter()

@router.get("/health", tags=["monitoring"])
async def health_check():
    return {"status": "healthy", "message": "Healthy"}