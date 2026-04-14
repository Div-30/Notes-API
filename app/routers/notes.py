from typing import Optional
from fastapi import APIRouter, HTTPException, Response, status, BackgroundTasks
from app.service import note_service
from datetime import datetime
from app import schemas

router = APIRouter(
    prefix="/api/notes",
    tags=["Notes"]
)

@router.get("/", response_model=list[schemas.NoteResponse])
def get_note(limit: int = 5, skip: int = 0, search: Optional[str] = ""):
    return note_service.filter_and_paginated_notes(search, limit, skip)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, background_tasks: BackgroundTasks):
    new_note = note_service.create_note(note)
    background_tasks.add_task(
        note_service.send_email_notification,
        note_title = new_note["title"],
    )
    return new_note

@router.get("/{id}", response_model=schemas.NoteResponse)
def get_note(id: int):
    note = note_service.get_note_by_id(id)
    if not note:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note of the id {id} is not found")
    return note


@router.patch("/{id}", response_model=schemas.NoteResponse)
def update_note(id: int, updated_note: schemas.NoteUpdate):
    update_data = updated_note.model_dump(exclude_unset=True)
    note = note_service.update_note_by_id(id, update_data)
    if not note:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note of the id {id} is not found")
    return note

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id: int):
    note = note_service.delete_note_by_id(id)
    if not note:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note of the id {id} is not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

