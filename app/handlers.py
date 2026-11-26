from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import (
    UserAlreadyExistsException,
    RoomTypeAlreayExistsException,
    RoomAlreayExistsException,
    NoSuchRoomTypeException
)

async def user_already_exists_handler(requset: Request, exc: UserAlreadyExistsException):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Пользователь с таким email или телефоном уже существует"
        }
    )

async def room_type_alreay_exists_handler(request: Request, exc: RoomTypeAlreayExistsException):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Тип комнаты уже существует"
        }
    )

async def room_already_exists_hanler(request: Request, exc: RoomAlreayExistsException):

    JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Помещение с таким назанием уже существует"
        }
    )

async def no_such_room_type_handler(request: Request, exc: NoSuchRoomTypeException):

    JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Такого типа комнаты несуществует"
        }
    )