# runner.py
import sys
from organs.tasks import setup_tasks

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python runner.py <topic>")
        sys.exit(1)

    topic = " ".join(sys.argv[1:])
    tasks = setup_tasks()
    print(tasks.run("deep_dive_research", topic))
