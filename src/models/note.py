from sqlalchemy import Integer
from sqlalchemy.orm import Mapped,mapped_column
from src.models import Base


class Note(Base):
    title: Mapped[str]
