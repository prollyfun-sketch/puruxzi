import os
import json

MEMORY_PATH = os.path.join(os.path.dirname(__file__), "memory.json")
SEED_VERSION = "1.0.0"

def init_memory():
    if not os.path.exists(MEMORY_PATH):
        data = {
            "seed_version": SEED_VERSION,
            "projects": []
        }
        save_memory(data)
        print("[+] Created new memory.json")

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        init_memory()

    try:
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[!] memory.json is corrupted — repairing…")
        init_memory()
        return load_memory()

def save_memory(data):
    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=4)
