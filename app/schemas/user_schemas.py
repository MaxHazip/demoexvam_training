from pydantic import BaseModel, Field, EmailStr, field_validator

class UserRegisterRequest(BaseModel):

    login: str = Field(..., min_length=6, pattern=r"^[A-Za-z0-9]{6,50}$")
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=3, pattern=r"^[А-Яа-яЁё]+([ ][А-Яа-яЁё]+)*$")
    email: EmailStr = Field(...)
    phone: str = Field(..., pattern=r"^8\(\d{3}\)\d{3}-\d{2}-\d{2}$")
    role: str