from fastapi import APIRouter, Query

from app.dependencies.db_dependency import DBDependency
from app.dependencies.user_dependency import CurrentUser
from app.schemas.schemas import TodoIn, TodoOut, TodoUpdate
from app.services import services

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=TodoOut, status_code=201)
async def create_todo(
    todo: TodoIn,
    db: DBDependency,
    current_user: CurrentUser,
):
    return await services.create_todo(
        db,
        todo.title,
        todo.description,
        todo.category_id,
        current_user.id,
    )


@router.get("/", response_model=list[TodoOut])
async def get_todos(
    db: DBDependency,
    current_user: CurrentUser,
    completed: bool | None = None,
    search: str | None = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
):
    return await services.get_todos(
        db,
        current_user.id,
        completed,
        search,
        page,
        limit
    )


@router.get("/stats")
async def get_todo_stats(db: DBDependency, current_user: CurrentUser):
    return await services.get_todo_stats(db, current_user.id)


@router.get("/{id}", response_model=TodoOut)
async def get_todo(
    id: int,
    db: DBDependency,
    current_user: CurrentUser,
):
    return await services.get_todo(db, id, current_user.id)


@router.put("/{id}", response_model=TodoOut)
async def update_todo(
    id: int,
    todo: TodoUpdate,
    db: DBDependency,
    current_user: CurrentUser,
):
    return await services.update_todo(
        db,
        id,
        todo.title,
        todo.description,
        todo.isDone,
        todo.category_id,
        current_user.id,
    )


@router.delete("/{id}")
async def delete_todo(
    id: int,
    db: DBDependency,
    current_user: CurrentUser,
):
    return await services.delete_todo(db, id, current_user.id)
