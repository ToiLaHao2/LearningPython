from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def add_custom_middlewares(app: FastAPI):
    # Cấu hình CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],    # Allow all origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
