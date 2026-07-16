from urllib.parse import urljoin


class HttpClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get(self, path: str) -> str:
        url = urljoin(self.base_url, path)
        return f"GET {url} -> 200 OK"

    def post(self, path: str, payload: dict) -> str:
        url = urljoin(self.base_url, path)
        return f"POST {url} ({len(payload)} fields) -> 201 Created"
