# PMIS Backend V1 Clean

## How to run

1. Put your PMIS Excel file into `data/` and rename it to `PMIS.xlsx`.
2. Double-click `setup.bat` once.
3. Double-click `run.bat`.
4. Open: http://127.0.0.1:8000/docs

## Main APIs

- `GET /` health check
- `GET /api/racks` read Rack_Master
- `GET /api/rooms` read Room_Master
- `GET /api/equipment` read Equipment_Master
- `GET /api/layout` read Room + Rack layout data
- `POST /api/workbook/upload` upload Excel, admin only via header `X-Role: admin`
- `POST /api/rack-position/update` update X/Y in Rack_Position, admin only

## Role

Viewer can read only. Admin can upload/update.
Use header: `X-Role: admin`
