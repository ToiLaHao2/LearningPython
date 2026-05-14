import json
from typing import Any, Optional
# pyrefly: ignore [missing-import]
import redis.asyncio as redis
from .base import BaseCache
from libs.core.config import settings

class RedisCache(BaseCache):
    """Lớp xử lý kết nối và thao tác với Redis Server"""
    
    def __init__(self, redis_url: str = settings.REDIS_URL):
        # Khởi tạo connection pool tới Redis
        self.redis_client = redis.from_url(redis_url, decode_responses=True)

    async def get(self, key: str) -> Optional[Any]:
        try:
            data = await self.redis_client.get(key)
            if data:
                # Vì Redis lưu dạng chuỗi, ta cần parse JSON về lại Object/List
                return json.loads(data)
            return None
        except Exception as e:
            print(f"Redis GET Error: {e}")
            return None

    async def set(self, key: str, value: Any, ttl: int = 300) -> None:
        try:
            # Chuyển Object/List thành JSON string trước khi lưu
            json_data = json.dumps(value)
            await self.redis_client.set(key, json_data, ex=ttl)
        except Exception as e:
            print(f"Redis SET Error: {e}")

    async def delete(self, key: str) -> None:
        try:
            await self.redis_client.delete(key)
        except Exception as e:
            print(f"Redis DELETE Error: {e}")
            
    async def close(self):
        """Đóng kết nối khi app tắt"""
        await self.redis_client.close()
