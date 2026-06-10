from fastapi import FastAPI, UploadFile, File
import shutil

from services.ocr_service import extract_text
from services.summarizer import summarize_document

app = FastAPI(
    title="Multimodal Document Intelligence System"
)

@app.get("/")
def home():
    return {
        "message": "System Running Successfully"
    }

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    summary = summarize_document(text)

    return {
        "filename": file.filename,
        "extracted_text": text,
        "summary": summary
    }
