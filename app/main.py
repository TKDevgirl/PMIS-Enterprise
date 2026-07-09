from fastapi import FastAPI
from app.api import racks, rooms, equipment, dashboard, buildings, floors, layout, web
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="PMIS Enterprise API",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(racks.router)
app.include_router(rooms.router)
app.include_router(equipment.router)
app.include_router(dashboard.router)
app.include_router(buildings.router)
app.include_router(floors.router)
app.include_router(layout.router)
app.include_router(web.router)

@app.get("/")
def root():
    return {"message": "PMIS Enterprise Backend is running"}
