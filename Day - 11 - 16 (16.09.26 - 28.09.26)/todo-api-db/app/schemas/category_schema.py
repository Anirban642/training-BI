from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class CategoryIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class CategoryOut(BaseModel):
    id: UUID
    name: str
    model_config = ConfigDict(from_attributes=True)