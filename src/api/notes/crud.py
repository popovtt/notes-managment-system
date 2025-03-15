from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.notes.schemas import NoteCreateSchema, NoteUpdateSchema
from src.models import Note


# Reads all notes in DB
async def read_notes(session: AsyncSession) -> Sequence[Note]:
    stmt = select(Note)
    res = await session.execute(stmt)
    notes = res.scalars().all()
    return notes


# Reads note by id
async def read_note_by_id(session: AsyncSession, note_id: int) -> Note | None:
    return await session.get(Note, note_id)


async def read_note_by_title(session: AsyncSession, title: str) -> Note | None:
    stmt = select(Note).where(Note.title == title)
    res = await session.execute(stmt)
    note = res.scalars().first()
    return note


async def create_note(session: AsyncSession, note_in: NoteCreateSchema) -> Note:
    new_note = Note(**note_in.model_dump())
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)
    return new_note


async def update_note(session: AsyncSession, note: Note, note_in: NoteUpdateSchema):
    for name, value in note_in.model_dump(exclude_unset=True).items():
        setattr(note, name, value)
    await session.commit()
    await session.refresh(note)
    return note


async def delete_note(session: AsyncSession, note: Note):
    await session.delete(note)
    await session.commit()
    return {"msg": f"Note {note.id} deleted"}
