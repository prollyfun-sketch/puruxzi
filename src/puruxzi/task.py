# src/puruxzi/task.py
class Task:
    """Base class for all tasks."""
    def run(self):
        """Execute the task. Must be overridden by subclasses."""
        raise NotImplementedError("Task subclasses must implement run().")
