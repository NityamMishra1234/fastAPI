from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.command_service import handle_command

router = APIRouter()

class CommandRequest(BaseModel):
    text: str

@router.post("/process")
async def process_command(data: CommandRequest):
    try:
        response = handle_command(data.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
