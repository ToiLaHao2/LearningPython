# Python Daily Exercises - Làm Vua Hàng Ngày

## Mô tả
File này chứa các bài tập Python theo trend từ cơ bản đến nâng cao, giúp bạn luyện tập suy luận và giải quyết vấn đề thực tế. Mỗi bài tập có gợi ý và lời giải.

---

## Week 1: Python Cơ Bản (Days 1-7)

### Day 1: Variables và Data Types

#### Bài tập 1.1: Machine Status Checker
**Mô tả:** Viết function kiểm tra trạng thái máy theo công suất.
```python
def check_machine_status(power_usage):
    """
    Kiểm tra trạng thái máy dựa trên công suất tiêu thụ:
    - < 50W: "Idle"
    - 50-200W: "Running" 
    - > 200W: "Overload"
    """
    # Code của bạn ở đây
    pass

# Test cases
print(check_machine_status(30))    # Expected: "Idle"
print(check_machine_status(150))   # Expected: "Running"
print(check_machine_status(250))   # Expected: "Overload"
```

**Gợi ý:**
- Sử dụng if-elif-else
- Nhớ vấn đề về comparison operators

**Lời giải:**
```python
def check_machine_status(power_usage):
    if power_usage < 50:
        return "Idle"
    elif power_usage <= 200:
        return "Running"
    else:
        return "Overload"
```

#### Bài tập 1.2: Temperature Converter
**Mô tả:** Viết function chuyển đổi nhiệt độ sang Fahrenheit.
```python
def celsius_to_fahrenheit(celsius):
    """
    Chuyển đổi Celsius sang Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    pass

# Test
print(celsius_to_fahrenheit(0))    # Expected: 32.0
print(celsius_to_fahrenheit(100))  # Expected: 212.0
```

---

### Day 2: Lists và Loops

#### Bài tập 2.1: Production Line Monitor
**Mô tả:** Quản lý danh sách các máy trong dây chuyền sản xuất.
```python
def get_active_machines(machines):
    """
    Lấy danh sách các máy đang hoạt động (status = "running")
    machines: list of {"name": str, "status": str, "power": int}
    """
    pass

machines = [
    {"name": "Machine A", "status": "running", "power": 120},
    {"name": "Machine B", "status": "idle", "power": 30},
    {"name": "Machine C", "status": "running", "power": 180}
]

print(get_active_machines(machines))
# Expected: ["Machine A", "Machine C"]
```

**Gợi ý:**
- Sử dụng for loop
- Kiểm tra condition trong loop

#### Bài tập 2.2: Power Consumption Calculator
**Mô tả:** Tính công suất tiêu thụ tổng.
```python
def calculate_total_power(machines):
    """
    Tính công suất tiêu thụ của tất cả các máy
    """
    pass

print(calculate_total_power(machines))  # Expected: 330
```

---

### Day 3: Dictionaries và Functions

#### Bài tập 3.1: Machine Data Manager
**Mô tả:** Quản lý thông tin máy bằng dictionary.
```python
def update_machine_status(machines, machine_name, new_status):
    """
    Cập nhật trạng thái máy và trả về thông tin mới
    """
    pass

machines = {
    "Machine A": {"status": "idle", "power": 30},
    "Machine B": {"status": "running", "power": 120}
}

result = update_machine_status(machines, "Machine A", "running")
print(result)
# Expected: {"status": "running", "power": 30, "updated": True}
```

---

### Day 4: String Manipulation

#### Bài tập 4.1: Production Code Generator
**Mô tả:** Tạo mã sản xuất theo format.
```python
def generate_production_code(date, line, product):
    """
    Tạo mã sản xuất: PROD-DDMMYY-LINE-PRODUCT
    date: "DD/MM/YYYY"
    line: "A", "B", "C"
    product: "TYPE1", "TYPE2"
    """
    pass

print(generate_production_code("15/04/2026", "A", "TYPE1"))
# Expected: "PROD-150426-A-TYPE1"
```

---

### Day 5: Error Handling

#### Bài tập 5.1: Safe Division
**Mô tả:** Xử lý chia số an toàn.
```python
def safe_divide(a, b):
    """
    Chia an toàn, trả về error message nếu chia cho 0
    """
    pass

print(safe_divide(10, 2))    # Expected: 5.0
print(safe_divide(10, 0))    # Expected: "Error: Cannot divide by zero"
```

