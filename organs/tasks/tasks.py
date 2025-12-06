"""
Tasks Organ
Task execution and pipeline organ for the Puruxzi Seed.

Seed-level responsibilities:
- Maintain a very small, deterministic API for registering and running tasks.
- Keep everything in-memory for now (no background workers, no threads).
- Provide a foundation that Kernel/Operator/Brain can call later.
"""

from typing import Callable, Any, Dict

class Tasks:
    def __init__(self) -> None:
        # Simple in-memory registry: {task_name: callable}

        # Import your task module(s) here
        from . import hello
        from . import build_report  # ← Add more as needed

        # Register the task name and function
        self._registry: Dict[str, Callable[..., Any]] = {
            "hello": hello.run,
            "build_report": build_report.run,  # ← Add here too
        }

    # -----------------------------
    # Registration
    # -----------------------------
    def register(self, name: str, func: Callable[..., Any]) -> None:
        """
        Register a callable under a task name.
        Example usage (later, from kernel/brain):
            tasks.register("build_project", some_function)
        """
        if not callable(func):
            raise TypeError(f"[Tasks] func for '{name}' is not callable")
        self._registry[name] = func

    def unregister(self, name: str) -> None:
        """
        Remove a task from the registry, if it exists.
        """
        self._registry.pop(name, None)

    def list_tasks(self) -> Dict[str, Callable[..., Any]]:
        """
        Return a shallow copy of the internal registry.
        """
        return dict(self._registry)

    # -----------------------------
    # Execution
    # -----------------------------
    def run(self, name: str, *args, **kwargs) -> Any:
        """
        Run a registered task synchronously and return its result.
        """
        if name not in self._registry:
            raise KeyError(f"[Tasks] No task registered with name '{name}'")

        func = self._registry[name]
        return func(*args, **kwargs)

    # Optional proof-of-life hook
    def status(self) -> str:
        return f"[Tasks] Online (registered={len(self._registry)})"
