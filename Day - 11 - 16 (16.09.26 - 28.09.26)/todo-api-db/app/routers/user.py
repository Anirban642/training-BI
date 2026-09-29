from fastapi import APIRouter, BackgroundTasks

from app.dependencies.db_dependency import DBDependency
from app.dependencies.user_dependency import CurrentUser
from app.schemas.common_schema import SuccessResponse
from app.schemas.user_schema import Credentials, TokenResponse, UserCreate, UserResponse
from app.services import user_service
from app.utils.responses import success_response
from app.utils.mailer import send_welcome_email

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=SuccessResponse[UserResponse], status_code=201)
async def register(
    user_data: UserCreate,
    background_tasks: BackgroundTasks,
    db: DBDependency,
):
    new_user = await user_service.create_user(db, user_data.name, user_data.email, user_data.password)
    # Send email in background
    background_tasks.add_task(send_welcome_email, new_user.email, new_user.name)
    return success_response(data=new_user, message="User registered successfully")


@router.post("/login", response_model=SuccessResponse[TokenResponse])
async def login(
    credentials: Credentials,
    db: DBDependency,
):
    token_data = await user_service.login(
        db, credentials.email, credentials.password
    )
    return success_response(data=token_data, message="Login successful")


@router.get("/me", response_model=SuccessResponse[UserResponse])
async def get_me(curr_user: CurrentUser):
    return success_response(
        data=curr_user, message="Current user profile retrieved"
    )