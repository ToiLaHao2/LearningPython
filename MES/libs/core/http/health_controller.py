from sys import prefix
import time
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter(prefix="/health", tags=["System"])

@router.get("/")
async def get_health():
    return {
        "status": "healty",
        "uptime": time.time(),
        "services": {
            "database": "connected",
            "redis": "connected",
            "storage": "configured"
        }
    }