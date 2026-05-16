from fastapi import HTTPException, status

from app.core.config import get_settings
from app.schemas.chat import ChatCompletionRequest, ChatCompletionResponse


def _model_to_dict(value: object) -> dict[str, object]:
    if isinstance(value, dict):
        return value

    model_dump = getattr(value, "model_dump", None)
    if callable(model_dump):
        return model_dump(exclude_none=True)

    return {}


def _to_openai_compatible_response(
    response: object,
    requested_model: str,
) -> ChatCompletionResponse:
    data = _model_to_dict(response)

    choices = []
    for index, raw_choice in enumerate(data.get("choices", [])):
        choice = _model_to_dict(raw_choice)
        message = _model_to_dict(choice.get("message", {}))

        choices.append(
            {
                "index": choice.get("index", index),
                "message": message,
                "finish_reason": choice.get("finish_reason"),
                "logprobs": choice.get("logprobs"),
            }
        )

    return ChatCompletionResponse.model_validate(
        {
            "id": data.get("id", ""),
            "object": "chat.completion",
            "created": data.get("created", 0),
            "model": data.get("model", requested_model),
            "choices": choices,
            "usage": data.get("usage"),
            "system_fingerprint": data.get("system_fingerprint"),
        }
    )


async def create_chat_completion(
    request: ChatCompletionRequest,
) -> ChatCompletionResponse:
    if request.stream:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Streaming is not supported in module 2",
                "code": "STREAMING_NOT_SUPPORTED",
            },
        )

    settings = get_settings()
    if not settings.openai_api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "OPENAI_API_KEY is not configured",
                "code": "OPENAI_API_KEY_MISSING",
            },
        )

    try:
        from openai import AsyncOpenAI
    except ImportError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "openai package is not installed",
                "code": "OPENAI_PACKAGE_MISSING",
            },
        ) from exc

    client = AsyncOpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url,
    )

    payload = {
        "model": request.model,
        "messages": [message.model_dump() for message in request.messages],
        "stream": False,
    }
    if request.temperature is not None:
        payload["temperature"] = request.temperature
    if request.max_tokens is not None:
        payload["max_tokens"] = request.max_tokens

    try:
        response = await client.chat.completions.create(**payload)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={
                "message": "Chat completion request failed",
                "code": "CHAT_COMPLETION_FAILED",
                "details": {"error": str(exc)},
            },
        ) from exc

    return _to_openai_compatible_response(response, request.model)
