
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import charlogic

app = FastAPI()

class CharRequest(BaseModel):
    charname: str

class CharUpdateRequest(BaseModel):
    charname: str
    new_data: dict

@app.post("/character/get")
async def get_character(data: CharRequest):
    char_data = charlogic.get_character(data.charname)
    if char_data:
        return {"data": char_data}
    raise HTTPException(status_code=404, detail="Character not found")

@app.post("/character/update")
async def update_character(data: CharUpdateRequest):
    result = charlogic.update_character(data.charname, data.new_data)
    if result:
        return {"status": "success", "message": "Character updated"}
    raise HTTPException(status_code=404, detail="Character not found or update failed")
