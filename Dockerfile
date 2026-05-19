# ============================================================
# WMSS MES Service (Python / FastAPI)
# ============================================================

FROM python:3.11-slim

WORKDIR /app

# Cài dependencies trước (tận dụng Docker cache)
COPY MES/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code MES
COPY MES/ ./

# Expose port cho FastAPI (HTTP) và gRPC
EXPOSE 8000 50051

# Chạy FastAPI qua uvicorn (không reload trong production)
CMD ["python", "run.py"]
