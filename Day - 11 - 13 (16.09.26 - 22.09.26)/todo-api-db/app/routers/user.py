from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse, TokenResponse
from app.services import user_service

from app.dependencies.user_dependency import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

# register
@router.post("/register", response_model=UserResponse, status_code=201)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(
        db, user.name, user.email, user.password
    )
    
# login
@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    return await user_service.login(
        db, form_data.username, form_data.password
    )    
    
# me
@router.get("/me", response_model=UserResponse)
async def get_me(
    curr_user = Depends(get_current_user)
):
    return curr_user
    
    
    