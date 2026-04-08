from pydantic import BaseModel, Field
from datetime import datetime

class NoteBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None = Field(default=None, min_length=1)

class NoteResponse(NoteBase):
    id: int
    created_at: datetime
