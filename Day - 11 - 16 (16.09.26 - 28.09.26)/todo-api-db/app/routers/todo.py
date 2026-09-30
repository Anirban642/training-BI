import math
from uuid import UUID
from fastapi import APIRouter, Query, BackgroundTasks

from app.dependencies.db_dependency import DBDependency
from app.dependencies.user_dependency import CurrentUser
from app.schemas.common_schema import SuccessResponse
from app.schemas.todo_schema import TodoIn, TodoOut, TodoStats, TodoUpdate
from app.services import todo_service
from app.utils.responses import success_response
from app.utils.mailer import send_todos_export_email

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=SuccessResponse[TodoOut], status_code=201)
async def create_todo(
    todo: TodoIn,
    db: DBDependency,
    current_user: CurrentUser,
):
    new_todo = await todo_service.create_todo(
        db,
        todo.title,
        todo.description,
        todo.category_id,
        current_user.id,
    )
    return success_response(data=new_todo, message="Todo created successfully")


@router.get("/", response_model=SuccessResponse[list[TodoOut]])
async def get_todos(
    db: DBDependency,
    current_user: CurrentUser,
    completed: bool | None = None,
    search: str | None = None,
    sort_by: str = Query("id", description="Field to sort by: id, title"),
    order: str = Query("asc", description="Sort direction: asc or desc"),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
):
    items, total = await todo_service.get_todos(
        db,
        current_user.id,
        completed,
        search,
        sort_by,
        order,
        page,
        limit,
    )
    total_pages = math.ceil(total / limit) if limit > 0 else 1
    return success_response(
        data=items,
        message="Todos retrieved successfully",
        meta={
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": total_pages,
            "sort_by": sort_by,
            "order": order,
        },
    )

@router.get("/stats", response_model=SuccessResponse[TodoStats])
async def get_todo_stats(db: DBDependency, current_user: CurrentUser):
    stats = await todo_service.get_todo_stats(db, current_user.id)
    return success_response(data=stats, message="Todo statistics retrieved successfully")


@router.get("/{id}", response_model=SuccessResponse[TodoOut])
async def get_todo(
    id: UUID,
    db: DBDependency,
    current_user: CurrentUser,
):
    todo = await todo_service.get_todo(db, id, current_user.id)
    return success_response(data=todo, message="Todo retrieved successfully")


@router.put("/{id}", response_model=SuccessResponse[TodoOut])
async def update_todo(
    id: UUID,
    todo: TodoUpdate,
    db: DBDependency,
    current_user: CurrentUser,
):
    updated = await todo_service.update_todo(
        db,
        id,
        todo.title,
        todo.description,
        todo.isDone,
        todo.category_id,
        current_user.id,
    )
    return success_response(data=updated, message="Todo updated successfully")


@router.delete("/{id}", response_model=SuccessResponse[None])
async def delete_todo(
    
    id: UUID,
    db: DBDependency,
    current_user: CurrentUser,
):
    await todo_service.delete_todo(db, id, current_user.id)
    return success_response(data=None, message="Todo deleted successfully")

@router.post("/export", response_model=SuccessResponse[None])
async def export_todos(background_tasks: BackgroundTasks, db: DBDependency, current_user: CurrentUser):
    json_data = await todo_service.export_todos_json(db, current_user.id)
    background_tasks.add_task(
        send_todos_export_email,
        current_user.email,
        current_user.name,
        json_data
    )
    return success_response(
        data=None,
        message="Your todos export has been sent to your email"
    )