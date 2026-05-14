from typing import Any


def success_response(data: Any = None, message: str = "ok") -> dict[str, Any]:
    return {
        "success": True,
        "data": data if data is not None else {},
        "message": message,
    }

