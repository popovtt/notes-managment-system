from sqlalchemy.orm import Mapped

from src.models import Base


class Note(Base):
    title: Mapped[str]
