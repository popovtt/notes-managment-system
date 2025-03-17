from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Note


async def notes_list(session: AsyncSession):
    stmt = select(Note.title)
    result = await session.execute(stmt)
    notes = [row[0] for row in result.all()]

    if not notes:
        raise HTTPException(
            status_code=404,
            detail="No notes found"
        )

    return notes
