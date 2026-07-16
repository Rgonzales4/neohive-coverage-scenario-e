from collections import OrderedDict


class LruCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._store: OrderedDict = OrderedDict()

    def get(self, key: str):
        if key not in self._store:
            return None
        self._store.move_to_end(key)
        return self._store[key]

    def put(self, key: str, value) -> None:
        self._store[key] = value
        self._store.move_to_end(key)
        if len(self._store) > self.capacity:
            self._store.popitem(last=False)
