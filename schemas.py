
from pydantic import BaseModel

class CharRequest(BaseModel):
    charname: str

class CharUpdateRequest(BaseModel):
    charname: str
    new_data: dict
