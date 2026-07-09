from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.api.layout import get_layout_by_floor

router = APIRouter(tags=["Web"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/web/layout/{floor_id}")
def web_layout_floor(floor_id: str, request: Request):
    rooms = get_layout_by_floor(floor_id)

    return templates.TemplateResponse(
        "layout.html",
        {
            "request": request,
            "floor_id": floor_id,
            "rooms": rooms
        }
    )

@router.get("/dashboard")
def dashboard_page(request: Request):
    summary = {
        "total_rooms": 21,
        "total_racks": 72,
        "total_equipment": 128,
        "total_floors": 3
    }

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "summary": summary
        }
    )
