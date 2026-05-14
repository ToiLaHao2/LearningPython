from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # --- Config Server ---
    PROJECT_NAME: str = "FastAPI MES"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # --- Database Config ---
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/mes_db"

    # --- Redis Config (Đồng bộ với Node.js) ---
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""
    REDIS_TLS: bool = False

    @computed_field
    @property
    def REDIS_URL(self) -> str:
        """Tự động xây dựng URL từ các thành phần lẻ"""
        protocol = "rediss" if self.REDIS_TLS else "redis"
        auth = f":{self.REDIS_PASSWORD}@" if self.REDIS_PASSWORD else ""
        return f"{protocol}://{auth}{self.REDIS_HOST}:{self.REDIS_PORT}/0"

    # --- gRPC Config ---
    GRPC_PORT: int = 50051

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
