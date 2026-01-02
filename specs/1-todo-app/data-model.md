# Data Model: In-Memory Todo Python Console App

## Task Entity

**Attributes**:
- `id` (int): Auto-incremented unique identifier for the task
- `title` (str): Title of the task (required, non-empty)
- `description` (str): Description of the task (optional, can be empty)
- `completed` (bool): Completion status of the task (default: False)

**Validation Rules**:
- ID must be a positive integer
- Title must be a non-empty string (1-200 characters)
- Description can be empty but must be a string if provided (max 1000 characters)
- Completed status must be a boolean value

**State Transitions**:
- Default state: `completed = False` when task is created
- State change: `completed = True` when task is marked complete
- State change: `completed = False` when task is marked incomplete

## Task List Collection

**Structure**: List of Task objects with methods for:
- Adding new tasks (with auto-incremented ID)
- Retrieving tasks by ID
- Updating task properties
- Deleting tasks by ID
- Listing all tasks
- Filtering tasks by completion status

**Behavior**:
- Maintains order of task creation
- Ensures unique IDs across all tasks
- Provides efficient lookup by ID (O(1) expected)
- Handles operations gracefully when tasks don't exist