import { Component } from '@angular/core';
import { TodoComponent } from './todo/todo.component';  // Import TodoComponent

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,  // Marking this as standalone if used this way
  imports: [TodoComponent],  // Import TodoComponent
})
export class AppComponent {
  title = 'todo-app';
}
