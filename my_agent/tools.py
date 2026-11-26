"""Tools the model can call: read_file, write_file, list_dir, search, run_command."""
from pathlib import Path


def read_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

# TODO: write_file, list_dir, search_in_files, run_command
