from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.schemas import CategoryIn, CategoryOut, TodoOut
from app.services import services

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryOut, status_code=201)
async def create_category(
    category: CategoryIn,
    db: AsyncSession = Depends(get_db)
):
    return await services.create_category(db, category.name)


@router.get("/", response_model=list[CategoryOut])
async def get_categories(db: AsyncSession = Depends(get_db)):
    return await services.get_categories(db)


@router.get("/{id}", response_model=CategoryOut)
async def get_category(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    return await services.get_category(db, id)


@router.put("/{id}", response_model=CategoryOut)
async def update_category(
    id: int,
    category: CategoryIn,
    db: AsyncSession = Depends(get_db)
):
    return await services.update_category(db, id, category.name)


@router.delete("/{id}")
async def delete_category(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    return await services.delete_category(db, id)


@router.get("/{id}/todos", response_model=list[TodoOut])
async def get_todos_by_category(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    return await services.get_todos_by_category(db, id)


@router.delete("/{id}/todos")
async def delete_todos_by_category(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    return await services.delete_todos_by_category(db, id)