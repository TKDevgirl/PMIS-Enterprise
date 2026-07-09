from fastapi import APIRouter
from app.services.excel_service import read_sheet

router = APIRouter(prefix="/api/floors", tags=["Floors"])


@router.get("/")
def get_floors():
    return read_sheet("Floor_Master")


@router.get("/{floor_id}/rooms")
def get_rooms_by_floor(floor_id: str):
    rooms = read_sheet("Room_Master")

    rack = read_sheet("Rack_Master")

    seen = set()
    result = []

    for r in rack:
        if str(r.get("Floor_ID", "")).strip() != floor_id:
            continue

        room_id = str(r.get("Room_ID", "")).strip()

        if room_id and room_id not in seen:
            seen.add(room_id)

            result.append({
                "Room_ID": room_id,
                "Floor_ID": floor_id
            })

    return result