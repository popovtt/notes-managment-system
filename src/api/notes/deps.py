from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Path, Depends, HTTPException, status

from src.models import db_helper, Note
from . import crud


async def note_by_id(
        note_id: int = Path,
        session: AsyncSession = Depends(db_helper.session_dependency)
) -> Note | None:
    note = await crud.read_note_by_id(session=session, note_id=note_id)
    if note is not None:
        return note

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Note {note_id} not found!"
    )
