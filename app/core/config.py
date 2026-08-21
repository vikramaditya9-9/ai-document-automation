"""Application configuration management"""

from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration from environment variables"""

    # Application
    app_name: str = "DocuFlow AI"
    debug: bool = False

    # Database
    database_url: str = "sqlite:///./test.db"

    # JWT
    secret_key: str = "your-super-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # AI Provider
    ai_provider: str = "mock"  # 'mock', 'openai', etc.
    ai_api_key: Optional[str] = None
    ai_model: Optional[str] = None

    # File Upload
    max_upload_size_mb: int = 10
    upload_directory: str = "uploads/"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
