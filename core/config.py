from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    BOT_TOKEN: str
    BLOCKCYPHER_TOKEN: str
    ADMIN_IDS: List[int] = []
    BASE_URL: str = ""
    DATABASE_URL: str = "sqlite+aiosqlite:///dev.db"

    model_config = {"env_file": ".env"}

settings = Settings()