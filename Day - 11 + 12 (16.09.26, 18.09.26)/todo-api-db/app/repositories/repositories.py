from sqlalchemy import delete, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Category, Todo


async def create_category(db: AsyncSession, name: str):
    category = Category(name=name)
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category


async def get_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()


async def get_category(db: AsyncSession, id: int):
    result = await db.execute(select(Category).where(Category.id == id))
    return result.scalar_one_or_none()


async def get_category_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Category).where(Category.name == name))
    return result.scalar_one_or_none()


async def get_category_by_name_except(db: AsyncSession, name: str, id: int):
    result = await db.execute(
        select(Category).where(Category.name == name, Category.id != id)
    )
    return result.scalar_one_or_none()


async def update_category(db: AsyncSession, category: Category, name: str):
    category.name = name
    await db.commit()
    await db.refresh(category)
    return category


async def delete_category(db: AsyncSession, category: Category):
    await db.delete(category)
    await db.commit()


async def create_todo(db: AsyncSession, title: str, description: str, category_id: int):
    todo = Todo(
        title=title, description=description, isDone=False, category_id=category_id
    )
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo


async def get_todos(
    db: AsyncSession,
    completed: bool | None = None,
    search: str | None = None,
    page: int = 1,
    limit: int = 10,
):
    query = select(Todo)
    if completed is not None:
        query = query.where(Todo.isDone == completed)
    if search:
        search = f"%{search}%"
        query = query.where(
            or_(Todo.title.ilike(search), Todo.description.ilike(search))
        )
    offset = (page - 1) * limit
    query = query.offset(offset).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


async def get_todo(db: AsyncSession, id: int):
    result = await db.execute(select(Todo).where(Todo.id == id))
    return result.scalar_one_or_none()


async def update_todo(
    db: AsyncSession,
    todo: Todo,
    title: str,
    description: str,
    isDone: bool,
    category_id: int,
):
    todo.title = title
    todo.description = description
    todo.isDone = isDone
    todo.category_id = category_id
    await db.commit()
    await db.refresh(todo)
    return todo


async def delete_todo(db: AsyncSession, todo: Todo):
    await db.delete(todo)
    await db.commit()


async def get_todos_by_category(db: AsyncSession, category_id: int):
    result = await db.execute(select(Todo).where(Todo.category_id == category_id))
    return result.scalars().all()


async def delete_todos_by_category(db: AsyncSession, category_id: int):
    result = await db.execute(delete(Todo).where(Todo.category_id == category_id))
    await db.commit()
    return result.rowcount


async def get_todo_stats(db: AsyncSession):
    total = await db.scalar(select(func.count()).select_from(Todo))
    completed = await db.scalar(
        select(func.count()).select_from(Todo).where(Todo.isDone == True)
    )
    pending = total - completed
    return total, completed, pending
