from fastapi import FastAPI

from app.api import api_router
from app.core import success_response

app = FastAPI(title="LocalMind")

app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, object]:
    return success_response({"status": "ok"})
