from fastapi import APIRouter, HTTPException
from app.services.excel_service import read_sheet

router = APIRouter(prefix="/api/buildings", tags=["Buildings"])


@router.get("/")
def get_buildings():
    return read_sheet("Building_Master")


@router.get("/{building_id}/floors")
def get_floors_by_building(building_id: str):
    floors = read_sheet("Floor_Master")

    result = [
        f for f in floors
        if str(f.get("Building_ID", "")).strip() == building_id
    ]

    if not result:
        raise HTTPException(status_code=404, detail="No floors found for this building")

    return result