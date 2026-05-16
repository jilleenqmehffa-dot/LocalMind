import os
from functools import lru_cache

from dotenv import load_dotenv


load_dotenv()


class Settings:
    app_name: str = os.getenv("APP_NAME", "LocalMind")
    app_env: str = os.getenv("APP_ENV", "development")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_base_url: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    default_chat_model: str = os.getenv("DEFAULT_CHAT_MODEL", "gpt-4.1-mini")


@lru_cache
def get_settings() -> Settings:
    return Settings()
