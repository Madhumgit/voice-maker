from pydantic import BaseModel
from typing import Optional

class UserInteraction(BaseModel):
    user_input: str
    intent: str
    response: Optional[str] = None
    media_url: Optional[str] = None
    timestamp: Optional[str] = None  # ISO format string for timestamp