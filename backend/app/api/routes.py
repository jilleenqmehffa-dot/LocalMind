from fastapi import APIRouter

from app.core import success_response
from app.schemas.chat import ChatCompletionRequest, ChatCompletionResponse
from app.services.chat_service import create_chat_completion

api_router = APIRouter()


@api_router.get("/health")
async def health_check() -> dict[str, object]:
    return success_response({"status": "ok"})


@api_router.post(
    "/v1/chat/completions",
    response_model=ChatCompletionResponse,
    response_model_exclude_none=True,
)
async def chat_completions(
    request: ChatCompletionRequest,
) -> ChatCompletionResponse:
    return await create_chat_completion(request)
