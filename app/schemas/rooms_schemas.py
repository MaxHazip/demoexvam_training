from pydantic import BaseModel, Field, ConfigDict
    
class RoomCreateRequest(BaseModel):

    name: str = Field(..., min_length=3, pattern=r"^[А-Яа-яЁёA-Za-z0-9№]+([ -][А-Яа-яЁёA-Za-z0-9№]+)*$")
    room_type: str = Field(..., min_length=3)

    model_config = ConfigDict(str_strip_whitespace=True)