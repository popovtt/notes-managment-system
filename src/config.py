from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent
env_file = f"{BASE_DIR}/.env"


class EnvSettings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    GEMINI_API_KEY: str

    @property
    def DATABASE_URL_ASYNCPG(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=env_file)


class Settings(BaseSettings):
    env: EnvSettings = EnvSettings()


settings = Settings()
