from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

# Hàm này sẽ bắt các lỗi không lường trước được (lỗi 500)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "Đã có lỗi hệ thống xảy ra. Vui lòng thử lại sau.",
            "detail": str(exc) 
        },
    )

# Hàm đăng ký các handler vào FastAPI app
def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(Exception, global_exception_handler)
    
