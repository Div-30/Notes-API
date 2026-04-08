from fastapi import APIRouter, HTTPException, Response, status
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

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.NoteResponse)
def create_post(note: schemas.NoteCreate):
    note_dict = note.model_dump()
    new_id = 1 if not notes else max(n["id"] for n in notes) + 1

    note_dict["id"] = new_id
    note_dict["created_at"] = datetime.now()

    notes.append(note_dict)
    return note_dict

@router.get("/{id}", response_model=schemas.NoteResponse)
def get_note(id: int):
    for note in notes:
        if note["id"] == id:
            return note
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note of the id {id} is not found")

@router.patch("/{id}", response_model=schemas.NoteResponse)
def update_note(id: int, updated_note: schemas.NoteUpdate):
    for note in notes:
        if note["id"] == id:
            update_data = updated_note.model_dump(exclude_unset=True)
            note.update(update_data)
            return note
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note of the id {id} is not found")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id: int):
    for i, note in enumerate(notes):
        if note["id"] == id:
            notes.pop(i)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note of the id {id} is not found")
    

