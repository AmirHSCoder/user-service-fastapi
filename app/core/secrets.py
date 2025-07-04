import os
from pathlib import Path


def get_secret(key: str) -> str:
    """Retrieve secrets from env vars or Docker secrets."""
    if key in os.environ:
        return os.environ[key]
    secret_path = Path("/run/secrets") / key
    if secret_path.exists():
        return secret_path.read_text().strip()
    return ""
