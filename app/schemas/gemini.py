from pydantic import BaseModel, Field
from typing import List

class Venue(BaseModel):
    name: str = Field(..., description="Название заведения")
    cuisine: str = Field(..., description="Тип кухни")
    why_visit: str = Field(..., description="Почему стоит посетить")
    address_hint: str = Field(..., description="Подсказка по адресу (район, улица, ориентир)")

class VenuesResponse(BaseModel):
    venues: List[Venue] = Field(
        ...,
        min_length=10,
        max_length=20,
        description="Список рекомендованных заведений (10–20 штук)"
    )

class RecommendationRequest(BaseModel):
    city: str = Field(..., description="Город", examples=["Москва", "Санкт-Петербург"])
    lang: str = Field("русский", description="Язык ответа", examples=["русский", "английский"])
    criteria: str = Field(
        ...,
        description="Критерии поиска",
        examples=[
            "вегетарианская кухня, уютная атмосфера, недорого",
            "морепродукты, вид на воду, премиум",
            "кофейни с десертами, центр города"
        ]
    )