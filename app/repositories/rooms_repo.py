from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.rooms_models import Room

class RoomRepo():

    def __init__(self, session: AsyncSession):

        self.session = session

    async def get_room_by_name(
        self,
        name: str
    ):

        smtm = select(Room).where(Room.name == name)
        return await self.session.scalar(smtm)

    async def create_new_room(
        self,
        room: Room
    ):

        self.session.add(room)
        await self.session.commit()