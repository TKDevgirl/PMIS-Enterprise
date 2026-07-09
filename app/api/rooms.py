from fastapi import APIRouter, HTTPException
from app.services.excel_service import read_sheet

router = APIRouter(prefix="/api/rooms", tags=["Rooms"])


@router.get("/")
def get_rooms():
    return read_sheet("Room_Master")


@router.get("/{room_id}/racks")
def get_racks_by_room(room_id: str):
    racks = read_sheet("Rack_Master")

    result = [
        rack for rack in racks
        if str(rack.get("Room_ID", "")).strip() == room_id
    ]

    if not result:
        raise HTTPException(status_code=404, detail="No racks found for this room")

    return result