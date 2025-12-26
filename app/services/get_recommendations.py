from google import genai
from google.genai import types
from app.schemas.gemini import VenuesResponse
import os

async def get_recommendations(city: str, lang: str, criteria: str) -> VenuesResponse:
    prompt = f"""
    You are a local food expert and food blogger in {city}.
    Your specialization: unique, atmospheric places with high ratings and authentic experience. You strictly avoid tourist traps and overhyped spots.

    Response language: {lang}.

    TASK: Find 12–18 real establishments that best match the user's request: {criteria}.

    STRICT RULES:
    1. Include ONLY real, currently existing establishments (knowledge as of December 2025).
    2. Exclude large international or federal chains (McDonald's, Starbucks, KFC, Burger King, etc.), unless the user explicitly asks for them.
    3. Provide variety in price levels (from affordable to premium), but always maintain high quality and positive reputation.
    4. Prioritize places with unique concept, outstanding atmosphere, beautiful interior, exceptional service, or signature taste/dishes.
    5. Do not invent or hallucinate places — only those that actually exist.

    OUTPUT FORMAT:
    Return ONLY a valid JSON array of objects (no ```json markers, no additional text, no explanations, no introductions).
    Return only the JSON array, nothing else.
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
            print(f"Gemini API Error: {e}")
            return VenuesResponse(venues=[])