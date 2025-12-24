from pydantic import BaseModel

class User(BaseModel):
    id: int
    tg_user_id: int
    tg_name: str | None = None
    tg_surname: str | None = None
    tg_username: str | None = None
    tg_language_code: str | None = "en"
    tg_premium: bool | None = False

class Venue(BaseModel):
    name: str
    cuisine: str | None = None # venue type
    why_visit: str
    address_hint: str | None = None
    city: str
    country: str
    rating: float | None = None






