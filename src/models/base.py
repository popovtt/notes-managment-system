from datetime import datetime
from typing import Annotated
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


created_at = Annotated[datetime, mapped_column(default=datetime.now, server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(
    default=datetime.now,
    server_default=func.now(),
    onupdate=datetime.now,
)]


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now,server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
        onupdate=datetime.now,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
