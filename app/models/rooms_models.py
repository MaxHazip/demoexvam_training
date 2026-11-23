from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Index, func, CheckConstraint, ForeignKey

class RoomType(Base):

    __tablename__ = "room_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, unique=True)

    rooms: Mapped[list["Room"]] = relationship(back_populates="room_type")

    __table_args__ = (
        Index(
            "idx_lower_name_unique",
            func.lower(name),
            unique=True
        ),
        CheckConstraint(
            "length(name) >= 3",
            name="chk_room_type_name_3_or_more"
        ),
        CheckConstraint(
            r"name !~ '^\s*$'",
            "check_room_type_name_is_not_empty"
        )
    )

class Room(Base):

    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), index=True, unique=True, nullable=False)

    room_type_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("room_types.id", ondelete="CASCADE"),
        nullable=False
    )
    room_type: Mapped["RoomType"] = relationship(back_populates="rooms")

    requests: Mapped[list["Request"]] = relationship(back_populates="room")

    __table_args__ = (
        CheckConstraint(
            "length(name) >= 3",
            name="chk_name_length_3_or_more"
        ),
        CheckConstraint(
            r"name ~ '^[А-Яа-яЁёA-Za-z0-9№]{3,}([ -][№А-Яа-яЁёA-Za-z0-9]+)*$'",
            name="chk_name_format"
        ),
    )

