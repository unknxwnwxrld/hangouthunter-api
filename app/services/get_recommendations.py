from google import genai
from google.genai import types
from app.schemas.gemini import VenuesResponse
import os

async def get_recommendations(city: str, lang: str, criteria: str) -> VenuesResponse:
    prompt = f"""
    Ты — локальный гастро-эксперт и фуд-блогер в городе {city}.
    Специализация: уникальные, атмосферные места с высоким рейтингом, без туристических ловушек.

    Язык ответа: {lang}.

    КРИТЕРИИ: Найди 10–20 заведений, максимально соответствующих: {criteria}.

    Правила:
    1. ТОЛЬКО реальные существующие заведения (знания на 2025 год).
    2. Никаких крупных сетей, если не указано.
    3. Разнообразие цен, но всегда высокое качество.
    4. Приоритет уникальной концепции, атмосфере, интерьеру, сервису или вкусу.

    Верни ТОЛЬКО JSON по схеме (без ```json, без пояснений).
    """

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    async with client.aio as async_client:
        try:
            response = await async_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=VenuesResponse,
                    temperature=0.7,
                )
            )

            return response.parsed

        except Exception as e:
            print(f"Ошибка Gemini API: {e}")
            return VenuesResponse(venues=[])