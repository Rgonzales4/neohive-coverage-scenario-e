from app.config import load_config
from lib.http_client import HttpClient


def register_routes(client: HttpClient) -> dict:
    config = load_config()
    return {
        "/health": lambda: client.get("/health"),
        "/version": lambda: client.get("/version"),
        "/config": lambda: config,
    }
