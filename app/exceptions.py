from fastapi.exceptions import HTTPException

class AppException(HTTPException):
    pass

class UserAlreadyExistsException(AppException):
    """Пользователь уже существует"""
    pass

class RoomTypeAlreayExistsException(AppException):
    """Тип комнаты уже существует"""
    pass

class RoomAlreayExistsException(AppException):
    """Помещение с таким названием уже существует"""
    pass

class NoSuchRoomTypeException(AppException):
    """Нет такого типа помещения"""
    pass