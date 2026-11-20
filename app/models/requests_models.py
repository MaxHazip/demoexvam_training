from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Enum, TIMESTAMP
import enum
from datetime import datetime

class PaymentType(enum.Enum):

    OFFLINE = "offline"
    SBP = "SBP"

class RequestStatus(enum.Enum):

    NEW = "Новая"
    ASSIGNED = "Мероприятие назначено"
    END = "Завершено"

class Request(Base):

    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)

    room_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("rooms.id", ondelete="SET NULL"),
        nullable=True
    )
    room: Mapped["Room"] = relationship(back_populates="requests")

    payment: Mapped[PaymentType] = mapped_column(
        Enum(PaymentType, name="payment_type_enum", values_callable=lambda x: [e.value for e in x]),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )
    user: Mapped["User"] = relationship(back_populates="requests")

    status: Mapped[RequestStatus] = mapped_column(
        Enum(RequestStatus, name="request_statuses_enum", values_callable=lambda x: [e.value for e in x]),
        default=RequestStatus.NEW,
        server_default="Новая",
        nullable=False
    )
    start_time: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=False),
        nullable=False
    )

    reviews: Mapped[list["Review"]] = relationship(back_populates="request")