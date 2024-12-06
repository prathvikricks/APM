Create and activate a virtual environment:


python -m venv .venv
source .venv/bin/activate  


Install dependencies for the backend:
pip install fastapi uvicorn celery redis pymongo bson pydantic


Install Redis locally (if needed):
brew install redis  # macOS


Install Angular CLI:
npm install -g @angular/cli



1. Start the Backend (FastAPI) Server
To start your FastAPI server (assuming it's running on localhost:8000):


uvicorn app:app --reload
2. Start Celery Worker (Background Task Processor)
To start the Celery worker using Redis as the message broker:
celery -A celery_app worker --loglevel=info



3. Start Redis
To start Redis server locally (ensure Redis is installed first):
redis-server

4. Start the Frontend (Angular)
To start your Angular frontend (assuming you're in the todo-app directory):
ng serve
This will start the Angular development server, typically on http://localhost:4200.



Recap:
Start FastAPI server:
uvicorn app:app --reload


Start Celery worker:
celery -A celery_app worker --loglevel=info


Start Redis:
redis-server


Start Angular frontend:
ng serve
These are the core commands you need to run your full-stack application with FastAPI as the backend, Celery for task processing, Redis as the message broker, and Angular as the frontend.


