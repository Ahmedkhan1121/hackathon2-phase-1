# Implementation Plan: In-Memory Todo Python Console App

## Project Structure
```
todo-app/
├── src/
│   ├── main.py              # Entry point and menu loop
│   ├── todo_manager.py      # Business logic for task operations
│   └── task.py              # Task data model
├── specs/history
├── README.md
├── CLAUDE.md
└── history/
    └── prompts/
        └── spec/
            └── 1-todo-app-spec.spec.prompt.md
```

## Main Modules and Responsibilities

### task.py
- Defines the `Task` class with attributes: id (auto-incremented), title, description, and completed status
- Implements data validation for task properties
- Provides methods for task representation and serialization

### todo_manager.py
- Manages the in-memory collection of tasks
- Implements all core business logic:
  - Add task with auto-incremented ID
  - View all tasks
  - Update task by ID
  - Delete task by ID
  - Mark task as complete/incomplete
- Handles error cases (invalid IDs, missing tasks)
- Ensures data integrity and validation

### main.py
- Implements the main application loop
- Provides the menu-driven CLI interface
- Handles user input and navigation
- Displays formatted output to console
- Processes user commands and calls appropriate manager methods

## Implementation Details

### 1. How tasks will be stored in memory
- Tasks will be stored in a Python list within the TodoManager class
- A separate counter variable will track the next available ID
- Each new task receives the current counter value as its ID, then the counter increments
- The in-memory storage persists only during the application session

### 2. How menu loop will work
- Main function runs an infinite loop that displays the menu options
- User input is captured and validated
- Based on user selection, appropriate functions in TodoManager are called
- After each operation, the menu is displayed again unless user chooses to exit
- Input validation prevents crashes from invalid entries

### 3. How each feature maps to a function
- **Add Task**: `TodoManager.add_task(title, description)` → creates new task with auto-incremented ID
- **View Tasks**: `TodoManager.get_all_tasks()` → returns all tasks for display
- **Update Task**: `TodoManager.update_task(task_id, title, description)` → updates specific task
- **Delete Task**: `TodoManager.delete_task(task_id)` → removes task by ID
- **Mark Complete/Incomplete**: `TodoManager.mark_complete(task_id)` and `TodoManager.mark_incomplete(task_id)` → toggles status

### 4. Order of implementation steps
1. **Create Task class** - Define the data model with validation
2. **Create TodoManager class** - Implement core business logic
3. **Implement basic menu structure** - Create the main loop and menu display
4. **Add Add Task functionality** - Connect user input to task creation
5. **Add View Tasks functionality** - Display tasks with proper formatting
6. **Add Update Task functionality** - Allow task modification
7. **Add Delete Task functionality** - Remove tasks by ID
8. **Add Mark Complete/Incomplete functionality** - Toggle task status
9. **Implement error handling** - Handle invalid IDs and inputs gracefully
10. **Add input validation** - Ensure clean, safe user input processing
11. **Refine UI/UX** - Improve console messages and formatting
12. **Testing** - Verify all functionality works as expected