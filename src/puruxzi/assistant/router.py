import re
from puruxzi.assistant.tools.dolphin import DolphinTool
from puruxzi.assistant.tools.calculator import CalculatorTool

ROUTES = [
    (r"dolphin", DolphinTool),
    (r"^calc\s", CalculatorTool),
]

def route_tool(message: str):
    for pattern, tool_cls in ROUTES:
        if re.search(pattern, message, re.IGNORECASE):
            return tool_cls()
    return None