---

### Day 6: File I/O

#### Bài tập 6.1: Log Manager
**Mô tả:** Ghi log ra file.
```python
def write_machine_log(machine_name, status, timestamp):
    """
    Ghi thông tin máy vào log file
    Format: "YYYY-MM-DD HH:MM:SS - Machine [NAME]: [STATUS]"
    """
    pass

# Test
write_machine_log("Machine A", "running", "2026-04-15 10:30:00")
# File content: "2026-04-15 10:30:00 - Machine [Machine A]: running"
```

---

### Day 7: List Comprehensions

#### Bài tập 7.1: Filter Machines
**Mô tả:** Lấy các máy có công suất > 100W.
```python
def get_high_power_machines(machines):
    """
    Sử dụng list comprehension
    """
    pass

machines = [
    {"name": "A", "power": 50},
    {"name": "B", "power": 150},
    {"name": "C", "power": 200}
]

print(get_high_power_machines(machines))
# Expected: [{"name": "B", "power": 150}, {"name": "C", "power": 200}]
```

---

## Week 2: OOP và Advanced Concepts (Days 8-14)

### Day 8: Classes và Objects

#### Bài tập 8.1: Machine Class
**Mô tả:** Tạo class Machine.
```python
class Machine:
    def __init__(self, name, machine_type):
        # Khởi tạo
        pass
    
    def start(self):
        # Bật máy
        pass
    
    def stop(self):
        # Tắt máy
        pass
    
    def get_status(self):
        # Lấy trạng thái
        pass

# Test
machine = Machine("Machine A", "CNC")
machine.start()
print(machine.get_status())  # Expected: "running"
```

---

### Day 9: Inheritance

#### Bài tập 9.1: Specialized Machines
**Mô tả:** Tạo class chuyên biệt.
```python
class CNCMachine(Machine):
    def __init__(self, name, spindle_speed):
        # Khởi tạo
        pass
    
    def set_spindle_speed(self, speed):
        # Đặt tốc độ dao
        pass

# Test
cnc = CNCMachine("CNC-001", 1000)
cnc.start()
cnc.set_spindle_speed(1500)
print(cnc.get_status())  # Expected: "running at 1500 RPM"
```

---

### Day 10: Encapsulation

#### Bài tập 10.1: Private Data
**Mô tả:** Bảo vệ dữ liệu private.
```python
class ProductionLine:
    def __init__(self, name):
        self.__production_count = 0  # Private
        self.name = name
    
    def increment_production(self):
        # Tăng số lượng sản xuất
        pass
    
    def get_production_count(self):
        # Lấy số lượng sản xuất (read-only)
        pass

# Test
line = ProductionLine("Line A")
line.increment_production()
print(line.get_production_count())  # Expected: 1
```

---

### Day 11: Polymorphism

#### Bài tập 11.1: Different Machine Types
**Mô tả:** Các máy khác nhau có hành vi khác nhau.
```python
class Machine:
    def get_info(self):
        pass

class Pump(Machine):
    def get_info(self):
        return "Pump - Flow rate: 100 L/min"

class Conveyor(Machine):
    def get_info(self):
        return "Conveyor - Speed: 2 m/s"

def print_machine_info(machine):
    print(machine.get_info())

# Test
pump = Pump()
conveyor = Conveyor()
print_machine_info(pump)       # Expected: "Pump - Flow rate: 100 L/min"
print_machine_info(conveyor)   # Expected: "Conveyor - Speed: 2 m/s"
```

---

### Day 12: Decorators

#### Bài tập 12.1: Performance Monitor
**Mô tả:** Decorator đo performance.
```python
import time

def performance_monitor(func):
    def wrapper(*args, **kwargs):
        # Thời gian bắt đầu
        start = time.time()
        result = func(*args, **kwargs)
        # Thời gian kết thúc
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@performance_monitor
def process_data(data):
    time.sleep(0.1)  # Simulate work
    return len(data)

# Test
print(process_data([1, 2, 3, 4, 5]))  # Expected: 5 + time message
```

---

### Day 13: Generators

