# Notes API

A lightweight RESTful API for managing notes, built with **FastAPI** and **Python**. Notes are stored in-memory, making this ideal for development, prototyping, and learning purposes.

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

### Running the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Reference

All endpoints are prefixed with `/api/notes`.

### List Notes

```
GET /api/notes/
```

| Query Parameter | Type | Default | Description |
|---|---|---|---|
| `limit` | int | 5 | Maximum number of notes to return |
| `skip` | int | 0 | Number of notes to skip (offset) |
| `search` | string | `""` | Filter notes whose title contains this string |

**Example**

```
GET /api/notes/?limit=10&skip=0&search=meeting
```

---

### Get a Note

```
GET /api/notes/{id}
```

Returns the note with the given `id`. Responds with `404` if not found.

---

### Create a Note

```
POST /api/notes/
```

**Request Body**

```json
{
  "title": "My first note",
  "content": "This is the content of my note."
}
```

- `title`: required, 1–100 characters
- `content`: required, at least 1 character

**Response** `201 Created`

```json
{
  "id": 1,
  "title": "My first note",
  "content": "This is the content of my note.",
  "created_at": "2024-01-01T12:00:00"
}
```

A background task will log an email notification for the new note.

---

### Update a Note

```
PATCH /api/notes/{id}
```

Partially updates an existing note. Only include the fields you want to change.

**Request Body** (all fields optional)

```json
{
  "title": "Updated title",
  "content": "Updated content."
}
```

Responds with `404` if the note is not found.

---

### Delete a Note

```
DELETE /api/notes/{id}
```

Deletes the note with the given `id`. Returns `204 No Content` on success, or `404` if not found.

---

## Interactive Documentation

Once the server is running, visit:

- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Notes

> Data is stored in-memory and will be lost when the server restarts. For persistent storage, consider integrating a database such as PostgreSQL or SQLite with SQLAlchemy.
