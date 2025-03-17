from sqlalchemy import select, func, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import NoteVersion, Note
from src.api.notes.schemas import NoteUpdateSchema


async def read_all_notes_versions(session: AsyncSession) -> Sequence[NoteVersion]:
    stmt = select(NoteVersion).order_by(NoteVersion.id)
    res = await session.execute(stmt)
    notes_versions = res.scalars().all()
    return notes_versions


async def read_versions_by_note_id(session: AsyncSession, note_id: int):
    stmt = select(NoteVersion).where(NoteVersion.note_id == note_id)
    res = await session.execute(stmt)
    notes_versions = res.scalars().all()
    return notes_versions


async def create_last_version(session: AsyncSession, note: Note, note_in: NoteUpdateSchema):
    stmt = select(NoteVersion).where(
        NoteVersion.version_id == select(func.max(NoteVersion.version_id))
        .where(NoteVersion.note_id == note.id)
        .scalar_subquery()
    )
    res = await session.execute(stmt)
    last_version = res.scalar()
    session.add(NoteVersion(
        title=note_in.title,
        note_id=note.id,
        version_id=last_version.version_id + 1,
        created_at=note.created_at,
        updated_at=note.updated_at,
        summary=note.summary
    ))
    await session.commit()


async def create_note_version(session: AsyncSession, note: Note):
    note_version = NoteVersion(title=note.title, note_id=note.id, created_at=note.created_at, updated_at=note.updated_at, summary=note.summary)
    session.add(note_version)
    await session.commit()
