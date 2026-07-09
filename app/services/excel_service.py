from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
EXCEL_FILE = BASE_DIR / "data" / "PMIS.xlsx"


def read_sheet(sheet_name: str):
    if not EXCEL_FILE.exists():
        return {
            "error": True,
            "message": f"Excel file not found: {EXCEL_FILE}"
        }

    df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)
    df = df.fillna("")
    return df.to_dict(orient="records")