from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(bind=self.engine)

    async def session_dependency(self) -> AsyncGenerator[AsyncGenerator, None]:
        async with self.session_factory() as session:
            yield session
            await session.close()


db_helper = DatabaseHelper(
    url=settings.env.DATABASE_URL_ASYNCPG,
    echo=False,
)
