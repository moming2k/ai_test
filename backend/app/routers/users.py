from fastapi import APIRouter, HTTPException

from app.data import USERS
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[User])
def list_users() -> list[User]:
    return USERS


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    for user in USERS:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
