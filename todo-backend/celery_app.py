from celery import Celery
from pymongo import MongoClient

# Celery Configuration to use Redis as Broker
app = Celery('tasks', broker='redis://localhost:6379/0')

# MongoDB setup
CONNECTION_STRING = "mongodb+srv://prathvinaik100:euQVQDAkI7nzbNAd@cluster0.hbfzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "todoappdb2"
COLLECTION_NAME = "todoappcollection2"

client = MongoClient(CONNECTION_STRING)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Define a background task (e.g., adding a note)
@app.task
def add_note_task(note_content):
    # Simulate processing the note (e.g., saving to DB or additional processing)
    print(f'Processing note: {note_content}')
    collection.insert_one({"description": note_content})
    return f'Note "{note_content}" processed successfully'
