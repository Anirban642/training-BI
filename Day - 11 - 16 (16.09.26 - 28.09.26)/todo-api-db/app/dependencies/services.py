from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.repositories.user_repo import UserRepository  # or repo module/class
# Adjust to your repo/service classes:
from app.services.user_service import UserService

DBDep = Annotated[AsyncSession, Depends(get_db)]

def get_user_service(db: DBDep) -> UserService:
    return UserService(db)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]