"""All terminal output (rich) lives here."""
from rich.console import Console
from rich.panel import Panel

console = Console()


def banner(version: str, model: str, workspace: str):
    console.print(Panel(f"version {version}\nmodel {model}\nworkspace {workspace}", title="my-agent"))


def info(msg: str):
    console.print(f"[dim]{msg}[/dim]")


def error(msg: str):
    console.print(Panel(msg, title="Error", border_style="red"))
