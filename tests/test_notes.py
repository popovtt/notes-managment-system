import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app


class TestNotesViews:
    @pytest.mark.asyncio
    async def test_get_notes(self):
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://localhost:8000"
        ) as async_client:
            response = await async_client.get("/api/v1/notes/")
            data = response.json()
            assert response.status_code == 200
            assert len(data) == 4


    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "id, res",
        [
            (28,{"title": "test1","id": 23}),
            (1, {"detail": "Note not found"}),
        ]
    )
    async def test_get_note_by_id(self, id, res):
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://localhost:8000"
        ) as async_client:
            response = await async_client.get(f"/api/v1/notes/{id}")
            data = response.json()
            assert data == res

