import json
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.errors import NotFoundError
from app.repositories import todo_repo, category_repo



async def create_todo(
    db: AsyncSession, title: str, description: str, category_id: UUID, user_id: UUID
):
    category = await category_repo.get_category(db, category_id, user_id)
    if category is None:
        raise NotFoundError(message="Category not found")
    return await todo_repo.create_todo(db, title, description, category_id, user_id)


async def get_todos(
    db: AsyncSession,
    user_id: UUID,
    completed: bool | None = None,
    search: str | None = None,
    sort_by: str = "id",
    order: str = "asc",
    page: int = 1,
    limit: int = 10,
):
    return await todo_repo.get_todos(db, user_id, completed, search, sort_by, order, page, limit)


async def get_todo(db: AsyncSession, id: UUID, user_id: UUID):
    todo = await todo_repo.get_todo(db, id, user_id)
    if todo is None:
        raise NotFoundError(message="Todo not found")
    return todo


async def update_todo(
    db: AsyncSession,
    id: UUID,
    title: str,
    description: str,
    isDone: bool,
    category_id: UUID,
    user_id: UUID,
):
    todo = await todo_repo.get_todo(db, id, user_id)
    if todo is None:
        raise NotFoundError(message="Todo not found")
    category = await category_repo.get_category(db, category_id, user_id)
    if category is None:
        raise NotFoundError(message="Category not found")
    return await todo_repo.update_todo(
        db, todo, title, description, isDone, category_id
    )


async def delete_todo(db: AsyncSession, id: UUID, user_id: UUID):
    todo = await todo_repo.get_todo(db, id, user_id)
    if todo is None:
        raise NotFoundError(message="Todo not found")
    await todo_repo.delete_todo(db, todo)
    return {"message": "Todo deleted"}


async def get_todos_by_category(db: AsyncSession, id: UUID, user_id: UUID):
    category = await category_repo.get_category(db, id, user_id)
    if category is None:
        raise NotFoundError(message="Category not found")
    return await todo_repo.get_todos_by_category(db, id, user_id)


async def delete_todos_by_category(db: AsyncSession, id: UUID, user_id: UUID):
    category = await category_repo.get_category(db, id, user_id)
    if category is None:
        raise NotFoundError(message="Category not found")
    deleted = await todo_repo.delete_todos_by_category(db, id, user_id)
    return {"deleted_count": deleted}


async def get_todo_stats(db: AsyncSession, user_id: UUID):
    total, completed, pending = await todo_repo.get_todo_stats(db, user_id)
    return {"total": total, "completed": completed, "pending": pending}


async def export_todos_json(db: AsyncSession, user_id: UUID) -> str:
    todos = await todo_repo.get_all_todos(db, user_id)
    todos_data = [
        {
            "id": str(t.id),
            "title": t.title,
            "description": t.description,
            "isDone": t.isDone,
            "category_id": str(t.category_id) if t.category_id else None,
        }
        for t in todos
    ]
    return json.dumps(todos_data, indent=2)