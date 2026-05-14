import asyncio
from contextlib import asynccontextmanager
# pyrefly: ignore [missing-import]
from fastapi import FastAPI

# 1. Import cấu hình và hạ tầng từ core
from libs.core.config import settings
from libs.core.logger import logger
from libs.core.http.middlewares import add_custom_middlewares
from libs.core.http.exceptions import register_exception_handlers
from libs.core.http.health_controller import router as health_router

# 2. Import gRPC Server để chạy nền
from .grpc_server import serve_grpc

# 3. Định nghĩa Lifespan để chạy song song HTTP và gRPC
@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP: Bật gRPC Server
    logger.info("--- Khởi động MES Microservice ---")
    logger.info("🚀 Đang khởi động gRPC Server tại port 50051...")
    grpc_task = asyncio.create_task(serve_grpc())
    
    yield # App FastAPI bắt đầu nhận request ở port 8000
    
    # SHUTDOWN: Dọn dẹp
    logger.info("--- Đang tắt MES Microservice ---")
    grpc_task.cancel()
    try:
        await grpc_task
    except asyncio.CancelledError:
        logger.info("✅ gRPC Server đã dừng an toàn.")

# 4. Khởi tạo FastAPI App
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

# 5. Đăng ký các Middleware và Router
add_custom_middlewares(app)
register_exception_handlers(app)
app.include_router(health_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "status": "Running",
        "grpc_port": 50051
    }