#### Bài tập 13.1: Sensor Data Stream
**Mô tả:** Generator cho sensor data.
```python
def sensor_data_generator(interval, count):
    """
    Generator mô phỏng sensor data
    """
    pass

# Test
for i, data in enumerate(sensor_data_generator(1, 5)):
    print(f"Reading {i+1}: {data}")
# Expected: Random sensor values
```

---

### Day 14: Exception Handling Advanced

#### Bài tập 14.1: Custom Exceptions
**Mô tả:** Tạo custom exception.
```python
class MachineError(Exception):
    pass

class MachineOverloadError(MachineError):
    pass

def check_machine_load(power, max_power):
    if power > max_power:
        raise MachineOverloadError(f"Power {power} exceeds max {max_power}")
    return "OK"

# Test
try:
    print(check_machine_load(250, 200))
except MachineOverloadError as e:
    print(f"Error: {e}")  # Expected: Error message
```

---

## Week 3: MES-Specific Applications (Days 15-21)

### Day 15: Production Scheduling

#### Bài tập 15.1: Simple Scheduler
**Mô tả:** Lịch trình sản xuất.
```python
def create_schedule(orders, machines):
    """
    Phân công đơn hàng vào máy
    orders: [{"id": 1, "time": 2, "priority": 1}]
    machines: ["A", "B", "C"]
    """
    pass

orders = [
    {"id": 1, "time": 2, "priority": 1},
    {"id": 2, "time": 1, "priority": 3},
    {"id": 3, "time": 3, "priority": 2}
]

print(create_schedule(orders, ["A", "B"]))
# Expected: Schedule assignment
```

---

### Day 16: Quality Control

#### Bài tập 16.1: Quality Checker
**Mô tả:** Kiểm tra chất lượng.
```python
def check_quality(measurements, specs):
    """
    measurements: [10.1, 9.9, 10.2]
    specs: {"min": 9.5, "max": 10.5}
    """
    pass

print(check_quality([10.1, 9.9, 10.2], {"min": 9.5, "max": 10.5}))
# Expected: {"passed": True, "avg": 10.07}
```

---

### Day 17: Inventory Management

#### Bài tập 17.1: Stock Tracker
**Mô tả:** Quản lý tồn kho.
```python
def update_inventory(inventory, transactions):
    """
    inventory: {"item1": 100, "item2": 50}
    transactions: [{"item": "item1", "qty": -10}, {"item": "item2", "qty": 5}]
    """
    pass

print(update_inventory({"A": 100, "B": 50}, [{"item": "A", "qty": -10}]))
# Expected: {"A": 90, "B": 50}
```

---

### Day 18: Data Analysis

#### Bài tập 18.1: Production Analytics
**Mô tả:** Phân tích dữ liệu sản xuất.
```python
def analyze_production(production_data):
    """
    production_data: [{"date": "2026-04-15", "units": 100}, ...]
    """
    pass

data = [
    {"date": "2026-04-15", "units": 100},
    {"date": "2026-04-16", "units": 120},
    {"date": "2026-04-17", "units": 90}
]

print(analyze_production(data))
# Expected: {"total": 310, "avg": 103.33, "max": 120}
```

---

### Day 19: Real-time Monitoring

#### Bài tập 19.1: Alert System
**Mô tả:** Hệ thống cảnh báo.
```python
def check_alerts(sensor_data, thresholds):
    """
    sensor_data: {"temperature": 85, "pressure": 150}
    thresholds: {"temperature": 80, "pressure": 200}
    """
    pass

print(check_alerts({"temperature": 85, "pressure": 150}, 
                   {"temperature": 80, "pressure": 200}))
# Expected: ["Temperature alert: 85°C (threshold: 80°C)"]
```

---

### Day 20: Report Generation

#### Bài tập 20.1: Daily Report
**Mô tả:** Tạo báo cáo hàng ngày.
```python
def generate_daily_report(date, production, quality, downtime):
    """
    Tạo báo cáo format HTML
    """
    pass

print(generate_daily_report("2026-04-15", 500, 95.5, 2.5))
# Expected: HTML report string
```

---

### Day 21: Integration Challenge

#### Bài tập 21.1: Mini MES System
**Mô tả:** Tích hợp tất cả concepts.
```python
class MiniMES:
    def __init__(self):
        # Khởi tạo hệ thống
        pass
    
    def add_machine(self, machine):
        # Thêm máy
        pass
    
    def start_production(self, product_id, quantity):
        # Bắt đầu sản xuất
        pass
    
    def get_status(self):
        # Lấy trạng thái hệ thống
        pass

# Test
mes = MiniMES()
mes.add_machine("Machine A")
mes.start_production("PROD-001", 100)
print(mes.get_status())
# Expected: System status summary
```

