from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User

async def create_user(db: AsyncSession, user: User):
    try:
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    except:
        await db.rollback()
        raise

async def get_user_by_mail(db: AsyncSession, email: str):
    res = await db.execute(
        select(User).where(User.email == email)
    )
    return res.scalar_one_or_none()

async def get_user_by_id(db: AsyncSession, id: int):
    res = await db.execute(
        select(User).where(User.id == id)
    )
    return res.scalar_one_or_none()