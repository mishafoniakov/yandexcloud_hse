import uuid
import shutil

import uvicorn
from pathlib import Path
from fastapi import FastAPI, UploadFile, File

#from models import User, Contact, FeedBack, SimpleResponse

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI()

@app.get("/image")
def image():
    pass

@app.get("/image_information")
def read_users():
    pass

@app.get("/uuid")
def read_feedback():
    pass

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
    