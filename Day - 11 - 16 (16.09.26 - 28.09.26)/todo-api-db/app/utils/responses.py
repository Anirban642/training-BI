from typing import Any, TypeVar

T = TypeVar("T")


def success_response(
    data: T | None = None,
    message: str = "Operation successful",
    meta: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "success": True,
        "message": message,
        "data": data,
        "meta": meta,
    }