import sys
import os
import json

# Make sure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from organs.bridge.bridge import Bridge

# Load kernel map
with open("kernel_map.json", "r") as f:
    kernel_map = json.load(f)

# Read input key from command line
if len(sys.argv) < 2:
    print("Usage: python test_bridge_run.py <kernel_key>")
    sys.exit(1)

key = sys.argv[1]

if key not in kernel_map:
    print(f"Key '{key}' not found in kernel_map.json")
    sys.exit(1)

# Run prompt through Bridge
bridge = Bridge()
result = bridge.run_prompt(kernel_map[key])
print("\n=== FINAL RESPONSE ===\n")
print(result)
