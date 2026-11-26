"""Config: API key, model name, permission mode. Cross-platform paths via platformdirs."""
import os
from pathlib import Path
from platformdirs import user_config_dir

APP_NAME = "my-agent"
CONFIG_DIR = Path(user_config_dir(APP_NAME))
DEFAULT_MODEL = "gemini-2.5-flash"
PERMISSIONS = "ask"  # ask | auto


def get_api_key() -> str | None:
    return os.environ.get("GEMINI_API_KEY")
