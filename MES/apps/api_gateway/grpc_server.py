import asyncio
import grpc
from libs.core.contracts import mes_pb2_grpc
from libs.core.logger import logger
from .grpc_handler import PathfindingHandler, SlotAllocationHandler

async def serve_grpc():
    """Khởi chạy gRPC Server"""
    server = grpc.aio.server()
    
    # Đăng ký Handler của chúng ta vào Server
    mes_pb2_grpc.add_PathfindingServiceServicer_to_server(
        PathfindingHandler(), server
    )
    mes_pb2_grpc.add_SlotAllocationServiceServicer_to_server(
        SlotAllocationHandler(), server
    )

    # Lắng nghe ở port 50051 (Port mặc định của gRPC)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    
    logger.info(f"🚀 gRPC Server đang chạy tại: {listen_addr}")
    
    await server.start()
    await server.wait_for_termination()
