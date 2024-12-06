from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# FastAPI instance
app = FastAPI()

# Add CORS middleware to handle requests from Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Allow requests from Angular app on localhost:4200
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, DELETE)
    allow_headers=["*"],  # Allow all headers
)

# MongoDB setup
CONNECTION_STRING = "mongodb+srv://prathvinaik100:euQVQDAkI7nzbNAd@cluster0.hbfzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "todoappdb2"
COLLECTION_NAME = "todoappcollection2"

client = MongoClient(CONNECTION_STRING)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Model for validation
class Todo(BaseModel):
    description: str

# API Endpoints
@app.get("/api/todoapp/getNotes")
async def get_notes():
    notes = []
    for note in collection.find():
        note["_id"] = str(note["_id"])  # Convert ObjectId to string
        notes.append(note)
    return notes

@app.post("/api/todoapp/AddNotes")
async def add_note(note: Todo):
    result = collection.insert_one(note.dict())
    return {"message": "Note added successfully", "insertedId": str(result.inserted_id)}

@app.delete("/api/todoapp/DeleteNotes/{id}")
async def delete_note(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}
