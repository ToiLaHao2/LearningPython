# pyrefly: ignore [missing-import]
from pydantic import BaseModel
from typing import Optional, Tuple

class ItemRequest(BaseModel):
    item_id: str
    length: float
    width: float

class SlotConfig(BaseModel):
    slot_id: str
    max_length: float
    max_width: float
    is_occupied: bool
    # Tọa độ (x, y) của slot trên bản đồ để sau này kết hợp với thuật toán tìm đường
    position: Tuple[int, int]

class AllocationResult(BaseModel):
    success: bool
    slot_id: Optional[str] = None
    message: str
    error_code: Optional[str] = None
