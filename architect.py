import json
import os
from datetime import datetime
import typer

architect_app = typer.Typer()

MEMORY_PATH = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return {"projects": []}
    with open(MEMORY_PATH, "r") as f:
        try:
            return json.load(f)
        except:
            return {"projects": []}


def save_memory(data):
    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=4)


@architect_app.command()
def plan(project_name: str, description: str = "No description"):
    """Creates a blueprint and stores it into memory.json"""

    memory = load_memory()

    blueprint = {
        "name": project_name,
        "description": description,
        "timestamp": datetime.utcnow().isoformat(),
        "files": [
            {"name": "data_pipeline.py", "path": "data_pipeline.py"},
            {"name": "model_trainer.py", "path": "model_trainer.py"},
            {"name": "evaluation.py", "path": "evaluation.py"},
            {"name": "requirements.txt", "path": "requirements.txt"},
            {"name": "README.md", "path": "README.md"},
        ]
    }

    memory["projects"].append(blueprint)
    save_memory(memory)

    print(f"[✔] Blueprint stored for: {project_name}")
