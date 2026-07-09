import pandas as pd
from app.repository.excel_repository import read_sheet, none_safe_records


def _optional_sheet(sheet_name: str) -> pd.DataFrame:
    try:
        return read_sheet(sheet_name)
    except Exception:
        return pd.DataFrame()


def get_layout(building_id=None, floor_id=None, drawing_id=None):
    rack_master = _optional_sheet("Rack_Master")
    rack_position = _optional_sheet("Rack_Position")
    room_master = _optional_sheet("Room_Master")
    drawing_master = _optional_sheet("Drawing_Master")

    if not rack_master.empty and not rack_position.empty and "Rack_ID" in rack_master.columns and "Rack_ID" in rack_position.columns:
        racks = rack_position.merge(rack_master, on="Rack_ID", how="left", suffixes=("", "_master"))
    else:
        racks = rack_position

    if drawing_id and not racks.empty and "Drawing_ID" in racks.columns:
        racks = racks[racks["Drawing_ID"].astype(str) == str(drawing_id)]

    if floor_id and not racks.empty:
        floor_cols = [c for c in ["Floor_ID", "Floor_ID_master"] if c in racks.columns]
        if floor_cols:
            racks = racks[racks[floor_cols[0]].astype(str) == str(floor_id)]

    if building_id and not drawing_master.empty and "Building_ID" in drawing_master.columns:
        drawing_master = drawing_master[drawing_master["Building_ID"].astype(str) == str(building_id)]

    if floor_id and not room_master.empty and "Floor_ID" in room_master.columns:
        room_master = room_master[room_master["Floor_ID"].astype(str) == str(floor_id)]

    if drawing_id and not room_master.empty and "Drawing_ID" in room_master.columns:
        room_master = room_master[room_master["Drawing_ID"].astype(str) == str(drawing_id)]

    return {
        "rooms": none_safe_records(room_master) if not room_master.empty else [],
        "racks": none_safe_records(racks) if not racks.empty else [],
    }
