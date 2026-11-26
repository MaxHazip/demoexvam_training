from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.rooms_models import RoomType

class RoomTypesRepo():

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_room_type(
        self,
        room_type: str
    ):

        smtm = select(RoomType).where(RoomType.name == room_type)
        return await self.session.scalar(smtm)

    async def create_new_room_type(
        self,
        room_type: RoomType
    ):

        self.session.add(room_type)
        await self.session.commit()