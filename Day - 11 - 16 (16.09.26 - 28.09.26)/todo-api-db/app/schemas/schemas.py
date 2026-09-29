from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class CategoryIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class CategoryOut(BaseModel):
    id: UUID
    name: str
    model_config = ConfigDict(from_attributes=True)


class TodoIn(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=10, max_length=2000)
    category_id: UUID


class TodoUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=10, max_length=2000)
    isDone: bool
    category_id: UUID


class TodoOut(BaseModel):
    id: UUID
    title: str
    description: str
    isDone: bool
    category_id: UUID
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class TodoStats(BaseModel):
    total: int
    completed: int
    pending: int