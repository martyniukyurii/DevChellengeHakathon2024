# api/routes/call.py
import json

from fastapi import APIRouter, HTTPException
from models.call import Call
from services.call_service import process_audio_call

router = APIRouter()


@router.post("/", response_model=Call)
async def create_call(audio_url: str):
    try:
        call = process_audio_call(audio_url)
        return call
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.get("/{id}", response_model=Call)
async def get_call(call_id: str):
    try:
        with open(f"./calls/{call_id}.json", "r") as f:
            call_data = json.load(f)
            return Call(**call_data)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Call not found")
