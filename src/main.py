"""
Main entry point for the Todo In-Memory Console Application
Provides a menu-driven interface for all task operations
"""

import sys
import os
# Add the src directory to the path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__)))

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.rule import Rule
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

from todo_manager import TodoManager

# Create a console instance for Rich output
if RICH_AVAILABLE:
    console = Console(force_terminal=True, emoji=False, highlight=False)
else:
    console = None


def display_menu():
    """Display the main menu options to the user"""
    if RICH_AVAILABLE:
        console.print(Panel("[bold blue]TODO APPLICATION[/bold blue]", expand=False))
        console.print(Panel("[bold]MAIN MENU[/bold]", expand=False))
        console.print("1. [green]Add Task[/green]")
        console.print("2. [blue]View Tasks[/blue]")
        console.print("3. [yellow]Update Task[/yellow]")
        console.print("4. [red]Delete Task[/red]")
        console.print("5. [cyan]Mark Task Complete[/cyan]")
        console.print("6. [magenta]Mark Task Incomplete[/magenta]")
        console.print("7. [bold red]Exit[/bold red]")
        console.print("[dim]" + "-"*50 + "[/dim]")
    else:
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
                if RICH_AVAILABLE:
                    console.print("[red]Invalid choice. Please enter a number between 1 and 7.[/red]")
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
        except (ValueError, EOFError, KeyboardInterrupt):
            if RICH_AVAILABLE:
                console.print("\n[red]Invalid input. Please enter a number between 1 and 7.[/red]")
            else:
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
                if RICH_AVAILABLE:
                    console.print("[red]Input cannot be empty. Please try again.[/red]")
                else:
                    print("Input cannot be empty. Please try again.")
        except (EOFError, KeyboardInterrupt):
            if RICH_AVAILABLE:
                console.print("\n[red]Operation cancelled.[/red]")
            else:
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
                if RICH_AVAILABLE:
                    console.print("[red]Task ID must be a positive integer. Please try again.[/red]")
                else:
                    print("Task ID must be a positive integer. Please try again.")
        except ValueError:
            if RICH_AVAILABLE:
                console.print("[red]Invalid input. Please enter a valid number for task ID.[/red]")
            else:
                print("Invalid input. Please enter a valid number for task ID.")
        except (EOFError, KeyboardInterrupt):
            if RICH_AVAILABLE:
                console.print("\n[red]Operation cancelled.[/red]")
            else:
                print("\nOperation cancelled.")
            return None


def add_task(todo_manager):
    """Handle adding a new task"""
    if RICH_AVAILABLE:
        console.print(Panel("[bold]ADD NEW TASK[/bold]", expand=False))
        title = get_task_input("Enter task title: ")
        if title is None:
            return

        description_input = input("Enter task description (optional, press Enter to skip): ").strip()

        try:
            task = todo_manager.add_task(title, description_input)
            console.print(f"[green]Task added successfully! ID: {task.id}[/green]")
        except ValueError as e:
            console.print(f"[red]Error adding task: {e}[/red]")
    else:
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
    if RICH_AVAILABLE:
        console.print(Panel("[bold]ALL TASKS[/bold]", expand=False))
        tasks = todo_manager.get_all_tasks()

        if not tasks:
            console.print("[yellow]No tasks found.[/yellow]")
            return

        # Create a table for tasks
        table = Table(title=f"Total tasks: {len(tasks)}")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Status", style="magenta", no_wrap=True)
        table.add_column("Title", style="green")
        table.add_column("Description", style="yellow")

        for task in tasks:
            status = "[green]✓[/green]" if task.completed else "[red]✗[/red]"
            table.add_row(
                str(task.id),
                status,
                task.title,
                task.description if task.description else "[italic]No description[/italic]"
            )

        console.print(table)
    else:
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
    if RICH_AVAILABLE:
        console.print(Panel("[bold]UPDATE TASK[/bold]", expand=False))
        task_id = get_task_id()
        if task_id is None:
            return

        # Check if task exists
        existing_task = todo_manager.get_task_by_id(task_id)
        if existing_task is None:
            console.print(f"[red]Task with ID {task_id} not found.[/red]")
            return

        console.print(f"Current task: {existing_task}")
        console.print("[italic]Leave blank to keep current value.[/italic]")

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
                console.print("[green]Task updated successfully![/green]")
            else:
                console.print("[red]Failed to update task.[/red]")
        except ValueError as e:
            console.print(f"[red]Error updating task: {e}[/red]")
    else:
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
    if RICH_AVAILABLE:
        console.print(Panel("[bold]DELETE TASK[/bold]", expand=False))
        task_id = get_task_id()
        if task_id is None:
            return

        # Check if task exists and show it before deletion
        existing_task = todo_manager.get_task_by_id(task_id)
        if existing_task is None:
            console.print(f"[red]Task with ID {task_id} not found.[/red]")
            return

        console.print(f"Task to delete: {existing_task}")

        confirm = input("Are you sure you want to delete this task? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            if todo_manager.delete_task(task_id):
                console.print("[green]Task deleted successfully![/green]")
            else:
                console.print("[red]Failed to delete task.[/red]")
        else:
            console.print("[yellow]Deletion cancelled.[/yellow]")
    else:
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
    if RICH_AVAILABLE:
        console.print(Panel("[bold]MARK TASK COMPLETE[/bold]", expand=False))
        task_id = get_task_id()
        if task_id is None:
            return

        if todo_manager.mark_complete(task_id):
            console.print(f"[green]Task with ID {task_id} marked as complete![/green]")
        else:
            console.print(f"[red]Task with ID {task_id} not found.[/red]")
    else:
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
    if RICH_AVAILABLE:
        console.print(Panel("[bold]MARK TASK INCOMPLETE[/bold]", expand=False))
        task_id = get_task_id()
        if task_id is None:
            return

        if todo_manager.mark_incomplete(task_id):
            console.print(f"[green]Task with ID {task_id} marked as incomplete![/green]")
        else:
            console.print(f"[red]Task with ID {task_id} not found.[/red]")
    else:
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
    if RICH_AVAILABLE:
        console.print(Panel("[bold blue]TODO APPLICATION[/bold blue]", title="[bold]Welcome![/bold]", expand=False))
        console.print("[italic]This application stores tasks in memory only (no persistence).[/italic]")
        console.print("[dim]" + "="*50 + "[/dim]")
    else:
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
            if RICH_AVAILABLE:
                console.print("[dim]" + "="*50 + "[/dim]")
                console.print("\n[bold green]Thank you for using the Todo Application. Goodbye![/bold green]")
            else:
                print("\nThank you for using the Todo Application. Goodbye!")
            break


if __name__ == "__main__":
    main()