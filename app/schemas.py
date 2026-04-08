from pydantic import BaseModel, Field

class NoteBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(m)