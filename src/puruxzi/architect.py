# src/puruxzi/architect.py

import os
import json
from datetime import datetime
import typer

architect_app = typer.Typer(help="Puruxzi Architect")

MEMORY_PATH = os.path.join(os.path.dirname(__file__), "memory.json")


# === Persistence ===
def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return {"projects": []}
    try:
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"projects": []}


def save_memory(data):
    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=4)


# === Architect Class (LLM interface or callable) ===
class Architect:
    def __init__(self, model=None):
        self.model = model or self.default_model()

    def default_model(self):
        # TODO: Plug in your real model (e.g., GPT-4, Claude, LM Studio, etc.)
        return None

    def plan(self, goal: str) -> dict:
        """
        Generate a plan from a high-level goal (stubbed right now).
        Replace this with a call to your LLM.
        """
        return {
            "files": {
                "main.py": {
                    "functions": ["main"]
                },
                "utils.py": {
                    "functions": ["helper_function"]
                }
            },
            "description": f"Auto-plan for: {goal}"
        }


# === CLI: Blueprint Generator ===
@architect_app.command()
def module(name: str, description: str = "No description"):
    """
    Creates a Puruxzi MODULE blueprint (organ, engine, component, task).
    """
    memory = load_memory()

    blueprint = {
        "name": name,
        "description": description,
        "timestamp": datetime.utcnow().isoformat(),
        "type": "module",
        "files": [
            {"name": f"{name}.py", "path": f"organs/{name}/{name}.py"},
            {"name": "README.md", "path": f"organs/{name}/README.md"},
            {"name": "requirements.txt", "path": f"organs/{name}/requirements.txt"},
        ]
    }

    memory["projects"].append(blueprint)
    save_memory(memory)

    print(f"[+] Module blueprint created for: {name}")
    print(f"[+] Stored in memory.json")
