from sqlalchemy.orm import Mapped

from src.models import Base, created_at, updated_at


class Note(Base):
    title: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
