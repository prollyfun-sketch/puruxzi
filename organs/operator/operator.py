# Operator Organ
# Executes steps and can trigger registered tasks.

from organs.status_checker import status_checker
from typing import List, Any, Dict
from organs.tasks.tasks import Tasks   # <-- NEW (bridge to Tasks)

class Operator:
    """
    Operator executes structured steps produced by the Brain,
    and can also trigger named tasks from the Tasks organ.
    """

    def __init__(self, tasks: Tasks = None) -> None:
        # tasks gets injected later by Kernel
        self.tasks = tasks

    # -------------------------
    # Execute a single step
    # -------------------------
    def execute_step(self, step: str) -> str:
        """
        Deterministic executor for a single step.
        """
        return f"[Operator] executing step -> {step}"

    # -------------------------
    # Execute a full plan
    # -------------------------
    def execute_plan(self, steps: List[str]) -> Dict[str, Any]:
        transcript = []
        for step in steps:
            transcript.append(self.execute_step(step))

        return {
            "type": "plan_execution",
            "steps": len(steps),
            "transcript": transcript
        }

    # -------------------------
    # NEW: Run a registered task
    # -------------------------
    def run_task(self, name: str, *args, **kwargs) -> Any:
        """
        Bridge to the Tasks organ.
        """
        if not self.tasks:
            raise RuntimeError("Tasks organ not attached to Operator")
        return self.tasks.run(name, *args, **kwargs)

    # -------------------------
    # Status
    # -------------------------
    def status(self) -> Dict[str, str]:
        return {"operator_status": "OK"}

if __name__ == "__main__":
    print("[Operator] Booting direct run mode...")
    report = status_checker.run()
    print("[Operator] Status received:")
    print(report)
