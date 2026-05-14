from fastapi import APIRouter

from app.core import success_response

api_router = APIRouter()


@api_router.get("/health")
async def health_check() -> dict[str, object]:
    return success_response({"status": "ok"})
