import random
from puruxzi.assistant.memory import write_log
from puruxzi.assistant.router import route_tool
from puruxzi.assistant.router import route_tool

def assistant(message: str) -> str:
    try:
        tool = route_tool(message)
        result = tool.run(message)
        return result
    except Exception as e:
        return f"❌ Sorry, something went wrong: {e}"

def assistant(message: str) -> str:
    write_log(f"User: {message}")

    tool = route_tool(message)
    if tool:
        result = tool().run(message)
        write_log(f"Tool: {result}")
        return result

    return "🤖 I don't know how to help with that."

def assistant(message: str) -> str:
    message = message.strip().lower()

    # Dolphin facts tool
    dolphin_facts = [
        "Dolphins are marine mammals known for their intelligence.",
        "They use echolocation to hunt and navigate.",
        "Some dolphin species can swim up to 25 miles per hour.",
        "Dolphins are highly social and live in groups called pods.",
    ]
    if "dolphin" in message:
        return random.choice(dolphin_facts)

    # Calculator tool
    if message.startswith("calc "):
        expr = message[5:]
        try:
            result = eval(expr)
            return f"🧮 Result: {result}"
        except Exception as e:
            return f"Error: {e}"

    return "🤖 I'm not sure about that yet!"
