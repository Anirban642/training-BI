from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from app.models.user import User
from app.config.config import JWT_ALGORITHM, JWT_SECRET
from app.db.database import get_db
from app.repositories import user_repo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    cred_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise cred_exception
        user_id = int(user_id)
    except (JWTError, ValueError):
        raise cred_exception
    
    user = await user_repo.get_user_by_id(db, user_id)
    if user is None:
        raise cred_exception
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Inactive user")
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]