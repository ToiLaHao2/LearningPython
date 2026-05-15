class SlotAllocationError(Exception):
    """Base exception cho module slot allocation"""
    pass

class ItemTooLargeError(SlotAllocationError):
    def __init__(self, message="Hàng quá khổ, vượt quá kích thước tối đa của thiết kế kệ trong kho."):
        super().__init__(message)

class NoAvailableSlotError(SlotAllocationError):
    def __init__(self, message="Không tìm thấy slot nào trống và phù hợp kích thước ở thời điểm hiện tại."):
        super().__init__(message)
