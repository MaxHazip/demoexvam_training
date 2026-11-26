from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repo import UserRepo
from app.services.room_types_service import RoomTypesService
from app.models.user_models import User
from app.schemas.room_types_schemas import RoomTypesCreateRequest
from app.services.rooms_service import RoomService
from app.schemas.rooms_schemas import RoomCreateRequest
from app.core.security import get_password_hash
 

async def create_admin(session: AsyncSession):

    user_repo = UserRepo(session=session)

    amdin = await user_repo.get_user_by_login(user_login="Conf2027") 

    if not amdin :

        new_admin = User(
            login="Conf2027",
            hashed_password=get_password_hash("Demo77"),
            full_name="Админ",
            email="admin@example.com",
            phone="8(211)321-12-32",
            role="admin"
        )

        await user_repo.add_new_user(user=new_admin)

async def create_initial_room_types(session: AsyncSession):

    room_types_service = RoomTypesService(session=session)

    init_types = [
        "аудитория",
        "коворкинг",
        "кинозал"
    ]


    async with session.begin():
        for type in init_types:

            room_type = await room_types_service.get_room_type_by_name(room_type=type)

            if not room_type:

                new_type = RoomTypesCreateRequest(
                    name=type
                )

                await room_types_service.create_new_room_type(new_type)

async def create_initial_rooms(session: AsyncSession):

    room_service = RoomService(session=session)

    init_rooms = [

        {
            "name": "Вега зал 1",
            "room_type": "кинозал"
        },
        {
            "name": "Workki",
            "room_type": "коворкинг"
        },
        {
            "name": "МФТИ аудитория 245",
            "room_type": "аудитория"
        }

    ]

    async with session.begin():

        for room in init_rooms:

            db_room = await room_service.get_room_by_name(name=room["name"])

            if not db_room:

                new_room = RoomCreateRequest(
                    name=room["name"],
                    room_type=room["room_type"]
                )

                await room_service.create_new_room(new_room=new_room)