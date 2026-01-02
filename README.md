# Todo In-Memory Console Application

A simple, menu-driven console application for managing tasks in memory. This application provides basic todo functionality without any persistence - all data is stored in memory during the application session.

## Features

- **Add Task**: Create new tasks with a title and description
- **View Tasks**: Display all tasks with their ID, title, description, and completion status
- **Update Task**: Modify existing task title and/or description
- **Delete Task**: Remove tasks by ID with confirmation
- **Mark Complete/Incomplete**: Toggle task completion status

## Requirements

- Python 3.8 or higher

## How to Run

1. Clone or download the repository
2. Navigate to the project directory
3. Run the application:
   ```bash
   python src/main.py
   ```

## Usage

The application provides a menu-driven interface:

```
==================================================
TODO APPLICATION - MAIN MENU
==================================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit
==================================================
```

Simply select an option by entering the corresponding number and follow the prompts.

## Project Structure

```
src/
├── main.py              # Entry point and menu interface
├── todo_manager.py      # Business logic for task operations
└── task.py              # Task data model
```

## Design Notes

- All data is stored in memory only (no persistence)
- Tasks are assigned auto-incremented IDs
- New tasks are marked as incomplete by default
- The application handles invalid inputs gracefully
- Status is displayed with [✓] for complete and [ ] for incomplete tasks