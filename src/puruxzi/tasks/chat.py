from puruxzi.task_registry import register_task
from puruxzi.assistant.main import assistant

@register_task("chat")
class ChatTask:
    def run(self):
        print("🤖 Ask me something (type 'exit' to quit)...")
        while True:
            user_input = input("> ")
            if user_input.strip().lower() == "exit":
                print("👋 Goodbye.")
                break
            response = assistant(user_input)
            print(response)
