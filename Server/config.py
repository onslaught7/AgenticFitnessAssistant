from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import List


class Settings(BaseSettings):
    # API Keys
    OPENAI_API_KEY: str

    # CORS 
    allowed_origins: List[str] = ["http://localhost:3000", "http://localhost:5173"]

    # load the .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    ) 

    # check key
    @property
    def is_openai_configured(self) -> bool:
        return bool(self.OPENAI_API_KEY and len(self.OPENAI_API_KEY) > 10)


@lru_cache
def get_settings() -> Settings:
    return Settings()


# Global settings instance for non-dependency usage.
settings = get_settings()