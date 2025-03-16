from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import db_helper, Note
from . import crud
from .deps import note_by_id
from .schemas import NoteCreateSchema,NoteUpdateSchema


router = APIRouter(tags=["Notes"])


@router.get("/")
async def get_notes(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.read_notes(session=session)


@router.get("/{note_id}", summary="Get Note by ID")
async def get_note_by_id(
        note_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.read_note_by_id(note_id=note_id, session=session)


@router.get("/title/")
async def get_note_by_title(
        note_title: str,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.read_note_by_title(session=session, title=note_title)


@router.post("/", status_code=201)
async def post_note(
        note_in: NoteCreateSchema,
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_note(note_in=note_in, session=session)


@router.patch("/")
async def patch_note(
        note_in: NoteUpdateSchema,
        note: Note = Depends(note_by_id),
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_note(session=session, note=note, note_in=note_in)


@router.delete("/", status_code=204)
async def delete_note(
        note: Note = Depends(note_by_id),
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.delete_note(note=note, session=session)
