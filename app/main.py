import uuid
import shutil

import uvicorn
from pathlib import Path
from fastapi import FastAPI, UploadFile, File

from services import MultiSystem, DeleteAllCache

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI()

@app.post("/image_information")
def get_information(img_file: UploadFile = File(...)):
    yandex_studio_ai_oil_service = MultiSystem(img_file)
    result = yandex_studio_ai_oil_service()
    return result

@app.delete("/delete_all_cache")
async def delete_all_cache():
    delete_cache = DeleteAllCache()
    return delete_cache()

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    