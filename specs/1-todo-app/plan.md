# Implementation Plan: In-Memory Todo Python Console App

**Branch**: `1-todo-app` | **Date**: 2026-01-02 | **Spec**: [link](../spec.md)
**Input**: Feature specification from `/specs/1-todo-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a console-based todo application in Python that stores tasks in memory. The application provides core functionality for adding, viewing, updating, deleting, and marking tasks as complete/incomplete through a simple menu-driven interface. The design follows a modular architecture with clear separation of concerns between data models, business logic, and user interface.

## Technical Context

**Language/Version**: Python 3.8+
**Primary Dependencies**: Built-in Python libraries only (no external dependencies)
**Storage**: In-memory storage using Python data structures (list/dict)
**Testing**: Python unittest module for testing
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: Single console application
**Performance Goals**: Fast in-memory operations with sub-second response times
**Constraints**: <200ms response time for all operations, <50MB memory usage
**Scale/Scope**: Single user, up to 1000 tasks in memory

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The implementation plan adheres to the project constitution by:
- Using a simple, maintainable architecture
- Focusing on core functionality without over-engineering
- Implementing proper error handling to prevent crashes
- Providing clear user feedback through console messages
- Following Python best practices and conventions

## Project Structure

### Documentation (this feature)
```
specs/1-todo-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── main.py              # Entry point and menu loop
├── todo_manager.py      # Business logic for task operations
└── task.py              # Task data model
```

```text
specs/history/
```

```text
README.md
CLAUDE.md
```

**Structure Decision**: Single console application with three main modules following separation of concerns. The Task class handles data representation, TodoManager handles business logic, and main.py handles user interaction.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [None] | [No violations detected] | [N/A] |

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