"""
Brain Organ
Cognitive reasoning and guidance organ for the Puruxzi Seed.

Seed-level responsibilities:
- Provide a minimal interface for "planning" and "interpreting" tasks.
- No AI/LLM logic here yet — only structural placeholders.
- Kernel, Operator, and Tasks will call into this organ later.
"""

from typing import Any, Dict, List
from organs.status_checker import status_checker  # <- add import

class Brain:
    def __init__(self) -> None:
        # Holds the last plan generated (simple deterministic store)
        self.last_plan: List[str] = []

    # -----------------------------
    # Planning
    # -----------------------------
    def plan(self, goal: str) -> List[str]:
        """
        Very simple deterministic "planning" placeholder.
        Takes a goal string and breaks it into steps.
        (Later phases will replace this with real logic.)
        """
        steps = [
            f"Analyze goal: {goal}",
            f"Determine requirements for: {goal}",
            f"Produce structured steps for: {goal}"
        ]

        self.last_plan = steps
        return steps

    # -----------------------------
    # Interpretation
    # -----------------------------
    def interpret(self, data: Any) -> Dict[str, Any]:
        """
        Basic deterministic interpretation stub.
        Returns structure describing the input.
        """
        return {
            "input_type": str(type(data)),
            "summary": f"Received data: {data}",
            "token_count": len(str(data))
        }

    # -----------------------------
    # Thinking
    # -----------------------------
    def think(self, thoughts: List[str]) -> str:
        """
        Optional orchestration hook for status introspection.
        """
        if "status" in thoughts:
            print("[Brain] Detected system status inquiry.")
            result = status_checker.run()
            print("[Brain] Status report ready.")
            return str(result)
        return "[Brain] No actionable thoughts."

    # -----------------------------
    # Status
    # -----------------------------
    def status(self) -> str:
        return "[Brain] Online"

    def attach_context(self, context):
        self.context = context
