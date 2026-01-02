"""
Task class for the Todo In-Memory Console Application
Represents a single task with id, title, description, and completion status
"""

class Task:
    def __init__(self, task_id, title, description=""):
        """
        Initialize a new Task instance

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (required, 1-200 characters)
            description (str): Description of the task (optional, max 1000 characters)
        """
        self.id = self._validate_id(task_id)
        self.title = self._validate_title(title)
        self.description = self._validate_description(description)
        self.completed = False  # Default status is incomplete

    def _validate_id(self, task_id):
        """Validate that the ID is a positive integer"""
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        return task_id

    def _validate_title(self, title):
        """Validate that the title is a non-empty string between 1-200 characters"""
        if not isinstance(title, str):
            raise ValueError("Task title must be a string")
        if not title or len(title) < 1 or len(title) > 200:
            raise ValueError("Task title must be between 1 and 200 characters")
        return title

    def _validate_description(self, description):
        """Validate that the description is a string with max 1000 characters"""
        if not isinstance(description, str):
            raise ValueError("Task description must be a string")
        if len(description) > 1000:
            raise ValueError("Task description must be 1000 characters or less")
        return description

    def to_dict(self):
        """Convert the task to a dictionary representation"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    def __str__(self):
        """String representation of the task for display purposes"""
        status = "[✓]" if self.completed else "[ ]"
        return f"{status} ID: {self.id} | Title: {self.title} | Description: {self.description}"

    def __repr__(self):
        """Detailed string representation of the task"""
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"