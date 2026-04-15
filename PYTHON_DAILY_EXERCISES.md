# Python Daily Exercises - Làm Vua Hàng Ngày

## Mô tiff
File này chúa các bài tap Python theo trend tu co ban nang cao, giúp ban luyen tap suy luan và giai quyêt vân dê thuc tê. Môi bài tap có gii y và lôi giai.

---

## Week 1: Python C Ban (Days 1-7)

### Day 1: Variables và Data Types

#### Bài tap 1.1: Machine Status Checker
**Mô tiff:** Viêt function kiêm tra trang thái máy theo công suât.
```python
def check_machine_status(power_usage):
    """
    Kiêm tra traang thái máy dda trên công suât tiêu thû:
    - < 50W: "Idle"
    - 50-200W: "Running" 
    - > 200W: "Overload"
    """
    # Code cûa ban o dây
    pass

# Test cases
print(check_machine_status(30))    # Expected: "Idle"
print(check_machine_status(150))   # Expected: "Running"
print(check_machine_status(250))   # Expected: "Overload"
```

**Gii y:**
- Sû dûng if-elif-else
- Nhu vân dê vê comparison operators

**Lôi giai:**
```python
def check_machine_status(power_usage):
    if power_usage < 50:
        return "Idle"
    elif power_usage <= 200:
        return "Running"
    else:
        return "Overload"
```

#### Bài tap 1.2: Temperature Converter
**Mô tiff:** Viêt function chuyên dôi nhiêt dô sang Fahrenheit.
```python
def celsius_to_fahrenheit(celsius):
    """
    Chuyên dôi Celsius sang Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    pass

# Test
print(celsius_to_fahrenheit(0))    # Expected: 32.0
print(celsius_to_fahrenheit(100))  # Expected: 212.0
```

---

### Day 2: Lists và Loops

#### Bài tap 2.1: Production Line Monitor
**Mô tiff:** Quân lý danh sách các máy trong dây chuyên sàn xuât.
```python
def get_active_machines(machines):
    """
    Lây danh sách các máy dang hoat dông (status = "running")
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

**Gii y:**
- Sû dung for loop
- Kiêm tra condition trong loop

#### Bài tap 2.2: Power Consumption Calculator
**Mô tiff:** Tính công suât tiêu thû tông.
```python
def calculate_total_power(machines):
    """
    Tính công suât tiêu thû cûa tât ca các máy
    """
    pass

print(calculate_total_power(machines))  # Expected: 330
```

---

### Day 3: Dictionaries và Functions

#### Bài tap 3.1: Machine Data Manager
**Mô tiff:** Quân lý thông tin máy bâng dictionary.
```python
def update_machine_status(machines, machine_name, new_status):
    """
    Câp nhât traang thái máy và trâ vê thông tin mõi
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

#### Bài tap 4.1: Production Code Generator
**Mô tiff:** Tao mã sàn xuât theo format.
```python
def generate_production_code(date, line, product):
    """
    Tao mã sàn xuât: PROD-DDMMYY-LINE-PRODUCT
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

#### Bài tap 5.1: Safe Division
**Mô tiff:** Xû lý chia sô an toàn.
```python
def safe_divide(a, b):
    """
    Chia an toàn, tra vê error message nêu chia cho 0
    """
    pass

print(safe_divide(10, 2))    # Expected: 5.0
print(safe_divide(10, 0))    # Expected: "Error: Cannot divide by zero"
```

---

### Day 6: File I/O

#### Bài tap 6.1: Log Manager
**Mô tiff:** Ghi log ra file.
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

#### Bài tap 7.1: Filter Machines
**Mô tiff:** Lây các máy có công suât > 100W.
```python
def get_high_power_machines(machines):
    """
    Sû dung list comprehension
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

#### Bài tap 8.1: Machine Class
**Mô tiff:** Tao class Machine.
```python
class Machine:
    def __init__(self, name, machine_type):
        # Khôi tao
        pass
    
    def start(self):
        # Bât máy
        pass
    
    def stop(self):
        # Tât máy
        pass
    
    def get_status(self):
        # Lây traang thái
        pass

# Test
machine = Machine("Machine A", "CNC")
machine.start()
print(machine.get_status())  # Expected: "running"
```

---

### Day 9: Inheritance

#### Bài tap 9.1: Specialized Machines
**Mô tiff:** Tao class chuyên biêt.
```python
class CNCMachine(Machine):
    def __init__(self, name, spindle_speed):
        # Khôi tao
        pass
    
    def set_spindle_speed(self, speed):
        # Dat tôc dô dao
        pass

# Test
cnc = CNCMachine("CNC-001", 1000)
cnc.start()
cnc.set_spindle_speed(1500)
print(cnc.get_status())  # Expected: "running at 1500 RPM"
```

---

### Day 10: Encapsulation

#### Bài tap 10.1: Private Data
**Mô tiff:** Bao vê dã liêu private.
```python
class ProductionLine:
    def __init__(self, name):
        self.__production_count = 0  # Private
        self.name = name
    
    def increment_production(self):
        # Tang sô luông sàn xuât
        pass
    
    def get_production_count(self):
        # Lây sô luông sàn xuât (read-only)
        pass

