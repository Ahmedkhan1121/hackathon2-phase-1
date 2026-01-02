# Tasks: In-Memory Todo Python Console App

## Project Setup
1. Create src directory structure
2. Set up basic project files (README.md, CLAUDE.md)
3. Create specs/history directory
4. Initialize contracts directory structure

## Core Models
5. Create Task class with id, title, description, and completed attributes
6. Implement Task constructor with validation for title (non-empty)
7. Add Task string representation method for display purposes
8. Create method to convert Task to dictionary for serialization
9. Add validation to ensure title is 1-200 characters
10. Add validation to ensure description is max 1000 characters when provided

## Business Logic
11. Create TodoManager class with empty task list initialization
12. Implement auto-incrementing ID counter in TodoManager
13. Create add_task method that accepts title and description
14. Implement get_all_tasks method that returns all tasks
15. Create get_task_by_id method that returns specific task or None
16. Implement update_task method that modifies title and/or description
17. Create delete_task method that removes task by ID
18. Implement mark_complete method that sets completed status to True
19. Create mark_incomplete method that sets completed status to False
20. Add validation in all methods to handle invalid task IDs gracefully

## CLI Interface
21. Create main.py with basic program structure
22. Implement main menu display with all available options
23. Add input handling for menu selection
24. Create loop that continues until user selects exit option
25. Implement "Add Task" menu option with user input prompts
26. Create "View Tasks" functionality with formatted output
27. Implement "Update Task" menu option with ID and field prompts
28. Create "Delete Task" functionality with confirmation prompt
29. Implement "Mark Complete" option with ID input
30. Create "Mark Incomplete" option with ID input

## Validation & Error Handling
31. Add input validation for menu selection (numbers 1-6)
32. Implement validation for task title input (non-empty, proper length)
33. Add validation for task description input (proper length)
34. Create error handling for invalid task IDs in operations
35. Implement graceful error messages for non-existent tasks
36. Add input validation to prevent application crashes on invalid input
37. Create user-friendly error messages for all error scenarios
38. Implement validation to prevent duplicate operations on same input

## Final Testing
39. Test adding a new task with valid inputs
40. Verify auto-incremented ID assignment works correctly
41. Test viewing all tasks with proper formatting and status indicators
42. Verify updating task title and description works correctly
43. Test deleting tasks by ID with proper confirmation
44. Verify mark complete/incomplete functionality toggles status correctly
45. Test error handling with invalid task IDs
46. Verify application doesn't crash with invalid menu inputs
47. Test all menu options navigate correctly
48. Validate all user inputs are properly sanitized and validated