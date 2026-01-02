"""
Main entry point for the Todo In-Memory Console Application
Provides a menu-driven interface for all task operations
"""

import sys
import os
# Add the src directory to the path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__)))

from todo_manager import TodoManager


def display_menu():
    """Display the main menu options to the user"""
    print("\n" + "="*50)
    print("TODO APPLICATION - MAIN MENU")
    print("="*50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")
    print("="*50)


def get_menu_choice():
    """Get and validate user's menu choice"""
    while True:
        try:
            choice = input("Enter your choice (1-7): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                return int(choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except (ValueError, EOFError, KeyboardInterrupt):
            print("\nInvalid input. Please enter a number between 1 and 7.")
            continue


def get_task_input(prompt):
    """Get and validate task-related input from user"""
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            else:
                print("Input cannot be empty. Please try again.")
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return None


def get_task_id():
    """Get and validate task ID from user"""
    while True:
        try:
            task_id_input = input("Enter task ID: ").strip()
            task_id = int(task_id_input)
            if task_id > 0:
                return task_id
            else:
                print("Task ID must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for task ID.")
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
            return None


def add_task(todo_manager):
    """Handle adding a new task"""
    print("\n--- ADD NEW TASK ---")
    title = get_task_input("Enter task title: ")
    if title is None:
        return

    description = input("Enter task description (optional, press Enter to skip): ").strip()

    try:
        task = todo_manager.add_task(title, description)
        print(f"Task added successfully! ID: {task.id}")
    except ValueError as e:
        print(f"Error adding task: {e}")


def view_tasks(todo_manager):
    """Handle viewing all tasks"""
    print("\n--- ALL TASKS ---")
    tasks = todo_manager.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print(f"Total tasks: {len(tasks)}")
    print("-" * 80)
    for task in tasks:
        status = "[✓]" if task.completed else "[ ]"
        print(f"{status} ID: {task.id} | Title: {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print("-" * 80)


def update_task(todo_manager):
    """Handle updating a task"""
    print("\n--- UPDATE TASK ---")
    task_id = get_task_id()
    if task_id is None:
        return

    # Check if task exists
    existing_task = todo_manager.get_task_by_id(task_id)
    if existing_task is None:
        print(f"Task with ID {task_id} not found.")
        return

    print(f"Current task: {existing_task}")
    print("Leave blank to keep current value.")

    new_title = input(f"Enter new title (current: '{existing_task.title}'): ").strip()
    if new_title == "":
        new_title = None  # Keep current title

    new_description = input(f"Enter new description (current: '{existing_task.description}'): ").strip()
    if new_description == "":
        new_description = None  # Keep current description

    # If both are empty strings (not None), it means user wants to clear them
    if new_title == "" and new_description == "":
        new_title = ""
        new_description = ""
    elif new_title == "":
        new_title = None
    elif new_description == "":
        new_description = None

    try:
        if todo_manager.update_task(task_id, new_title, new_description):
            print("Task updated successfully!")
        else:
            print("Failed to update task.")
    except ValueError as e:
        print(f"Error updating task: {e}")


def delete_task(todo_manager):
    """Handle deleting a task"""
    print("\n--- DELETE TASK ---")
    task_id = get_task_id()
    if task_id is None:
        return

    # Check if task exists and show it before deletion
    existing_task = todo_manager.get_task_by_id(task_id)
    if existing_task is None:
        print(f"Task with ID {task_id} not found.")
        return

    print(f"Task to delete: {existing_task}")

    confirm = input("Are you sure you want to delete this task? (yes/no): ").strip().lower()
    if confirm in ['yes', 'y']:
        if todo_manager.delete_task(task_id):
            print("Task deleted successfully!")
        else:
            print("Failed to delete task.")
    else:
        print("Deletion cancelled.")


def mark_task_complete(todo_manager):
    """Handle marking a task as complete"""
    print("\n--- MARK TASK COMPLETE ---")
    task_id = get_task_id()
    if task_id is None:
        return

    if todo_manager.mark_complete(task_id):
        print(f"Task with ID {task_id} marked as complete!")
    else:
        print(f"Task with ID {task_id} not found.")


def mark_task_incomplete(todo_manager):
    """Handle marking a task as incomplete"""
    print("\n--- MARK TASK INCOMPLETE ---")
    task_id = get_task_id()
    if task_id is None:
        return

    if todo_manager.mark_incomplete(task_id):
        print(f"Task with ID {task_id} marked as incomplete!")
    else:
        print(f"Task with ID {task_id} not found.")


def main():
    """Main function to run the todo application"""
    print("Welcome to the Todo In-Memory Console Application!")
    print("This application stores tasks in memory only (no persistence).")

    todo_manager = TodoManager()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            add_task(todo_manager)
        elif choice == 2:
            view_tasks(todo_manager)
        elif choice == 3:
            update_task(todo_manager)
        elif choice == 4:
            delete_task(todo_manager)
        elif choice == 5:
            mark_task_complete(todo_manager)
        elif choice == 6:
            mark_task_incomplete(todo_manager)
        elif choice == 7:
            print("\nThank you for using the Todo Application. Goodbye!")
            break


if __name__ == "__main__":
    main()