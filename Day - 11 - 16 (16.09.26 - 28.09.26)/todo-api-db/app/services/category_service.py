from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.errors import BadRequestError, ConflictError, NotFoundError
from app.repositories import category_repo, todo_repo


async def create_category(db: AsyncSession, name: str, user_id: UUID):
    existing = await category_repo.get_category_by_name(db, name, user_id)
    if existing:
        raise ConflictError(message="Category already exists")
    return await category_repo.create_category(db, name, user_id)


async def get_categories(db: AsyncSession, user_id: UUID):
    return await category_repo.get_categories(db, user_id)


async def get_category(db: AsyncSession, id: UUID, user_id: UUID):
    category = await category_repo.get_category(db, id, user_id)
    if category is None:
        raise NotFoundError(message="Category not found")
    return category


async def update_category(db: AsyncSession, id: UUID, name: str, user_id: UUID):
    category = await category_repo.get_category(db, id, user_id)
    if category is None:
        raise NotFoundError(message="Category not found")
    existing = await category_repo.get_category_by_name_except(db, name, id, user_id)
    if existing:
        raise ConflictError(message="Category already exists")
    return await category_repo.update_category(db, category, name)


async def delete_category(db: AsyncSession, id: UUID, user_id: UUID):
    category = await category_repo.get_category(db, id, user_id)
    if category is None:
        raise NotFoundError(message="Category not found")
    todos = await todo_repo.get_todos_by_category(db, id, user_id)
    if todos:
        raise BadRequestError(message="Cannot delete category with todos")
    await category_repo.delete_category(db, category)
    return {"message": "Category deleted"}

