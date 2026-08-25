# File endpoints
# ilya_bisec
# Date: 25/08/2026 15:09

from fastapi import APIRouter, UploadFile, File
from backend.app.services.storage_service import upload_file, generate_url
import uuid

router = APIRouter()

# Upload files
@router.post("/upload")
async def upload_endpoint(file: UploadFile = File(...)):
    key = f"{uuid.uuid4()}_{file.filename}"
    upload_file(file.file, key)
    return {
        "message": f"File {file.filename} uploaded",
        "key": key
    }

# Get download link
@router.get("/{key}")
def download_endpoint(key: str):
    url = generate_url(key)
    return {"url": url}