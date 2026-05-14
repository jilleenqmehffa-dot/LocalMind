from fastapi import FastAPI

from app.api import api_router

app = FastAPI(title="LocalMind")

app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"status": "ok"}
