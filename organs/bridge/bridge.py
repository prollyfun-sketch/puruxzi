from organs.tasks import setup_tasks
from organs.operator.operator import Operator
from organs.brain.brain import Brain
from organs.kernel.kernel import load_kernel_map  # ✅ new import
from organs.kernel.context import Context         # ✅ new import

class Bridge:
    def __init__(self):
        tasks = setup_tasks()
        self.op = Operator(tasks=tasks)
        self.brain = Brain()

        # ✅ setup context with kernel map
        self.context = Context(kernel_map=load_kernel_map())
        self.brain.attach_context(self.context)

    def run_prompt(self, prompt):
        plan = self.brain.plan(prompt)
        return self.op.execute_plan(plan)
