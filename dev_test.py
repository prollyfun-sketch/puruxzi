# File: dev_test.py

from organs.kernel.kernel import PuruxziSystem

system = PuruxziSystem()

# --- Test 1: Execute Goal ---
goal_result = system.execute_goal("compile project status")
print("--- EXECUTE GOAL RESULT ---")
print(goal_result)

# --- INTERPRET AND RUN TASK ---
print("\n--- INTERPRET AND RUN TASK ---")
result = system.interpret_and_run_task("build_report")
print(result)
