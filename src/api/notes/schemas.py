from pydantic import BaseModel

from src.models import created_at, updated_at


class NoteSchema(BaseModel):
    title: str
    summary: str
    created_at: created_at
    updated_at: updated_at


class NoteCreateSchema(BaseModel):
    title: str


class NoteUpdateSchema(BaseModel):
    title: str | None = None
