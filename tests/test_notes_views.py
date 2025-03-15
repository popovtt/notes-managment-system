import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app


@pytest.mark.asyncio
async def test_get_notes():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://localhost:8000"
    ) as async_client:
        response = await async_client.get("/api/v1/notes/")
        data = response.json()
        assert data == []
