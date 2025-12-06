from puruxzi.task_registry import register_task

@register_task("hello")
class HelloTask:
    def run(self):
        print("Hello from HelloTask!")
