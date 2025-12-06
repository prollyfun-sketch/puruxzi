import os
from datetime import datetime

LOG_PATH = "memory.log"

def write_log(entry: str):
    timestamp = datetime.utcnow().isoformat()
    line = f"[{timestamp}] {entry}\n"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)
