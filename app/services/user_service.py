from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schemas import UserRegisterRequest
from app.repositories.user_repo import UserRepo
from app.exceptions import (
    UserAlreadyExistsException
)
from fastapi import status
from app.core.security import get_password_hash
from app.models.user_models import User

class UserService:

    def __init__(self, session: AsyncSession):
        self.repo = UserRepo(session=session)

    async def create_new_user(
        self,
        user: UserRegisterRequest
    ):
        if await self.repo.get_user_by_email(user_email=user.email.lower()):
            raise UserAlreadyExistsException(status_code=status.HTTP_403_FORBIDDEN)

        if await self.repo.get_user_by_phone(user_phone=user.phone):
            raise UserAlreadyExistsException(status_code=status.HTTP_403_FORBIDDEN)
        
        if await self.repo.get_user_by_login(user_login=user.login):
            raise UserAlreadyExistsException(status_code=status.HTTP_403_FORBIDDEN)

        password_hash = get_password_hash(user.password)

        if user.role is None:
            user.role = "user"

        new_user = User(
            login=user.login,
            hashed_password=password_hash,
            full_name=user.full_name,
            phone=user.phone,
            email=user.email,
            role=user.role
        )

        await self.repo.add_new_user(user=new_user)

    async def get_user_by_login(
        self,
        login: str
    ):

        return await self.repo.get_user_by_login(user_login=login)