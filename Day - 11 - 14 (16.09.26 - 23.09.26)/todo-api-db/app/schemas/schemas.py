from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class CategoryIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)

class CategoryOut(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class TodoIn(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=10, max_length=2000)
    category_id: int

class TodoUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=10, max_length=2000)
    isDone: bool
    category_id: int

class TodoOut(BaseModel):
    id: int
    title: str
    description: str
    isDone: bool
    category_id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)