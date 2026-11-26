"""Entry point: input loop and slash commands (/help, /model, /exit)."""
from pathlib import Path
import typer
from . import __version__
from .config import DEFAULT_MODEL
from . import ui

app = typer.Typer(add_completion=False)


@app.command()
def main():
    ui.banner(__version__, DEFAULT_MODEL, str(Path.cwd()))
    # TODO: prompt_toolkit input loop -> agent.run(...)


if __name__ == "__main__":
    app()