# Test
line = ProductionLine("Line A")
line.increment_production()
print(line.get_production_count())  # Expected: 1
```

---

### Day 11: Polymorphism

#### Bài tap 11.1: Different Machine Types
**Mô tiff:** Các máy khác nhau có hành vi khác nhau.
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

#### Bài tap 12.1: Performance Monitor
**Mô tiff:** Decorator dô performance.
```python
import time

def performance_monitor(func):
    def wrapper(*args, **kwargs):
        # Thôi gian bat dâu
        start = time.time()
        result = func(*args, **kwargs)
        # Thôi gian kêt thúc
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

#### Bài tap 13.1: Sensor Data Stream
**Mô tiff:** Generator cho sensor data.
```python
def sensor_data_generator(interval, count):
    """
    Generator mô phông sensor data
    """
    pass

# Test
for i, data in enumerate(sensor_data_generator(1, 5)):
    print(f"Reading {i+1}: {data}")
# Expected: Random sensor values
```

---

### Day 14: Exception Handling Advanced

#### Bài tap 14.1: Custom Exceptions
**Mô tiff:** Tao custom exception.
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

#### Bài tap 15.1: Simple Scheduler
**Mô tiff:** Lich trình sàn xuât.
```python
def create_schedule(orders, machines):
    """
    Phân công don dhang vào máy
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

#### Bài tap 16.1: Quality Checker
**Mô tiff:** Kiêm tra chât luông.
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

#### Bài tap 17.1: Stock Tracker
**Mô tiff:** Quân lý tôn kho.
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

#### Bài tap 18.1: Production Analytics
**Mô tiff:** Phân tích dã liêu sàn xuât.
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

#### Bài tap 19.1: Alert System
**Mô tiff:** Hê thông canh bâo.
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

#### Bài tap 20.1: Daily Report
**Mô tiff:** Tao bâo cáo hàng ngày.
```python
def generate_daily_report(date, production, quality, downtime):
    """
    Tao bâo cáo format HTML
    """
    pass

print(generate_daily_report("2026-04-15", 500, 95.5, 2.5))
# Expected: HTML report string
```

---

### Day 21: Integration Challenge

#### Bài tap 21.1: Mini MES System
**Mô tiff:** Tich hop tat ca concepts.
```python
class MiniMES:
    def __init__(self):
        # Khôi tao hê thông
        pass
    
    def add_machine(self, machine):
        # Thêm máy
        pass
    
    def start_production(self, product_id, quantity):
        # Bât dâu sàn xuât
        pass
    
    def get_status(self):
        # Lây traang thái hê thông
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

#### Bài tap 22.1: Data Serialization
```python
import json

def serialize_machine(machine_obj):
    """Chuyên object thành JSON"""
    pass

def deserialize_machine(json_str):
    """Chuyên JSON thành object"""
    pass

# Test
machine = {"name": "A", "status": "running", "power": 120}
json_str = serialize_machine(machine)
print(json_str)  # Expected: JSON string
```

---

### Day 23: HTTP Basics

#### Bài tap 23.1: API Request Simulator
```python
def simulate_api_request(endpoint, method, data=None):
    """Mô phông API request"""
    pass

print(simulate_api_request("/machines", "GET"))
print(simulate_api_request("/machines", "POST", {"name": "A"}))
```

---

### Day 24: Type Hints

#### Bài tap 24.1: Typed Functions
```python
from typing import List, Dict, Optional

def process_machines(machines: List[Dict[str, any]]) -> Optional[Dict[str, any]]:
    """Function vôi type hints"""
    pass
```

---

### Day 25: Async Basics

#### Bài tap 25.1: Async Operations
```python
import asyncio

async def fetch_sensor_data():
    """Mô phông async data fetch"""
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

#### Bài tap 26.1: Data Validation
```python
def validate_machine_data(data):
    """Validate machine data"""
    required_fields = ["name", "type", "status"]
    # Validation logic
    pass
```

---

### Day 27: Testing

#### Bài tap 27.1: Unit Tests
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

#### Bài tap 28.1: MES API Simulator
```python
class MESAPISimulator:
    def __init__(self):
        self.machines = {}
        self.production_orders = []
    
    def create_machine(self, machine_data):
        """Tao máy mõi"""
        pass
    
    def get_machine(self, machine_id):
        """Lây thông tin máy"""
        pass
    
    def create_production_order(self, order_data):
        """Tao don dhang sàn xuât"""
        pass
    
    def get_dashboard_data(self):
        """Lây dã liêu dashboard"""
        pass

# Test
api = MESAPISimulator()
api.create_machine({"id": "M001", "name": "Machine A", "type": "CNC"})
print(api.get_machine("M001"))
```

---

## Tips Hoc Tp

### 1. **Làm hàng ngày:**
- Dành 30-60 phút/ngày
- Không skip bài tap
- Ghi chú các concepts mõi

### 2. **Suy luân truoc khi code:**
- Dê bài yêu câ gi?
- Cân nhêu function?
- Edge cases nào?

### 3. **Test kip thoa:**
- Test vôi các cases khác nhau
- Kiêm tra error handling
- Verify output

### 4. **Refactor khi cân:**
- Code có clean không?
- Có thê optimize không?
- Có readable không?

### 5. **Build projects:**
- Áp dung concepts vào project thuc
- Tích hôn các bài tap
- Tao portfolio

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

**Lên lch:** 28 ngày mõi ngày 1 bài tap, build foundation solid cho FastAPI và MES development!
