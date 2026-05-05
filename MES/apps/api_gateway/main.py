from fastapi import FastAPI

# Absolute import từ libs
from libs.core.config import settings
from libs.modules.users.router import router as users_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

# Đăng ký các router (giống như app.use trong Node.js)
app.include_router(users_router, prefix=f"{settings.API_PREFIX}/users", tags=["Users"])

@app.get("/", tags=["Health"])
def root():
    return {"message": "Welcome to Warehouse Management API"}
