from typing import Optional
from fastapi import APIRouter, Depends
from app.dependencies import require_admin
from app.models import RackPositionUpdate
from app.services.layout_service import get_layout
from app.repository.excel_repository import update_rack_position

router = APIRouter(prefix="/api/layout", tags=["layout"])


@router.get("")
def layout(building_id: Optional[str] = None, floor_id: Optional[str] = None, drawing_id: Optional[str] = None):
    return get_layout(building_id=building_id, floor_id=floor_id, drawing_id=drawing_id)


@router.post("/rack-position/update")
def update_position(payload: RackPositionUpdate, role: str = Depends(require_admin)):
    return {"status": "saved", "updated": update_rack_position(payload.rack_id, payload.drawing_id, payload.x, payload.y)}
