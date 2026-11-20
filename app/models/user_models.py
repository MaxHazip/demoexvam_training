from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, CheckConstraint, Enum, Index, func
import enum

class UserRoles(enum.Enum):

    ADMIN = "admin"
    USER = "user"

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    login: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(70), nullable=False, unique=True)
    role: Mapped[UserRoles] = mapped_column(
        Enum(UserRoles, name="user_roles_enum", values_callable=lambda x: [e.value for e in x]),
        default=UserRoles.USER,
        server_default="user",
        nullable=False
    )

    __table_args__ = (
        CheckConstraint(
            r"full_name ~ '^[А-Яа-яЁё]+([ -][А-Яа-яЁё]+)*$'",
            name="chk_full_name_cyrillic"
        ),
        CheckConstraint(
            r"login ~ '^[A-Za-z0-9]{6,50}$'",
            name="chk_login_latin_and_nums"
        ),
        CheckConstraint(
            r"phone ~ '^8\([0-9]{3}\)[0-9]{3}-[0-9]{2}-[0-9]{2}$'",
            name="chk_phone_correct_format"
        ),
        CheckConstraint(
            r"email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'",
            name="chk_email_correct_format"
        ),
        Index(
            "idx_users_lower_email",
            func.lower(email),
            unique=True
        )
    )