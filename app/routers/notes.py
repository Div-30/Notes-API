from fastapi import APIRouter, HTTPException, Request, status
from datetime import datetime

from app.database import notes
from app import schemas

router = APIRouter(
    prefix="/api/notes",
    tags=["Notes"]
)

@router.get("/", response_model=list[schemas.NoteResponse])
def get_notes():
    return notes

@router.post("/", status_codes=status.HTTP_201_CREATED, response_model=schemas.NoteResponse)
def create_post(note: schemas.NoteCreate):
    note_dict = note.model_dump()
    new_id = 1 if not note else max(note["id"] for note in notes) + 1

    note_dict["id"] = new_id
    note_dict["created_at"] = datetime.now()

