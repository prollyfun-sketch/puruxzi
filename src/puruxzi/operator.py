from puruxzi.task_registry import TaskRegistry

def operator_app(task_name):
    task_cls = TaskRegistry.get_task(task_name)
    if task_cls is None:
        print(f"[!] Task '{task_name}' not found.")
        return
    try:
        task = task_cls()
        task.run()
    except Exception as e:
        print(f"[!] Failed to run task '{task_name}': {e}")
