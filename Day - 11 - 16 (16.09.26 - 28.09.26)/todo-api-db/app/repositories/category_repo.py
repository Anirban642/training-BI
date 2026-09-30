from uuid import UUID
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category



async def create_category(db: AsyncSession, name: str, user_id: UUID):
    try:
        category = Category(name=name, user_id=user_id)
        db.add(category)
        await db.commit()
        await db.refresh(category)
        return category
    except Exception:
        await db.rollback()
        raise


async def get_categories(db: AsyncSession, user_id: UUID):
    result = await db.execute(select(Category).where(Category.user_id == user_id))
    return result.scalars().all()


async def get_category(db: AsyncSession, id: UUID, user_id: UUID):
    result = await db.execute(
        select(Category).where(Category.id == id, Category.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def get_category_by_name(db: AsyncSession, name: str, user_id: UUID):
    result = await db.execute(
        select(Category).where(Category.name == name, Category.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def get_category_by_name_except(
    db: AsyncSession, name: str, id: UUID, user_id: UUID
):
    result = await db.execute(
        select(Category).where(
            Category.name == name,
            Category.id != id,
            Category.user_id == user_id,
        )
    )
    return result.scalar_one_or_none()


async def update_category(db: AsyncSession, category: Category, name: str):
    try:
        category.name = name
        await db.commit()
        await db.refresh(category)
        return category
    except Exception:
        await db.rollback()
        raise


async def delete_category(db: AsyncSession, category: Category):
    try:
        await db.delete(category)
        await db.commit()
    except Exception:
        await db.rollback()
        raise