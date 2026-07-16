from app.config import load_config
from lib.http_client import HttpClient
from lib.cache import LruCache


def run() -> None:
    config = load_config()
    client = HttpClient(base_url=config["base_url"])
    cache = LruCache(capacity=128)

    for path in ("/health", "/version"):
        if (hit := cache.get(path)) is not None:
            print(path, hit, "(cached)")
            continue
        body = client.get(path)
        cache.put(path, body)
        print(path, body)


if __name__ == "__main__":
    run()
