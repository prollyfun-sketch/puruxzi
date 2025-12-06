# src/puruxzi/cli.py

import os
import typer
from puruxzi.operator import operator_app

app = typer.Typer(help="Puruxzi Multimode CLI")

@app.command()
def run_task(task_name: str):
    """
    Runs a registered task by name.
    """
    try:
        print(f"[+] Running task: {task_name}")
        operator_app(task_name)
    except Exception as e:
        print(f"[!] Failed to run task '{task_name}': {e}")

@app.command()
def doctor():
    """
    Runs full diagnostic of the Puruxzi seed environment.
    """
    try:
        from .memory import MEMORY_PATH, load_memory
    except ImportError:
        print("[!] memory module not available")
        return

    print("=== PURUXZI DOCTOR ===")

    if not os.path.exists(MEMORY_PATH):
        print("[!] memory.json missing")
        return

    print("[+] memory.json found")

    try:
        mem = load_memory()
        print("[+] memory.json valid JSON")
    except Exception:
        print("[!] memory.json invalid")
        return

    seed_version = mem.get("seed_version", "UNKNOWN")
    print(f"[+] Seed version: {seed_version}")
    print("=== DONE ===")


if __name__ == "__main__":
    app()
