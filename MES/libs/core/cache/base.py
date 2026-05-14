from abc import ABC, abstractmethod
from typing import Any, Optional

class BaseCache(ABC):
    """Lớp trừu tượng định nghĩa các phương thức chung cho tất cả các loại Cache"""
    
    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        pass

    @abstractmethod
    async def set(self, key: str, value: Any, ttl: int = 300) -> None:
        pass

    @abstractmethod
    async def delete(self, key: str) -> None:
        pass
