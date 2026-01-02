# Interaction Contracts: Todo Console Application

## User Interface Contracts

### Main Menu Interface
**Input**: User selects option (1-6) from main menu
**Output**: Appropriate submenu or action result
**Error Handling**: On invalid input, display error message and re-prompt

### Add Task Interface
**Input**:
- Title (string, 1-200 characters)
- Description (optional string, 0-1000 characters)
**Output**: Success message with new task ID
**Error Handling**: Validate inputs, show appropriate error messages

### View Tasks Interface
**Input**: None required
**Output**: Formatted list of all tasks with ID, title, description, and status indicator
**Error Handling**: If no tasks exist, display "No tasks available" message

### Update Task Interface
**Input**:
- Task ID (integer)
- New title (optional string)
- New description (optional string)
**Output**: Success confirmation
**Error Handling**: If ID not found, show "Task not found" error

### Delete Task Interface
**Input**: Task ID (integer)
**Output**: Confirmation message
**Error Handling**: If ID not found, show "Task not found" error

### Mark Complete/Incomplete Interface
**Input**: Task ID (integer)
**Output**: Success confirmation
**Error Handling**: If ID not found, show "Task not found" error

## Internal Module Contracts

### Task Class Interface
- Constructor accepts: id, title, description, completed
- Properties: id, title, description, completed
- Methods: to_dict() for serialization

### TodoManager Class Interface
- Methods:
  - add_task(title, description) → Task
  - get_all_tasks() → List[Task]
  - get_task_by_id(task_id) → Task or None
  - update_task(task_id, title, description) → bool
  - delete_task(task_id) → bool
  - mark_complete(task_id) → bool
  - mark_incomplete(task_id) → bool