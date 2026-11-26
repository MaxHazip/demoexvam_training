from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.rooms_repo import RoomRepo
from app.schemas.rooms_schemas import RoomCreateRequest
from app.exceptions import RoomAlreayExistsException, NoSuchRoomTypeException
from fastapi import status
from app.models.rooms_models import Room
from app.services.room_types_service import RoomTypesService


class RoomService():

    def __init__(self, session: AsyncSession):
        self.repo = RoomRepo(session=session)
        self.room_types_service = RoomTypesService(session=session)

    async def get_room_by_name(
        self,
        name: str    
    ):

        return await self.repo.get_room_by_name(name=name)

        

    async def create_new_room(
        self,                
        new_room: RoomCreateRequest
    ):

        room = await self.repo.get_room_by_name(name=new_room.name)

        if room:
            raise RoomAlreayExistsException(
                status_code=status.HTTP_409_CONFLICT
            )

        is_room_type_correct = await self.room_types_service.get_room_type_by_name(room_type=new_room.room_type)

        if is_room_type_correct is None:
            raise NoSuchRoomTypeException(
                status_code=status.HTTP_404_NOT_FOUND
            )


        room_obj = Room(
            name=new_room.name,
            room_type_id=is_room_type_correct.id
        )

        await self.repo.create_new_room(room_obj)