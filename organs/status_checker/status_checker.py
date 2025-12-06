# organs/status_checker/status_checker.py

import time
import psutil

def run():
    print("[Status Checker] Running system status check...")
    
    # status check
    status = {
        "uptime": time.time(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage('/')._asdict(),
        "health": "OK"
    }
    print("[Status Checker] Report:")
    for key, value in status.items():
        print(f"  {key}: {value}")

    return status

if __name__ == "__main__":
    run()
