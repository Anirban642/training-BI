from fastapi import APIRouter, Depends, HTTPException
from app.exceptions.user_exceptions import InvalidCredentialsError, EmailAlreadyExistsError
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies.db_dependency import DBDependency
from app.dependencies.user_dependency import CurrentUser

from app.schemas.user_schema import UserCreate, UserResponse, TokenResponse
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

# register
@router.post("/register", response_model=UserResponse, status_code=201)
async def register(user: UserCreate, db: DBDependency):
    try:
        return await user_service.create_user(
            db, user.name, user.email, user.password
        )
    except EmailAlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=str(e))    
    
# login
@router.post("/login", response_model=TokenResponse)
async def login(
    db: DBDependency,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    try:
        return await user_service.login(
            db, form_data.username, form_data.password
        )
    except InvalidCredentialsError as e:
        raise HTTPException(status_code=401, detail=str(e))        
    
# me
@router.get("/me", response_model=UserResponse)
async def get_me(curr_user: CurrentUser):
    return curr_user
    
    
    