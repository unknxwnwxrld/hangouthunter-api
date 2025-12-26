from fastapi import APIRouter, HTTPException
from app.schemas.gemini import RecommendationRequest, VenuesResponse
from app.services.get_recommendations import get_recommendations

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"]
)

@router.post("/venues", response_model=VenuesResponse)
async def recommend_venues(request: RecommendationRequest):
    result = await get_recommendations(
        city=request.city,
        lang=request.lang,
        criteria=request.criteria
    )

    if not result.venues:
        raise HTTPException(status_code=500, detail="Unable to get recommendations")

    return result