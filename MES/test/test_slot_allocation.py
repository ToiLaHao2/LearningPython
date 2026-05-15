"""
Test thuật toán Slot Allocation (Best Fit).
Chạy lệnh: python -m test.test_slot_allocation
(Chạy từ thư mục MES)
"""

from libs.modules.slot_allocation.algorithm import BestFitAllocator
from libs.modules.slot_allocation.models import ItemRequest, SlotConfig
from libs.modules.slot_allocation.exceptions import ItemTooLargeError, NoAvailableSlotError

# Khởi tạo thuật toán
allocator = BestFitAllocator()

# ============================================================
# DỮ LIỆU GIẢ (Fake Data) — Thay thế cho việc lấy từ Redis
# ============================================================
# Giả sử kho có 4 slot với kích thước khác nhau:
fake_slots = [
    SlotConfig(slot_id="SLOT-A1", max_length=3.0, max_width=3.0, is_occupied=False, position=(1, 1)),
    SlotConfig(slot_id="SLOT-A2", max_length=5.0, max_width=5.0, is_occupied=False, position=(2, 1)),
    SlotConfig(slot_id="SLOT-B1", max_length=10.0, max_width=10.0, is_occupied=False, position=(1, 3)),
    SlotConfig(slot_id="SLOT-B2", max_length=4.0, max_width=3.0, is_occupied=True, position=(2, 3)),  # Đã bị chiếm
]


def test_case_1_item_too_large():
    """TEST 1: Hàng quá khổ — To hơn cả slot lớn nhất trong kho"""
    print("\n" + "=" * 60)
    print("TEST 1: Hàng quá khổ (15x15 vào kho max 10x10)")
    print("=" * 60)

    item = ItemRequest(item_id="ITEM-XXL", length=15.0, width=15.0)

    try:
        result = allocator.allocate(item, fake_slots)
        # Nếu chạy tới đây = FAIL (lẽ ra phải bắn lỗi)
        print("❌ FAIL — Không bắn lỗi ItemTooLargeError!")
    except ItemTooLargeError as e:
        # Đúng! Phải vào đây
        print(f"✅ PASS — Bắt được lỗi: {e}")
    except Exception as e:
        print(f"❌ FAIL — Lỗi không mong đợi: {e}")


def test_case_2_no_available_slot():
    """TEST 2: Hết chỗ — Hàng không quá khổ nhưng tất cả slot vừa đều bị chiếm"""
    print("\n" + "=" * 60)
    print("TEST 2: Hết chỗ (tất cả slot đều occupied)")
    print("=" * 60)

    # Tạo danh sách slot mà TẤT CẢ đều bị chiếm
    all_occupied_slots = [
        SlotConfig(slot_id="SLOT-A1", max_length=3.0, max_width=3.0, is_occupied=True, position=(1, 1)),
        SlotConfig(slot_id="SLOT-A2", max_length=5.0, max_width=5.0, is_occupied=True, position=(2, 1)),
    ]

    item = ItemRequest(item_id="ITEM-S", length=2.0, width=2.0)

    try:
        result = allocator.allocate(item, all_occupied_slots)
        print("❌ FAIL — Không bắn lỗi NoAvailableSlotError!")
    except NoAvailableSlotError as e:
        print(f"✅ PASS — Bắt được lỗi: {e}")
    except Exception as e:
        print(f"❌ FAIL — Lỗi không mong đợi: {e}")


def test_case_3_best_fit_found():
    """TEST 3: Tìm được slot tối ưu — Chọn slot vừa vặn nhất"""
    print("\n" + "=" * 60)
    print("TEST 3: Tìm slot tối ưu (item 2x2 → kỳ vọng chọn SLOT-A1 3x3)")
    print("=" * 60)

    item = ItemRequest(item_id="ITEM-M", length=2.0, width=2.0)

    try:
        result = allocator.allocate(item, fake_slots)
        print(f"📦 Slot được chọn: {result.slot_id}")
        print(f"📐 Kích thước slot: {result.max_length} x {result.max_width}")
        print(f"📍 Vị trí trên bản đồ: {result.position}")

        # Kiểm tra kết quả
        if result.slot_id == "SLOT-A1":
            print("✅ PASS — Đúng! Chọn slot 3x3 (vừa vặn nhất cho item 2x2)")
        else:
            print(f"⚠️ WARN — Chọn {result.slot_id} thay vì SLOT-A1. Kiểm tra lại logic.")
    except Exception as e:
        print(f"❌ FAIL — Lỗi: {e}")


def test_case_4_rotation():
    """TEST 4: Xoay 90 độ — Item 4x2 không vừa thẳng vào slot 3x4, nhưng xoay lại thì vừa"""
    print("\n" + "=" * 60)
    print("TEST 4: Xoay 90 độ (item 4x2 vào slot 3x4 → xoay thành 2x4)")
    print("=" * 60)

    rotation_slots = [
        # Slot này: max_length=3, max_width=4
        # Item thẳng: length=4 > max_length=3 → KHÔNG VỪA
        # Item xoay:  width=2 <= max_length=3, length=4 <= max_width=4 → VỪA!
        SlotConfig(slot_id="SLOT-R1", max_length=3.0, max_width=4.0, is_occupied=False, position=(5, 5)),
    ]

    item = ItemRequest(item_id="ITEM-R", length=4.0, width=2.0)

    try:
        result = allocator.allocate(item, rotation_slots)
        print(f"📦 Slot được chọn: {result.slot_id}")

        if result.slot_id == "SLOT-R1":
            print("✅ PASS — Đúng! Thuật toán biết xoay hàng 90 độ để nhét vào slot")
        else:
            print(f"❌ FAIL — Chọn sai slot: {result.slot_id}")
    except ItemTooLargeError:
        print("❌ FAIL — Báo quá khổ sai! Xoay 90 độ thì vừa mà.")
    except Exception as e:
        print(f"❌ FAIL — Lỗi: {e}")


# ============================================================
# CHẠY TẤT CẢ CÁC TEST
# ============================================================
if __name__ == "__main__":
    print("\n🧪 BẮT ĐẦU TEST MODULE SLOT ALLOCATION")
    print("=" * 60)

    test_case_1_item_too_large()
    test_case_2_no_available_slot()
    test_case_3_best_fit_found()
    test_case_4_rotation()

    print("\n" + "=" * 60)
    print("🏁 HOÀN TẤT TẤT CẢ CÁC TEST")
    print("=" * 60)
