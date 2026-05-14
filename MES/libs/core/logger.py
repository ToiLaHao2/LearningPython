import logging
import sys
from libs.core.config import settings

def setup_logger(name: str = "WMSS_MES") -> logging.Logger:
    """Thiết lập logger chuẩn cho toàn bộ dự án MES"""
    
    logger = logging.getLogger(name)
    
    # Nếu logger đã được cấu hình thì không cấu hình lại (tránh log bị in đúp)
    if logger.handlers:
        return logger

    # Mức độ log: Nếu DEBUG=True trong .env thì in cả thông tin chi tiết
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO
    logger.setLevel(log_level)

    # Định dạng chuỗi log: [Thời gian] [Mức độ] - File:Dòng - Tin nhắn
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # In log ra màn hình console (Terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)

    return logger

# Tạo sẵn một instance logger chung để các file khác import dùng luôn
logger = setup_logger()
