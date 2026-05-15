import grpc
from libs.core.contracts import mes_pb2, mes_pb2_grpc
from libs.core.logger import logger
from libs.modules.pathfinding.service import PathfindingService
from libs.modules.slot_allocation.service import SlotAllocationService


class PathfindingHandler(mes_pb2_grpc.PathfindingServiceServicer):
    """
    Handler tiếp nhận các cuộc gọi gRPC từ WMS (Node.js).
    """
    def __init__(self):
        # Khởi tạo Service từ tầng libs
        self.path_service = PathfindingService()

    async def CalculatePath(self, request, context):
        """
        Hàm xử lý logic tìm đường khi Node.js gọi qua gRPC
        """
        warehouse_id = request.warehouse_id
        start_pos = (request.start.x, request.start.y)
        end_pos = (request.end.x, request.end.y)

        logger.info(f"gRPC Request: Tìm đường cho kho {warehouse_id} từ {start_pos} tới {end_pos}")

        try:
            # Gọi vào tầng libs để xử lý logic A*
            path = await self.path_service.get_path_for_warehouse(warehouse_id, start_pos, end_pos)

            if not path:
                return mes_pb2.PathResponse(success=False, message="Không tìm thấy đường đi")

            # Convert kết quả mảng tọa độ sang định dạng gRPC Point
            waypoints = [mes_pb2.Point(x=p[0], y=p[1]) for p in path]

            return mes_pb2.PathResponse(
                waypoints=waypoints,
                success=True,
                message="Tìm đường thành công"
            )
        except Exception as e:
            logger.error(f"Lỗi gRPC CalculatePath: {str(e)}")
            return mes_pb2.PathResponse(success=False, message=str(e))

class SlotAllocationHandler(mes_pb2_grpc.SlotAllocationServiceServicer):
    def __init__(self):
        self.slot_service = SlotAllocationService()

    async def AllocateSlot(self, request, context):
        """
        Hàm xử lý logic cấp phát vị trí khi được gọi qua gRPC
        """
        warehouse_id = request.warehouse_id
        item_id = request.item_id
        length = request.length
        width = request.width

        logger.info(f"gRPC Request: Cấp phát vị trí cho kho {warehouse_id} với kiện {item_id}")

        try:
            # Gọi vào tầng libs để xử lý logic Best Fit
            result = await self.slot_service.allocate_optimal_slot(warehouse_id, item_id, length, width)

            # result là AllocationResult object, trả thẳng các trường về gRPC
            return mes_pb2.SlotAllocationResponse(
                success=result.success,
                slot_id=result.slot_id or "",
                message=result.message,
                error_code=result.error_code or ""
            )
        except Exception as e:
            logger.error(f"Lỗi gRPC AllocateSlot: {str(e)}")
            return mes_pb2.SlotAllocationResponse(
                success=False,
                message=str(e),
                error_code="INTERNAL_ERROR"
            )