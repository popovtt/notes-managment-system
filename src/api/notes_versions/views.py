from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import db_helper
from . import crud


router = APIRouter(tags=["Notes Versions"])


@router.get("/")
async def get_notes_versions(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.read_all_notes_versions(session=session)


@router.get("/{note_id}")
async def get_versions_by_note_id(note_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.read_versions_by_note_id(session=session, note_id=note_id)
