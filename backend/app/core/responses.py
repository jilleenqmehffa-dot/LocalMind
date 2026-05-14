from typing import Any


def success_response(data: Any = None, message: str = "ok") -> dict[str, Any]:
    return {
        "success": True,
        "data": data if data is not None else {},
        "message": message,
    }


def error_response(
    message: str,
    code: str,
    details: Any = None,
) -> dict[str, Any]:
    return {
        "success": False,
        "data": {},
        "message": message,
        "error": {
            "code": code,
            "details": details if details is not None else {},
        },
    }
