from pydantic import BaseModel, Field

class RoomTypesCreateRequest(BaseModel):

    name: str = Field(...)