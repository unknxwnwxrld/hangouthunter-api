from pydantic import BaseModel, Field
from typing import List

class Venue(BaseModel):
    name: str = Field(..., description="Venue name")
    cuisine: str = Field(..., description="Cuisine type")
    why_visit: str = Field(..., description="Why it's worth visiting")
    address_hint: str = Field(..., description="Address hint (district, street, landmark)")

class VenuesResponse(BaseModel):
    venues: List[Venue] = Field(
        ...,
        min_length=10,
        max_length=20,
        description="List of recommended venues (10–20 items)"
    )

class RecommendationRequest(BaseModel):
    city: str = Field(..., description="City", examples=["Moscow", "Saint Petersburg"])
    lang: str = Field("russian", description="Response language", examples=["russian", "english"])
    criteria: str = Field(
        ...,
        description="Search criteria",
        examples=[
            "vegetarian cuisine, cozy atmosphere, affordable",
            "seafood, water view, premium",
            "coffee shops with desserts, city center"
        ]
    )