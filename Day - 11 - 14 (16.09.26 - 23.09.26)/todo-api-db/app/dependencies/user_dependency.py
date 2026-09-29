import uuid
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.config import JWT_ALGORITHM, JWT_SECRET
from app.db.database import get_db
from app.errors import ForbiddenError, NotAuthenticatedError
from app.models.user import User
from app.repositories import user_repo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id_str = payload.get("sub")
        if user_id_str is None:
            raise NotAuthenticatedError(message="Could not validate credentials")
        user_id = uuid.UUID(user_id_str)
    except (JWTError, ValueError):
        raise NotAuthenticatedError(message="Could not validate credentials")

    user = await user_repo.get_user_by_id(db, user_id)
    if user is None:
        raise NotAuthenticatedError(message="Could not validate credentials")
    if not user.is_active:
        raise ForbiddenError(message="Inactive user account")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]