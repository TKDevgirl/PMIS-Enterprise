from typing import Optional
from pydantic import BaseModel


class RackPositionUpdate(BaseModel):
    rack_id: str
    drawing_id: Optional[str] = None
    x: float
    y: float
