import time


def with_retries(fn, attempts: int = 3, delay: float = 0.1):
    last_error = None
    for attempt in range(attempts):
        try:
            return fn()
        except Exception as err:  # noqa: BLE001
            last_error = err
            time.sleep(delay * (attempt + 1))
    raise last_error
