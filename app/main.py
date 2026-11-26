from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import get_session
from contextlib import asynccontextmanager

from app.core.init_db import create_admin, create_initial_room_types, create_initial_rooms
from app.core.database import async_session_maker
from app.exceptions import (
    UserAlreadyExistsException,
    RoomTypeAlreayExistsException,
    RoomAlreayExistsException,
    NoSuchRoomTypeException
)
from app.handlers import (
    user_already_exists_handler,
    room_type_alreay_exists_handler,
    room_already_exists_hanler,
    no_such_room_type_handler
)

@asynccontextmanager
async def lifespan(
    app: FastAPI
):

    async with async_session_maker() as session:
        await create_admin(session)
        await create_initial_room_types(session)
        await create_initial_rooms(session)
        yield

app = FastAPI(title="Конференции.РФ", lifespan=lifespan)

app.add_exception_handler(UserAlreadyExistsException, user_already_exists_handler)
app.add_exception_handler(RoomTypeAlreayExistsException, room_type_alreay_exists_handler)
app.add_exception_handler(RoomAlreayExistsException, room_already_exists_hanler)
app.add_exception_handler(NoSuchRoomTypeException, no_such_room_type_handler)