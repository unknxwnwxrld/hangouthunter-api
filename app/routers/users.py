from fastapi import APIRouter, HTTPException
from app.models import User

router = APIRouter(
    prefix = "/users",
    tags = ["User"],
)

fake_users_db = {
    1: {
        "id": 3242,
        "tg_tg_user_id": 103234,
        "tg_name": None,
        "tg_surname": None,
        "username": "admin34857",
        "tg_language_code": "ru",
        "tg_premium": True
    },
    2: {
        "id": 435,
        "tg_tg_user_id": 53425,
        "tg_name": "Ivan",
        "tg_surname": None,
        "username": "nbvcncgfdfsg",
        "tg_language_code": "ua",
        "tg_premium": True},
}

@router.get("/{user_id}")
def get_user_by_id(user_id: int) -> dict[str, int | None | str | bool]:
    user = fake_users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
