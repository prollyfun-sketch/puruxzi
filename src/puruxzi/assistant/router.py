from puruxzi.assistant.tools.dolphin import DolphinTool
from puruxzi.assistant.tools.calculator import CalculatorTool
from puruxzi.assistant.tools.quote import QuoteTool

def route_tool(message: str):
    message = message.lower()

    if "dolphin" in message:
        return DolphinTool()
    elif "calculate" in message or "add" in message or "plus" in message:
        return CalculatorTool()
    elif "quote" in message or "inspire" in message:
        return QuoteTool()
    else:
        return None
