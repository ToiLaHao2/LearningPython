import asyncio
from libs.core.cache.manager import CacheManager

async def seed():
    cache = CacheManager()
    # Tạo bản đồ 5x5: 0 là đường đi, 1 là vật cản
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    await cache.set("warehouse:WH001:grid", grid)
    print("✅ Đã nạp bản đồ 'WH001' vào Redis thành công!")

if __name__ == "__main__":
    asyncio.run(seed())
