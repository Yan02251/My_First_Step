from pydantic_settings import BaseSettings  # ✅ 올바른 import
import os
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv(".env")

class Settings(BaseSettings):
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()
