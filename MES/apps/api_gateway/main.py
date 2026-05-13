# pyrefly: ignore [missing-import]
from fastapi import FastAPI

# 1. Import cấu hình và hạ tầng từ core
from libs.core.config import settings
from libs.core.http.middlewares import add_custom_middlewares
from libs.core.http.exceptions import register_exception_handlers
from libs.core.http.health_controller import router as health_router

# 2. Import các module nghiệp vụ


# 3. Khởi tạo App
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

# 4. Đăng ký hạ tầng (Giống như app.use(...) trong Express)
add_custom_middlewares(app)
register_exception_handlers(app)

# 5. Đăng ký các Router
app.include_router(health_router)

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}
