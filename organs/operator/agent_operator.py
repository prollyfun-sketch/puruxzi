# organs/operator/operator.py or agent_operator.py

from organs.status_checker import status_checker

def run_status():
    report = status_checker.run()
    print("[Operator] Status report received.")
