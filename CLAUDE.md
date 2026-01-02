# Claude Code Rules

This file is generated during init for the selected agent.

You are an expert AI assistant specializing in Spec-Driven Development (SDD). Your primary goal is to work with the architecture to build products.

## Implementation Notes

This project implements a Todo In-Memory Console Application with the following characteristics:

- **Language**: Python 3.8+
- **Architecture**: Modular design with separation of concerns
- **Storage**: In-memory only (no persistence)
- **Interface**: Menu-driven console application
- **Dependencies**: Built-in Python libraries only (no external dependencies)

## Project Structure

- `src/task.py`: Task data model with validation
- `src/todo_manager.py`: Business logic for task operations
- `src/main.py`: Console interface and menu system
- `README.md`: User documentation
- `CLAUDE.md`: Implementation notes

## Key Features Implemented

1. **Add Task**: Create new tasks with title and description
2. **View Tasks**: Display all tasks with proper formatting
3. **Update Task**: Modify existing task details
4. **Delete Task**: Remove tasks by ID with confirmation
5. **Mark Complete/Incomplete**: Toggle task completion status

## Validation & Error Handling

- Input validation for all user inputs
- Graceful error handling for invalid task IDs
- Prevention of application crashes on invalid input
- Clear error messages for all error scenarios

## Design Decisions

- Used a class-based approach for clear separation of concerns
- Implemented proper validation in the Task class
- Created a TodoManager class to handle all business logic
- Designed a user-friendly menu system with clear prompts
- Followed Python best practices and conventions