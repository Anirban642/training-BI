from fastapi import HTTPException
from argon2 import PasswordHasher
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories import user_repo

from app.utils.auth import create_access_token

ph = PasswordHasher()


async def create_user(db: AsyncSession, name: str, email: str, password: str):
    existing = await user_repo.get_user_by_mail(db, email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = ph.hash(password)
    user = User(name=name, email=email, password=hashed_password)
    return await user_repo.create_user(db, user)


async def login(db: AsyncSession, email: str, password: str):
    user = await user_repo.get_user_by_mail(db, email)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    try:
        ph.verify(user.password, password)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer"
    }
