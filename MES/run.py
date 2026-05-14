# pyrefly: ignore [missing-import]
import uvicorn
import os
import sys

# Thêm thư mục hiện tại vào PYTHONPATH để Python tìm thấy libs
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("--- Khởi động Warehouse Management Simulation MES (Python) ---")
    uvicorn.run(
        "apps.api_gateway.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )
