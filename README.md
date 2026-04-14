# Notes API

A lightweight RESTful API for managing notes, built with **FastAPI** and **Python**.

## Features

- **Create** notes with a title and content
- **Retrieve** a single note by ID or list all notes
- **Update** notes partially (PATCH) — only changed fields need to be sent
- **Delete** notes by ID
- **Search** notes by title keyword
- **Pagination** support via `limit` and `skip` query parameters
- **Background tasks** — simulates an email notification on every new note creation
- **Input validation** via Pydantic schemas (title: 1–100 chars, content: non-empty)
- **Auto-generated interactive docs** at `/docs` (Swagger UI) and `/redoc` (ReDoc)

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| Validation | [Pydantic v2](https://docs.pydantic.dev/) |
| Server | [Uvicorn](https://www.uvicorn.org/) |
| Storage | In-memory (Python list) |

## Project Structure

```
Notes-API/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── schemas.py       # Pydantic request/response models
│   ├── routers/
│   │   └── notes.py     # Route handlers for /api/notes
│   └── service/
│       └── note_service.py  # Business logic & in-memory storage
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Div-30/Notes-API.git
   cd Notes-API
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux / macOS
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```


