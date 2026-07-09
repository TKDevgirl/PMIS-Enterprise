from fastapi import APIRouter, Depends, UploadFile, File
from app.dependencies import require_admin
from app.repository.excel_repository import save_uploaded_workbook

router = APIRouter(prefix="/api/workbook", tags=["workbook"])


@router.post("/upload")
async def upload_workbook(file: UploadFile = File(...), role: str = Depends(require_admin)):
    content = await file.read()
    path = save_uploaded_workbook(content)
    return {"status": "uploaded", "filename": file.filename, "saved_to": path}
