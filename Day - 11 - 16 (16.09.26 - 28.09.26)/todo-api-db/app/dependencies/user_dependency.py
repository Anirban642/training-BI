import uuid
from typing import Annotated
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.config import JWT_ALGORITHM, JWT_SECRET
from app.db.database import get_db
from app.errors import ForbiddenError, NotAuthenticatedError
from app.models.user import User
from app.repositories import user_repo

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    token = credentials.credentials

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id_str = payload.get("sub")
        token_iat = payload.get("iat")

        if not user_id_str:
            raise NotAuthenticatedError(message="Could not validate credentials")

        user_id = uuid.UUID(user_id_str)
    except (jwt.PyJWTError, ValueError):
        raise NotAuthenticatedError(message="Could not validate credentials")

    user = await user_repo.get_user_by_id(db, user_id)
    if user is None:
        raise NotAuthenticatedError(message="Could not validate credentials")
    if not user.is_active:
        raise ForbiddenError(message="Inactive user account")

    # Invalidate tokens issued prior to password change
    if user.password_changed_at and token_iat:
        if token_iat < int(user.password_changed_at.timestamp()):
            raise NotAuthenticatedError(message="Token has been revoked due to password change")

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]