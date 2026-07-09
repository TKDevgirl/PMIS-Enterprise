from fastapi import APIRouter
from app.services.excel_service import read_sheet

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


def count_by_field(data, field_name):
    result = {}

    for item in data:
        value = str(item.get(field_name, "")).strip() or "Unknown"
        result[value] = result.get(value, 0) + 1

    return result


@router.get("/")
def get_dashboard_summary():
    building = read_sheet("Building_Master")
    floor = read_sheet("Floor_Master")
    room = read_sheet("Room_Master")
    rack = read_sheet("Rack_Master")
    equipment = read_sheet("Equipment_Master")

    valid_racks = [
        r for r in rack
        if str(r.get("Rack_No", "")).strip() != ""
    ]

    return {
        "buildings": len(building),
        "floors": len(floor),
        "rooms": len(room),
        "racks": len(valid_racks),
        "equipment": len(equipment),
        "rack_by_type": count_by_field(valid_racks, "Rack_Type"),
        "rack_by_floor": count_by_field(valid_racks, "Floor_ID"),
        "rack_by_zone": count_by_field(valid_racks, "Zone_ID"),
    }