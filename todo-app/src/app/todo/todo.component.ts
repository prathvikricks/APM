import { Component, OnInit } from '@angular/core';
import { TodoService } from '../todo.service';  // Import TodoService
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-todo',
  standalone: true,
  imports: [CommonModule, FormsModule],  // Ensure CommonModule and FormsModule are imported
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css']
})
export class TodoComponent implements OnInit {
  notes: any[] = [];
  newNote = '';

  constructor(private todoService: TodoService) {}

  async ngOnInit() {
    this.notes = (await this.todoService.getNotes().toPromise()) || [];
  }

  async addNote() {
    if (this.newNote.trim()) {
      await this.todoService.addNote(this.newNote);
      this.newNote = '';
      this.notes = (await this.todoService.getNotes().toPromise()) || [];
    }
  }

  async deleteNote(id: string) {
    await this.todoService.deleteNote(id);
    this.notes = (await this.todoService.getNotes().toPromise()) || [];
  }
}
