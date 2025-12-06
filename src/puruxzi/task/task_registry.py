# src/puruxzi/task_registry.py
class TaskRegistry:
    """Registry for task classes."""
    _tasks = {}

    @classmethod
    def register(cls, name, task_cls):
        """Register a task class under a name."""
        cls._tasks[name] = task_cls

    @classmethod
    def get_task(cls, name):
        """Retrieve a task class by name."""
        return cls._tasks.get(name)

    @classmethod
    def list_tasks(cls):
        """List all registered task names."""
        return list(cls._tasks.keys())

def register_task(name):
    """Decorator to register a task class under a given name."""
    def decorator(task_cls):
        TaskRegistry.register(name, task_cls)
        return task_cls
    return decorator
