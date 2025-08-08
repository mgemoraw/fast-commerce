from pydantic_settings import BaseSettings
import os 


class Settings(BaseSettings):
    app_name: str = "FastAPI Application"
    debug: bool = True
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    return Settings()