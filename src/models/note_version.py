from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from src.models import Base


class NoteVersion(Base):
    __tablename__ = 'notes_versions'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    version_id: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    note_id: Mapped[int] = mapped_column(ForeignKey('notes.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    # __mapper_args__ = {"version_id_col": version_id}