import typer

mentor_app = typer.Typer(help="Mentor mode")

@mentor_app.command()
def demo():
    print("[mentor] demo command works!")
