from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.room_types_repo import RoomTypesRepo
from app.schemas.room_types_schemas import RoomTypesCreateRequest
from app.models.rooms_models import RoomType
from app.exceptions import RoomTypeAlreayExistsException
from fastapi import status

class RoomTypesService():

    def __init__(self, session: AsyncSession):

        self.repo = RoomTypesRepo(session=session)

    async def get_room_type_by_name(
        self,
        room_type:str
    ):

        return await self.repo.get_room_type(room_type=room_type)

    async def create_new_room_type(
        self,
        room_type: RoomTypesCreateRequest
    ):

        if await self.repo.get_room_type(room_type=room_type.name):
            raise RoomTypeAlreayExistsException(
                status_code=status.HTTP_409_CONFLICT
            )

        new_room_type = RoomType(
            name=room_type.name
        )

        await self.repo.create_new_room_type(room_type=new_room_type)