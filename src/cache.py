import time
from typing import Any, Optional, Dict

class Cache:
    def __init__(self, ttl: int = 600):
        self.ttl = ttl  # время жизни в секундах (10 минут)
        self._data: Dict[str, tuple[Any, float]] = {}
    
    def get(self, key: str) -> Optional[Any]:
        if key in self._data:
            value, expires = self._data[key]
            if time.time() < expires:
                return value
            del self._data[key]
        return None
    
    def set(self, key: str, value: Any) -> None:
        self._data[key] = (value, time.time() + self.ttl)
    
    def clear(self, key: str) -> None:
        self._data.pop(key, None)