from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import charlogic  # Assuming charlogic contains the logic for getting and updating character data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow your frontend app to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, change this to specific domains for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define request models
class CharRequest(BaseModel):
    charname: str

class CharUpdateRequest(BaseModel):
    charname: str
    new_data: dict

# Endpoint to get character data
@app.post("/character/get")
async def get_character(data: CharRequest):
    char_data = charlogic.get_character(data.charname)
    if char_data:
        return {"data": char_data}
    raise HTTPException(status_code=404, detail="Character not found")

# Endpoint to update character data
@app.post("/character/update")
async def update_character(data: CharUpdateRequest):
    result = charlogic.update_character(data.charname, data.new_data)
    if result:
        return {"status": "success", "message": "Character updated"}
    raise HTTPException(status_code=404, detail="Character not found or update failed")
