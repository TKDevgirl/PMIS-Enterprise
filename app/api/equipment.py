from fastapi import APIRouter, HTTPException
from app.services.excel_service import read_sheet

router = APIRouter(prefix="/api/equipment", tags=["Equipment"])


@router.get("/")
def get_equipment():
    return read_sheet("Equipment_Master")


@router.get("/rack/{rack_id}")
def get_equipment_by_rack(rack_id: str):
    equipment_list = read_sheet("Equipment_Master")

    result = [
        item for item in equipment_list
        if str(item.get("Rack_ID", "")).strip() == rack_id
    ]

    if not result:
        raise HTTPException(status_code=404, detail="No equipment found for this rack")

    return result


