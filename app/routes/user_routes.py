from fastapi import APIRouter
from app.models.user_model import User
from app.models.user_schema import UserCreate
from app.database.db import SessionLocal
from app.security.hash import hash_password

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    db = SessionLocal()

    hashed_pw = hash_password(user.password)

    new_user = User(
        username=user.username,
        password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }