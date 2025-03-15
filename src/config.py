from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


env_file = f"{Path(__file__).parent.parent}/.env"


class DBSettings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str

    @property
    def DATABASE_URL_ASYNCPG(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=env_file)


class Settings(BaseSettings):
    db: DBSettings = DBSettings()


settings = Settings()
