"""
Kernel Organ
Core system coordinator.

Runs all organs together and exposes a unified status().
"""

import json
from organs.brain.brain import Brain
from organs.operator.operator import Operator

def load_kernel_map():
    with open("kernel_map.json", "r") as f:
        return json.load(f)

class Kernel:
    def __init__(self):
        self.status_flag = "OK"

    def status(self):
        return {"kernel_status": self.status_flag}


class PuruxziSystem:
    """
    High-level system wrapper that wires all organs together.
    ONLY wiring — no logic.
    """

    def __init__(self):
        # -------------------------
        # Import *inside* __init__ to prevent circular imports
        # -------------------------
        from organs.brain.brain import Brain
        from organs.fs.fs import FS
        from organs.tasks.tasks import Tasks
        from organs.operator.operator import Operator
        from organs.mentor.mentor import Mentor

        # -------------------------
        # Instantiate organs
        # -------------------------
        self.kernel = Kernel()
        self.brain = Brain()
        self.fs = FS()
        self.tasks = Tasks()
        self.operator = Operator(tasks=self.tasks)
        self.mentor = Mentor()

    # -------------------------------------------------
    # Bridge: Brain -> Operator
    # -------------------------------------------------
    def execute_goal(self, goal: str):
        steps = self.brain.plan(goal)
        return self.operator.execute_plan(steps)

    # -------------------------------------------------
    # Bridge: Brain -> Tasks
    # -------------------------------------------------
    def interpret_and_run_task(self, data: str):
        interpretation = self.brain.interpret(data)
        task_name = interpretation.get("summary", "").replace("Received data: ", "")

        try:
            return self.tasks.run(task_name)
        except Exception as e:
            return {"error": str(e)}

    # -----------------------------------------------------
    # Bridge: FS -> Tasks (file-driven execution)
    # -----------------------------------------------------
    def run_file_task(self, filepath: str):
        content = self.fs.read_file(filepath)
        filename = filepath.split("/")[-1]
        task_name = filename.replace(".txt", "").replace(".task", "")

        try:
            return self.tasks.run(task_name, content)
        except Exception as e:
            return {"error": str(e)}

    # -----------------------------------------------------
    # SYSTEM STATUS
    # -----------------------------------------------------
    def status(self):
        return {
            "kernel": self.kernel.status(),
            "brain": self.brain.status(),
            "fs": self.fs.status(),
            "tasks": self.tasks.status(),
            "operator": self.operator.status(),
            "mentor": self.mentor.status(),
        }


if __name__ == "__main__":
    system = PuruxziSystem()
    print("[Kernel] Puruxzi boot complete.")
    print(system.status())
