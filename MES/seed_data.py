import asyncio
from libs.core.cache.manager import CacheManager

async def seed():
    try:
        cache = CacheManager()
        # Tạo bản đồ 5x5: 0 là đường đi, 1 là vật cản
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        
        print("⏳ Đang nạp dữ liệu lên Redis...")
        await cache.set("warehouse:WH001:grid", grid)
        
        # Kiểm tra lại thực tế trên Redis
        check_data = await cache.get("warehouse:WH001:grid")
        if check_data:
            print("✨ CHÚC MỪNG: Dữ liệu đã được nạp lên Redis thành công!")
        else:
            print("❌ THẤT BẠI: Không thể nạp dữ liệu. Vui lòng kiểm tra lại cấu hình REDIS_URL trong .env")
            
    except Exception as e:
        print(f"💥 LỖI KẾT NỐI: {str(e)}")

if __name__ == "__main__":
    asyncio.run(seed())
