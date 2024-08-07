from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
	DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/sql_app.db"
	db_echo: bool = True
	APP_PORT: int
	POSTGRES_PORT: str
	POSTGRES_USER: str
	POSTGRES_PASSWORD: str
	POSTGRES_NAME: str

	class Config:
		env_file = BASE_DIR / ".env"


settings = Settings()
