import os
import json
import typer

engineer_app = typer.Typer(help="Puruxzi Engineer")

MEMORY_PATH = os.path.join(os.path.dirname(__file__), "memory.json")

def load_latest(name: str):
    if not os.path.exists(MEMORY_PATH):
        print("[-] memory.json missing")
        return None

    with open(MEMORY_PATH, "r") as f:
        data = json.load(f)

    for entry in reversed(data.get("projects", [])):
        if entry.get("name") == name:
            return entry

    print(f"[-] No blueprint found with name '{name}'")
    return None

def create_files(blueprint):
    for file in blueprint.get("files", []):
        file_path = file["path"]
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as f:
            if file_path.endswith(".py"):
                f.write(f"# {file['name']}\n\n")
                f.write("def main():\n    pass\n")
            elif file_path.endswith(".md"):
                f.write(f"# {file['name']}\n\nTODO: Describe the module.")
            elif file_path.endswith(".txt"):
                f.write("# Dependencies\n")

    print(f"[+] Created {len(blueprint['files'])} files for {blueprint['name']}")

@engineer_app.command()
def build(name: str):
    """
    Builds (materializes) a Puruxzi module from blueprint.
    """
    bp = load_latest(name)
    if not bp:
        print(f"[!] No blueprint found for: {name}")
        return

    create_files(bp)
    print(f"[✓] Module built at: organs/{name}/")

if __name__ == "__main__":
    engineer_app()
