from fastapi import APIRouter
from app.services.excel_service import read_sheet

router = APIRouter(prefix="/api/layout", tags=["Layout"])


@router.get("/floor/{floor_id}/room/{room_id}")
def get_layout_by_floor_room(floor_id: str, room_id: str):
    racks = read_sheet("Rack_Master")

    filtered = [
        r for r in racks
        if str(r.get("Room_ID", "")).strip() == room_id
        and str(r.get("Floor_ID", "")).strip() == floor_id
        and str(r.get("Rack_No", "")).strip() != ""
    ]

    result = []

    for r in filtered:
        result.append({
            "Rack_ID": r.get("Rack_ID", ""),
            "Rack_Label": r.get("Rack_Label", ""),
            "Room_ID": r.get("Room_ID", ""),
            "Floor_ID": r.get("Floor_ID", ""),
            "Rack_Type": r.get("Rack_Type", ""),
            "Rack_Size": r.get("Rack_Size", "")
        })

    return result
@router.get("/floor/{floor_id}")
def get_layout_by_floor(floor_id: str):
    racks = read_sheet("Rack_Master")

    filtered = [
        r for r in racks
        if str(r.get("Floor_ID", "")).strip() == floor_id
        and str(r.get("Rack_No", "")).strip() != ""
    ]

    rooms = {}

    for r in filtered:
        room_id = str(r.get("Room_ID", "")).strip()

        if room_id not in rooms:
            rooms[room_id] = []

        rooms[room_id].append({
            "Rack_ID": r.get("Rack_ID", ""),
            "Rack_Label": r.get("Rack_Label", ""),
            "Room_ID": room_id,
            "Floor_ID": r.get("Floor_ID", ""),
            "Rack_Type": r.get("Rack_Type", ""),
            "Rack_Size": r.get("Rack_Size", "")
        })

    return rooms