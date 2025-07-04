import os


def get_secret(key: str) -> str:
    """Retrieve secrets. Placeholder for integration with secret managers."""
    return os.getenv(key, "")
