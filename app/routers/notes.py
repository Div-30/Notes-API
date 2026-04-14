from typing import Optional
from fastapi import APIRouter, HTTPException, Response, status, BackgroundTasks
from app.service import note_service
from app import schemas

router = APIRouter(
    prefix="/api/notes",
    tags=["Notes"]
)

@router.get("/", response_model=list[schemas.NoteResponse])
def get_note(limit: int = 5, skip: int = 0, search: Optional[str] = ""):
    return note_service.filter_and_paginated_notes(search, skip, limit)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, background_tasks: BackgroundTasks):
    note_dict = note.model_dump()
    note_dict["id"] = len(note_service.notes_db) + 1
    note_service.notes_db.append(note_dict)
    background_tasks.add_task(
        note_service.send_email_notification,
        note_title=note.title,
        author=note.author
    )
    return note_dict

@router.get("/{id}", response_model=schemas.NoteResponse)
def get_note(id: int):
    note = note_service.get_note_by_id(id)
    if not note:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note of the id {id} is not found")
    return note


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
    

