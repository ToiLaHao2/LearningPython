from typing import Any, Optional
from .local_cache import LocalCache
from .redis_cache import RedisCache
from libs.core.config import settings

class CacheManager:
    """
    Bộ não điều phối Cache.
    Luồng hoạt động (Lazy Loading):
    1. Tìm trong Local Cache trước (nhanh nhất, không tốn network).
    2. Nếu không có, tìm trên Redis.
    3. Nếu Redis có, lưu ngược lại vào Local Cache để lần sau lấy cho nhanh.
    """
    def __init__(self, redis_url: str = settings.REDIS_URL):
        self.local_cache = LocalCache()
        self.redis_cache = RedisCache(redis_url)

    async def get(self, key: str) -> Optional[Any]:
        # 1. Thử lấy từ Local Cache (RAM)
        local_data = self.local_cache.get(key)
        if local_data is not None:
            print(f"[CACHE] HIT Local Cache: {key}")
            return local_data

        # 2. Nếu Local không có, gọi qua Redis
        print(f"[CACHE] MISS Local Cache. Thử lấy từ Redis: {key}")
        redis_data = await self.redis_cache.get(key)
        
        if redis_data is not None:
            # 3. Lưu ngược lại vào Local Cache để dùng cho lần sau
            print(f"[CACHE] HIT Redis. Lưu ngược vào Local Cache: {key}")
            self.local_cache.set(key, redis_data, ttl=300) # Lưu trong RAM 5 phút
            return redis_data
            
        print(f"[CACHE] MISS Redis luôn: {key}")
        return None

    async def set(self, key: str, value: Any, ttl: int = 300) -> None:
        """Lưu đồng thời vào cả Local và Redis"""
        # Lưu vào Local
        self.local_cache.set(key, value, ttl)
        # Bắn lên Redis
        await self.redis_cache.set(key, value, ttl)

    async def delete(self, key: str) -> None:
        """Xóa đồng thời ở cả 2 nơi"""
        self.local_cache.delete(key)
        await self.redis_cache.delete(key)

    async def close(self):
        """Dọn dẹp kết nối khi tắt server"""
        await self.redis_cache.close()
