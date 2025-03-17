import pytest

from contextlib import nullcontext as does_not_raise
from httpx import AsyncClient, ASGITransport
from http.client import HTTPException

from src.main import app
from src.models import Base, db_helper


@pytest.fixture(scope="session", autouse=True)
async def test_db_setup():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
        await conn.run_sync(Base.metadata.drop_all)


class TestNotesViews:
    @pytest.mark.asyncio
    async def test_get_notes(self):
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://127.0.0.1:8000"
        ) as ac:
            response = await ac.get("/api/v1/notes/")
            data = response.json()
            assert response.status_code == 200
            assert len(data) == 3

    @pytest.mark.asyncio
    async def test_post_note(self):
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://127.0.0.1:8000"
        ) as ac:
            payload = {"title": "The only limit to our realization."}
            response = await ac.post(url="/api/v1/notes/", json=payload)
            assert response.status_code == 201
            data = response.json()
            assert data["title"] == payload["title"]

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "note_id, expectation",
        [
            (2, does_not_raise()),
            (5, pytest.raises(HTTPException)),
        ]
    )
    async def test_patch_note(self, note_id, expectation):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://127.0.0.1:8000"
        ) as ac:
            with expectation:
                new_payload = {"title": "The only limit smth."}
                response = await ac.patch(url=f"/api/v1/notes/?note_id={note_id}",json=new_payload)
                data = response.json()
                assert response.status_code == 200
                assert data["title"] == new_payload["title"]

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "note_id, expectation",
        [
            (2, does_not_raise()),
            (10, pytest.raises(HTTPException, match="Note not found")),
        ]
    )
    async def test_delete_note(self, note_id, expectation):
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://127.0.0.1:8000"
        ) as ac:
            with expectation:
                response = await ac.delete(url=f"/api/v1/notes/?note_id={note_id}")
                assert response.status_code == 204

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "note_id, expectation",
        [
            (3, does_not_raise()),
            (10, pytest.raises(HTTPException, match="Note not found")),
        ]
    )
    async def test_get_note_by_id(self, note_id, expectation):
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://127.0.0.1:8000"
        ) as ac:
            with expectation:
                response = await ac.get(url=f"/api/v1/notes/{note_id}")
                data = response.json()
                assert response.status_code == 200
                assert data["title"] == "The only limit to our realization of tomorrow is our doubts of today."
