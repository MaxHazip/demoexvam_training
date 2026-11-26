from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_models import User
from sqlalchemy import select

class UserRepo:

    def __init__(self, session: AsyncSession):

        self.session = session

    async def add_new_user(
        self,
        user: User
    ):

        self.session.add(user)
        await self.session.commit()

    async def get_user_by_email(
        self,
        user_email: str
    ):

        stmt = select(User).where(User.email == user_email)

        return await self.session.scalar(stmt)

    async def get_user_by_login(
        self,
        user_login: str
    ):

        stmt = select(User).where(User.login == user_login)

        return await self.session.scalar(stmt)

    async def get_user_by_phone(
            self,
            user_phone: str
        ):
    
            stmt = select(User).where(User.phone == user_phone)
    
            return await self.session.scalar(stmt)