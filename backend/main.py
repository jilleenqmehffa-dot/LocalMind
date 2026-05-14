from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api import api_router
from app.core import success_response
from app.core.handlers import (
    http_exception_handler,
    internal_exception_handler,
    validation_exception_handler,
)

app = FastAPI(title="LocalMind")

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, internal_exception_handler)

app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, object]:
    return success_response({"status": "ok"})
