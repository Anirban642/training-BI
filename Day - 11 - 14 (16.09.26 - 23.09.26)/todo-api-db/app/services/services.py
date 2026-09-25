from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import repositories


async def create_category(db: AsyncSession, name: str, user_id: int):
    existing = await repositories.get_category_by_name(db, name, user_id)
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")
    return await repositories.create_category(db, name, user_id)


async def get_categories(db: AsyncSession, user_id: int):
    return await repositories.get_categories(db, user_id)


async def get_category(db: AsyncSession, id: int, user_id: int):
    category = await repositories.get_category(db, id, user_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


async def update_category(db: AsyncSession, id: int, name: str, user_id: int):
    category = await repositories.get_category(db, id, user_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    existing = await repositories.get_category_by_name_except(db, name, id, user_id)
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")
    return await repositories.update_category(db, category, name)


async def delete_category(db: AsyncSession, id: int, user_id: int):
    category = await repositories.get_category(db, id, user_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    todos = await repositories.get_todos_by_category(db, id, user_id)
    if todos:
        raise HTTPException(status_code=400, detail="Cannot delete category with todos")
    await repositories.delete_category(db, category)
    return {"message": "Category deleted"}


async def create_todo(
    db: AsyncSession, title: str, description: str, category_id: int, user_id: int
):
    category = await repositories.get_category(db, category_id, user_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return await repositories.create_todo(db, title, description, category_id, user_id)


async def get_todos(
    db: AsyncSession,
    user_id: int,
    completed: bool | None = None,
    search: str | None = None,
    page: int = 1,
    limit: int = 10,
):
    return await repositories.get_todos(db, user_id, completed, search, page, limit)


async def get_todo(db: AsyncSession, id: int, user_id: int):
    todo = await repositories.get_todo(db, id, user_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


async def update_todo(
    db: AsyncSession,
    id: int,
    title: str,
    description: str,
    isDone: bool,
    category_id: int,
    user_id: int,
):
    todo = await repositories.get_todo(db, id, user_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    category = await repositories.get_category(db, category_id, user_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return await repositories.update_todo(
        db, todo, title, description, isDone, category_id
    )


async def delete_todo(db: AsyncSession, id: int, user_id: int):
    todo = await repositories.get_todo(db, id, user_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    await repositories.delete_todo(db, todo)
    return {"message": "Todo deleted"}


async def get_todos_by_category(db: AsyncSession, id: int, user_id: int):
    category = await repositories.get_category(db, id, user_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return await repositories.get_todos_by_category(db, id, user_id)


async def delete_todos_by_category(db: AsyncSession, id: int, user_id: int):
    category = await repositories.get_category(db, id, user_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    deleted = await repositories.delete_todos_by_category(db, id, user_id)
    return {"message": "Todos deleted", "deleted_count": deleted}


async def get_todo_stats(db: AsyncSession, user_id: int):
    total, completed, pending = await repositories.get_todo_stats(db, user_id)
    return {"total": total, "completed": completed, "pending": pending}
