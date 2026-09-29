from typing import Any, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "Operation Successful"
    data: T | None = None
    meta: dict[str, Any] | None = None