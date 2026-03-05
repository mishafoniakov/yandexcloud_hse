import uuid
import shutil

import uvicorn
from pathlib import Path
from fastapi import FastAPI, UploadFile, File

from services import YandexStudioAIOilService

#from models import User, Contact, FeedBack, SimpleResponse

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI()

@app.get("/image_information")
def get_information(message: str):
    yandex_studio_ai_oil_service = YandexStudioAIOilService(message)
    result = yandex_studio_ai_oil_service()
    return result

@app.post('/upload') 
def upload_file(file: UploadFile = File(...)):
    file_extension = Path(file.filename).suffix
    safe_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = UPLOAD_DIR / safe_filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "path": str(file_path)}

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    