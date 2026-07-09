from fastapi import APIRouter
from app.services.excel_service import read_sheet

router = APIRouter(prefix="/api/racks", tags=["Racks"])


@router.get("/")
def get_racks():
    return read_sheet("Rack_Master")

@router.get("/{rack_id}")
def get_rack_by_id(rack_id: str):
    racks = read_sheet("Rack_Master")

    for rack in racks:
        if str(rack.get("Rack_ID", "")).strip() == rack_id:
            return rack

    return {"error": "Rack not found"}
