import time
from typing import Any, Optional

class LocalCache:
    """InMemory Cache đơn giản cho từng dịch vụ"""
    def __init__(self):
        self._cache = {}
        self._expiry = {}

    def set(self, key: str, value: Any, ttl: int = 300):
        self._cache[key] = value
        self._expiry[key] = time.time() + ttl
    
    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None

        # Kiểm tra hết hạn
        if time.time() > self._expiry[key]:
            self.delete(key)
            return None

        return self._cache[key]

    def delete(self, key: str):
        self._cache.pop(key, None)
        self._expiry.pop(key, None)
