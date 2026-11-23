from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, TIMESTAMP, func, ForeignKey, CheckConstraint
from datetime import datetime

class Review(Base):

    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    request_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("requests.id"),
        nullable=False
    )
    request: Mapped["Request"] = relationship(back_populates="reviews")

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    user: Mapped["User"] = relationship(back_populates="reviews")

    __table_args__ = (
        CheckConstraint(
            r"content !~ '^\s*$'",
            name="chk_content_is_not_empty"
        ),
    )