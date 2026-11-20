from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Index, func, CheckConstraint, ForeignKey

class RoomType(Base):

    __tablename__ = "room_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, unique=True)

    rooms: Mapped["Room"] = relationship(back_populates="room_type")

    __table_args__ = (
        Index(
            "idx_lower_name_unique",
            func.lower(name),
            unique=True
        )
    )

class Room(Base):

    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), index=True, unique=True, nullable=False)

    room_type_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("room_types.id", ondelete="SET NULL"),
        nullable=True
    )
    room_type: Mapped["RoomType"] = relationship(back_populates="rooms")

    requests: Mapped["Request"] = relationship(back_populates="room")

    __table_args__ = (
        CheckConstraint(
            "length(name) >= 3",
            name="chk_name_length_3_or_more"
        ),
        CheckConstraint(
            r"name ~ '^[А-Яа-яЁёA-Za-z]+([ -][А-Яа-яЁёA-Za-z]+)*$'",
            name="chk_name_length_3_or_more"
        ),
    )

