from datetime import datetime


notes_db = []

def create_note(note) -> dict:
    note_dict = note.model_dump()
    note_dict["id"] = len(notes_db) + 1
    note_dict["created_at"] = datetime.now()
    notes_db.append(note_dict)
    return note_dict

def filter_and_paginated_notes(search: str, limit: int, skip: int):
    filtered = [note for note in notes_db if search.lower() in note['title'].lower()]
    return filtered[skip: skip + limit]

# This is a simulated background task
def send_email_notification(note_title: str):
    print(f"New note created titled: '{note_title}'")

def get_note_by_id(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    return None
def update_note_by_id(note_id: int, update_data: dict):
    for note in notes_db:
        if note["id"] == note_id:
            note.update(update_data)
            return note
    return None

def delete_note_by_id(note_id: int):
    for i, note in enumerate(notes_db):
        if note["id"] == note_id:
            notes_db.pop(i)
            return True
    return False