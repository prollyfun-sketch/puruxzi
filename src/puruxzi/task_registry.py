_task_registry = {}

def register_task(name):
    def decorator(cls):
        _task_registry[name] = cls
        return cls
    return decorator

class TaskRegistry:
    @staticmethod
    def get_task(name):
        return _task_registry.get(name)

    @staticmethod
    def list_tasks():
        return list(_task_registry.keys())
