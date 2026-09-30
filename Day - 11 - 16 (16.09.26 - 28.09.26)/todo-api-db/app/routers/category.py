from uuid import UUID
from fastapi import APIRouter

from app.dependencies.db_dependency import DBDependency
from app.dependencies.user_dependency import CurrentUser
from app.schemas.common_schema import SuccessResponse
from app.schemas.category_schema import CategoryIn, CategoryOut
from app.schemas.todo_schema import TodoOut
from app.services import category_service
from app.utils.responses import success_response

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=SuccessResponse[CategoryOut], status_code=201)
async def create_category(
    category: CategoryIn,
    db: DBDependency,
    current_user: CurrentUser,
):
    new_cat = await category_service.create_category(db, category.name, current_user.id)
    return success_response(data=new_cat, message="Category created successfully")


@router.get("/", response_model=SuccessResponse[list[CategoryOut]])
async def get_categories(db: DBDependency, current_user: CurrentUser):
    cats = await category_service.get_categories(db, current_user.id)
    return success_response(data=cats, message="Categories retrieved successfully")


@router.get("/{id}", response_model=SuccessResponse[CategoryOut])
async def get_category(
    id: UUID,
    db: DBDependency,
    current_user: CurrentUser,
):
    cat = await category_service.get_category(db, id, current_user.id)
    return success_response(data=cat, message="Category retrieved successfully")


@router.put("/{id}", response_model=SuccessResponse[CategoryOut])
async def update_category(
    id: UUID,
    category: CategoryIn,
    db: DBDependency,
    current_user: CurrentUser,
):
    updated = await category_service.update_category(
        db, id, category.name, current_user.id
    )
    return success_response(data=updated, message="Category updated successfully")


@router.delete("/{id}", response_model=SuccessResponse[None])
async def delete_category(
    id: UUID,
    db: DBDependency,
    current_user: CurrentUser,
):
    await category_service.delete_category(db, id, current_user.id)
    return success_response(data=None, message="Category deleted successfully")


@router.get("/{id}/todos", response_model=SuccessResponse[list[TodoOut]])
async def get_todos_by_category(
    id: UUID,
    db: DBDependency,
    current_user: CurrentUser,
):
    todos = await category_service.get_todos_by_category(db, id, current_user.id)
    return success_response(
        data=todos, message="Todos for category retrieved successfully"
    )


@router.delete("/{id}/todos", response_model=SuccessResponse[dict])
async def delete_todos_by_category(
    id: UUID,
    db: DBDependency,
    current_user: CurrentUser,
):
    res = await category_service.delete_todos_by_category(db, id, current_user.id)
    return success_response(
        data=res, message="All todos for category deleted successfully"
    )