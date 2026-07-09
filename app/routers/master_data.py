from fastapi import APIRouter
from app.repository.excel_repository import sheet_records

router = APIRouter(prefix="/api", tags=["master-data"])


@router.get("/buildings")
def get_buildings():
    return sheet_records("Building_Master")


@router.get("/floors")
def get_floors():
    return sheet_records("Floor_Master")


@router.get("/drawings")
def get_drawings():
    return sheet_records("Drawing_Master")


@router.get("/rooms")
def get_rooms():
    return sheet_records("Room_Master")


@router.get("/racks")
def get_racks():
    return sheet_records("Rack_Master")


@router.get("/rack-positions")
def get_rack_positions():
    return sheet_records("Rack_Position")


@router.get("/equipment")
def get_equipment():
    return sheet_records("Equipment_Master")
