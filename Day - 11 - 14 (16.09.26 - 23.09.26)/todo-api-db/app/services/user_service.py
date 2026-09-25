from app.exceptions.user_exceptions import EmailAlreadyExistsError, InvalidCredentialsError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories import user_repo

from app.utils.auth import create_access_token
from app.utils.password import hash_password, verify_password

async def create_user(db: AsyncSession, name: str, email: str, password: str):
    existing = await user_repo.get_user_by_mail(db, email)
    if existing:
        raise EmailAlreadyExistsError("Email already registered")
    hashed_password = hash_password(password)
    user = User(name=name, email=email, password=hashed_password)
    return await user_repo.create_user(db, user)


async def login(db: AsyncSession, email: str, password: str):
    user = await user_repo.get_user_by_mail(db, email)
    if user is None or not verify_password(user.password, password):
        raise InvalidCredentialsError("Invalid email or password")
    if not user.is_active:
        raise InvalidCredentialsError("Invalid email or password")
    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer"
    }
