from typing import List
from .models import ItemRequest, SlotConfig
from .exceptions import ItemTooLargeError, NoAvailableSlotError

class BestFitAllocator:
    """
    Thuật toán "Best Fit": Tìm slot vừa vặn nhất với món hàng để tiết kiệm tối đa không gian trống.
    Có hỗ trợ xoay hàng 90 độ.
    """
    def allocate(self, item: ItemRequest, all_slots: List[SlotConfig]) -> SlotConfig:
        valid_slots = []
        max_slot_length_in_warehouse = 0
        max_slot_width_in_warehouse = 0

        # 1. Duyệt qua tất cả các slot để tìm slot hợp lệ và lấy thông số lớn nhất của kho
        for slot in all_slots:
            # Lưu lại kích thước lớn nhất của kho để check hàng quá khổ
            max_slot_length_in_warehouse = max(max_slot_length_in_warehouse, slot.max_length)
            max_slot_width_in_warehouse = max(max_slot_width_in_warehouse, slot.max_width)

            if not slot.is_occupied:
                # Kiểm tra đặt thẳng
                fits_straight = (item.length <= slot.max_length and item.width <= slot.max_width)
                # Kiểm tra xoay 90 độ
                fits_rotated = (item.width <= slot.max_length and item.length <= slot.max_width)
                
                if fits_straight or fits_rotated:
                    valid_slots.append(slot)

        # TRƯỜNG HỢP 1: Hàng quá khổ (Ngay cả slot to nhất kho cũng không chứa nổi)
        item_max_dim = max(item.length, item.width)
        item_min_dim = min(item.length, item.width)
        wh_max_dim = max(max_slot_length_in_warehouse, max_slot_width_in_warehouse)
        wh_min_dim = min(max_slot_length_in_warehouse, max_slot_width_in_warehouse)
        
        if item_max_dim > wh_max_dim or item_min_dim > wh_min_dim:
            raise ItemTooLargeError()

        # TRƯỜNG HỢP 2: Hết chỗ (Hàng không quá khổ, nhưng các slot vừa vặn đều đã bị occupied)
        if not valid_slots:
            raise NoAvailableSlotError()

        # TRƯỜNG HỢP 3: Tìm được slot. Áp dụng Best Fit logic.
        # Tính toán "diện tích dư thừa". Slot nào dư thừa ít nhất sẽ được ưu tiên.
        valid_slots.sort(key=lambda s: (s.max_length * s.max_width) - (item.length * item.width))

        # Trả về slot tối ưu nhất (cái đầu tiên sau khi sort)
        return valid_slots[0]
