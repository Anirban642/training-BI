from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.schemas import TodoIn, TodoOut, TodoUpdate
from app.services import services

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=TodoOut, status_code=201)
async def create_todo(
    todo: TodoIn,
    db: AsyncSession = Depends(get_db)
):
    return await services.create_todo(
        db,
        todo.title,
        todo.description,
        todo.category_id
    )


@router.get("/", response_model=list[TodoOut])
async def get_todos(
    completed: bool | None = None,
    search: str | None = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: AsyncSession = Depends(get_db)
):
    return await services.get_todos(
        db,
        completed,
        search,
        page,
        limit
    )


@router.get("/stats")
async def get_todo_stats(db: AsyncSession = Depends(get_db)):
    return await services.get_todo_stats(db)


@router.get("/{id}", response_model=TodoOut)
async def get_todo(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    return await services.get_todo(db, id)


@router.put("/{id}", response_model=TodoOut)
async def update_todo(
    id: int,
    todo: TodoUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await services.update_todo(
        db,
        id,
        todo.title,
        todo.description,
        todo.isDone,
        todo.category_id
    )


@router.delete("/{id}")
async def delete_todo(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    return await services.delete_todo(db, id)