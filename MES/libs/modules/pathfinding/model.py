from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    x: int
    y: int
    g: float = 0 # Chi phí từ điểm bắt đầu đến node hiện tại
    h: float = 0 # Chi phí ước tính từ node hiện tại đến đích (Heuristic)
    f: float = 0 # f = g + h
    parent: Optional['Node'] = None

    def __lt__(self, other):
        # Hổ trợ Priority Queue so sánh dựa trên giá trị f
        return self.f < other.f

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Dùng tọa độ làm hash để kiểm tra trong Set cực nhanh
        return hash((self.x, self.y))