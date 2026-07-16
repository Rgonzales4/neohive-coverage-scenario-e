import os


def load_config() -> dict:
    return {
        "base_url": os.environ.get("SERVICE_URL", "https://example.test"),
        "timeout_seconds": int(os.environ.get("SERVICE_TIMEOUT", "10")),
        "retries": int(os.environ.get("SERVICE_RETRIES", "3")),
    }
