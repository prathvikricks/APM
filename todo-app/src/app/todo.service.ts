import { Injectable } from '@angular/core';
import { Observable, from } from 'rxjs';  // Import 'from' to convert Promise to Observable
// Removed HttpClient import, as it's globally provided

@Injectable({
  providedIn: 'root', // No need for HttpClient here
})
export class TodoService {
  private apiUrl = 'http://localhost:8000/api/todoapp';

  // No HttpClient injected here anymore
  constructor() {}

  // Method to get the list of notes
  getNotes(): Observable<any[]> {
    return from(
      fetch(`${this.apiUrl}/getNotes`)
        .then(response => response.json())  // Convert the Response to JSON
        .catch(error => { throw error }) // Handle any errors in the Promise
    );
  }

  // Method to add a new note
  addNote(note: string): Observable<any> {
    return from(
      fetch(`${this.apiUrl}/AddNotes`, {
        method: 'POST',
        body: JSON.stringify({ description: note }),
        headers: { 'Content-Type': 'application/json' },
      })
        .then(response => response.json())  // Convert the Response to JSON
    );
  }

  // Method to delete a note
  deleteNote(id: string): Observable<any> {
    return from(
      fetch(`${this.apiUrl}/DeleteNotes/${id}`, {
        method: 'DELETE',
      })
        .then(response => response.json())  // Convert the Response to JSON
    );
  }
}
