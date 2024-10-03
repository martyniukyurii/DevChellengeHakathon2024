# models/call.py

from pydantic import BaseModel, Field
from typing import Optional, List
import uuid


class Call(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: Optional[str] = None
    location: Optional[str] = None
    emotional_tone: str
    text: str
    categories: List[str]
