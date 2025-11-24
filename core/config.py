from pydantic_settings import BaseSettings
from typing import List
import json

class Settings(BaseSettings):
    BOT_TOKEN: str
    BLOCKCYPHER_TOKEN: str
    ADMIN_IDS: str = "[]"
    BASE_URL: str = ""
    DATABASE_URL: str = "sqlite+aiosqlite:///dev.db"

    model_config = {"env_file": ".env"}

    @property
    def admin_ids_list(self) -> List[int]:
        return json.loads(self.ADMIN_IDS)

settings = Settings()
