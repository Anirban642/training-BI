from typing import Any
from pydantic import BaseModel


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Any = None


class ErrorResponse(BaseModel):
    error: ErrorDetail


class AppError(Exception):  
    status_code: int = 500
    code: str = "INTERNAL_SERVER_ERROR"
    message: str = "An unexpected error occurred"

    def __init__(self, message: str | None = None, details: Any = None):
        self.message = message or self.__class__.message
        self.details = details
        super().__init__(self.message)


class NotFoundError(AppError):
    status_code: int = 404
    code: str = "NOT_FOUND"
    message: str = "Resource not found"


class ConflictError(AppError):
    status_code: int = 409
    code: str = "CONFLICT"
    message: str = "Resource conflict"


class BadRequestError(AppError):
    status_code: int = 400
    code: str = "BAD_REQUEST"
    message: str = "Bad request"


class InvalidCredentialsError(AppError):
    status_code: int = 401
    code: str = "INVALID_CREDENTIALS"
    message: str = "Invalid email or password"


class NotAuthenticatedError(AppError):
    status_code: int = 401
    code: str = "NOT_AUTHENTICATED"
    message: str = "Could not validate credentials"


class ForbiddenError(AppError):
    status_code: int = 403
    code: str = "FORBIDDEN"
    message: str = "You do not have permission to access this resource"