---

## Week 4: FastAPI Preparation (Days 22-28)

### Day 22: JSON Handling

#### Bài tập 22.1: Data Serialization
```python
import json

def serialize_machine(machine_obj):
    """Chuyển object thành JSON"""
    pass

def deserialize_machine(json_str):
    """Chuyển JSON thành object"""
    pass

# Test
machine = {"name": "A", "status": "running", "power": 120}
json_str = serialize_machine(machine)
print(json_str)  # Expected: JSON string
```

---

### Day 23: HTTP Basics

#### Bài tập 23.1: API Request Simulator
```python
def simulate_api_request(endpoint, method, data=None):
    """Mô phỏng API request"""
    pass

print(simulate_api_request("/machines", "GET"))
print(simulate_api_request("/machines", "POST", {"name": "A"}))
```

---

### Day 24: Type Hints

#### Bài tập 24.1: Typed Functions
```python
from typing import List, Dict, Optional

def process_machines(machines: List[Dict[str, any]]) -> Optional[Dict[str, any]]:
    """Function vôi type hints"""
    pass
```

---

### Day 25: Async Basics

#### Bài tập 25.1: Async Operations
```python
import asyncio

async def fetch_sensor_data():
    """Mô phỏng async data fetch"""
    await asyncio.sleep(0.1)
    return {"temperature": 25.5}

async def main():
    data = await fetch_sensor_data()
    print(data)

# Test
asyncio.run(main())
```

---

### Day 26: Validation

#### Bài tập 26.1: Data Validation
```python
def validate_machine_data(data):
    """Validate machine data"""
    required_fields = ["name", "type", "status"]
    # Validation logic
    pass
```

---

### Day 27: Testing

#### Bài tập 27.1: Unit Tests
```python
def test_machine_status():
    """Unit test cho machine status"""
    assert check_machine_status(30) == "Idle"
    assert check_machine_status(150) == "Running"
    assert check_machine_status(250) == "Overload"

# Run test
test_machine_status()
print("All tests passed!")
```

---

### Day 28: Final Challenge

#### Bài tập 28.1: MES API Simulator
```python
class MESAPISimulator:
    def __init__(self):
        self.machines = {}
        self.production_orders = []
    
    def create_machine(self, machine_data):
        """Tạo máy mới"""
        pass
    
    def get_machine(self, machine_id):
        """Lấy thông tin máy"""
        pass
    
    def create_production_order(self, order_data):
        """Tạo đơn hàng sản xuất"""
        pass
    
    def get_dashboard_data(self):
        """Lấy dữ liệu dashboard"""
        pass

# Test
api = MESAPISimulator()
api.create_machine({"id": "M001", "name": "Machine A", "type": "CNC"})
print(api.get_machine("M001"))
```

---

## Tips Học Tập

### 1. **Làm hàng ngày:**
- Dành 30-60 phút/ngày
- Không skip bài tập
- Ghi chú các concepts mới

### 2. **Suy luận trước khi code:**
- Đề bài yêu cầu gì?
- Cần những function nào?
- Edge cases nào?

### 3. **Test kịp thời:**
- Test với các cases khác nhau
- Kiểm tra error handling
- Verify output

### 4. **Refactor khi cần:**
- Code có clean không?
- Có thể optimize không?
- Có readable không?

### 5. **Build projects:**
- Áp dụng concepts vào project thực
- Tích hợp các bài tập
- Tạo portfolio

---

## Resources Tham Khao

### Documentation:
- [Python Official Docs](https://docs.python.org/3/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)

### Practice Platforms:
- [LeetCode](https://leetcode.com/)
- [HackerRank](https://www.hackerrank.com/)
- [Codewars](https://www.codewars.com/)

### Books:
- "Python Crash Course" - Eric Matthes
- "Effective Python" - Brett Slatkin
- "Fluent Python" - Luciano Ramalho

---

**Lên lịch:** 28 ngày mỗi ngày 1 bài tập, build foundation solid cho FastAPI và MES development!
