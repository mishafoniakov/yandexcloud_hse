import os
from pathlib import Path
import uuid
import shutil

def upload_file(img_file):
    UPLOAD_DIR = Path("uploads")
    UPLOAD_DIR.mkdir(exist_ok=True)
    file_extension = Path(img_file.filename).suffix
    safe_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, safe_filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(img_file.file, buffer)
    return file_path