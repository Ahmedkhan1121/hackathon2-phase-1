"""
TodoManager class for the Todo In-Memory Console Application
Handles all business logic for task operations
"""

from task import Task


class TodoManager:
    def __init__(self):
        """
        Initialize a new TodoManager instance
        Creates an empty task list and starts ID counter at 1
        """
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description=""):
        """
        Add a new task with the given title and description

        Args:
            title (str): Title of the task (required)
            description (str): Description of the task (optional)

        Returns:
            Task: The newly created task
        """
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        """
        Get all tasks in the system

        Returns:
            list: List of all Task objects
        """
        return self.tasks

    def get_task_by_id(self, task_id):
        """
        Get a specific task by its ID

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Task: The task with the given ID, or None if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, title=None, description=None):
        """
        Update the title and/or description of a task by ID

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            bool: True if task was updated successfully, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = task._validate_title(title)
        if description is not None:
            task.description = task._validate_description(description)

        return True

    def delete_task(self, task_id):
        """
        Delete a task by its ID

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if task was deleted successfully, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def mark_complete(self, task_id):
        """
        Mark a task as complete by its ID

        Args:
            task_id (int): The ID of the task to mark complete

        Returns:
            bool: True if task was marked complete, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = True
        return True

    def mark_incomplete(self, task_id):
        """
        Mark a task as incomplete by its ID

        Args:
            task_id (int): The ID of the task to mark incomplete

        Returns:
            bool: True if task was marked incomplete, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = False
        return True

    def get_next_id(self):
        """
        Get the next available ID for a new task

        Returns:
            int: The next available ID
        """
        return self.next_id