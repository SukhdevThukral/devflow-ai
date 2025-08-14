import typer
app = typer.Typer(help="Hey niqqas")
@app.command()
def hello(name: str):
    """
    Greets the user with their name.
    """
    print(f"Hello, {name}! Welcome to the DevFlow AI v0.")

if __name__ == "__main__":
    app()
    