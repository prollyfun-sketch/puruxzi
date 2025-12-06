# aurelium/puruxzi/operator.py
import typer
from puruxzi import agent_operator as operator

operator_app = typer.Typer(help="Operator mode")

@operator_app.command()
def demo():
    print("[operator] demo command works!")
