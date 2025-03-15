from sqlalchemy import Sequence, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Note


async def read_notes(session: AsyncSession):
    stmt = select(Note)
    res = await session.execute(stmt)
    notes = res.scalars().all()
    return notes
