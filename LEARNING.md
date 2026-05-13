# Lộ trình học Python từ Cơ bản đến Nâng cao

Chào mừng bạn đến với hướng dẫn học Python! Dưới đây là tổng hợp các kiến thức từ mức độ cơ bản cho đến nâng cao trong Python, kèm theo ví dụ minh hoạ để bạn dễ dàng nắm bắt.

---

## Phần 1: Python Cơ bản (Basic Python)

### 1. Cú pháp cơ bản và "Hello World"
Python là ngôn ngữ thông dịch, cú pháp của Python chú trọng vào sự tối giản và dễ đọc (sử dụng khoảng trắng/thụt lề thay vì dấu ngoặc nhọn `{}`).
```python
# In ra màn hình
print("Hello, World!")
```

### 2. Biến và Kiểu dữ liệu (Variables & Data Types)
Các kiểu dữ liệu cơ bản: `int` (số nguyên), `float` (số thực), `str` (chuỗi), `bool` (boolean: True/False).
```python
x = 10          # int
y = 3.14        # float
name = "Alice"  # str
is_active = True # bool

print(type(x))  # <class 'int'>
```

### 3. Cấu trúc điều kiện (If-Else)
```python
age = 18
if age >= 18:
    print("Bạn đã trưởng thành.")
elif age >= 12:
    print("Bạn là thanh thiếu niên.")
else:
    print("Bạn là trẻ em.")
```

### 4. Vòng lặp (Loops)
**Vòng lặp For:** Thường dùng để duyệt qua các phần tử của một danh sách hoặc dải số.
```python
for i in range(5): # Chạy từ 0 đến 4
    print(i)
```

**Vòng lặp While:** Lặp đến khi điều kiện sai.
```python
count = 0
while count < 3:
    print(count)
    count += 1
```

### 5. Hàm (Functions)
```python
def greet(name):
    return f"Xin chào, {name}!"

print(greet("Bob"))
```

---

## Phần 2: Cấu trúc Dữ liệu Cốt lõi (Data Structures)

### 1. List (Danh sách)
List là tập hợp các phần tử có thứ tự, có thể thay đổi (mutable).
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")    # Thêm phần tử
print(fruits[0])           # Truy cập phần tử đầu tiên
```

### 2. Tuple
Giống List nhưng **không thể thay đổi (immutable)**.
```python
coordinates = (10.0, 20.0)
# coordinates[0] = 15.0  # Lỗi! Tuple không cho phép thay đổi
```

### 3. Set (Tập hợp)
Tập hợp các phần tử không có thứ tự và **không trùng lặp**.
```python
unique_numbers = {1, 2, 2, 3, 3}
print(unique_numbers)  # Output: {1, 2, 3}
```

### 4. Dictionary (Từ điển)
Lưu trữ dữ liệu dưới dạng cặp `Key: Value`.
```python
person = {
    "name": "Alice",
    "age": 25
}
print(person["name"])  # Output: Alice
person["job"] = "Engineer" # Thêm thuộc tính
```

---

## Phần 3: Lập trình Hướng đối tượng (OOP)

OOP giúp tổ chức code mạnh mẽ hơn. Các khái niệm cốt lõi: Class (Lớp), Object (Đối tượng), Inheritance (Kế thừa), Encapsulation (Đóng gói), Polymorphism (Đa hình).

```python
# Định nghĩa lớp cơ sở (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass # Phương thức trống, chờ lớp con ghi đè

# Kế thừa (Inheritance)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy says Woof!
```

---

## Phần 4: Python Nâng cao (Advanced Python)

### 1. List Comprehension
Cách viết ngắn gọn để tạo ra list.
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers if x % 2 == 0] 
print(squares) # Output: [4, 16]
```

### 2. Exception Handling (Xử lý ngoại lệ)
Dùng `try-except` để tránh việc chương trình bị đóng đột ngột khi gặp lỗi.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0.")
finally:
    print("Khối lệnh này luôn được thực thi.")
```

### 3. Đọc / Ghi File
```python
# Ghi file
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào từ Python!")

# Đọc file
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

### 4. Generators và Yield
Rất hữu ích khi làm việc với lượng lớn dữ liệu để tiết kiệm bộ nhớ (Memory efficient). Nó không lưu toàn bộ dữ liệu vào RAM mà sinh ra từng bước.
```python
def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)  # 0, 1, 1, 2, 3
```

### 5. Decorators
Dùng để sửa đổi hành vi của một hàm mà không cần thay đổi code bên trong nó. Thường dùng cho logging, authentication, tính thời gian chạy,...
```python
def my_decorator(func):
    def wrapper():
        print("Đang chuẩn bị gọi hàm...")
        func()
        print("Gọi hàm xong.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Đang chuẩn bị gọi hàm...
# Hello!
# Gọi hàm xong.
```

### 6. Thư viện chuẩn và Modules (Modules & Packages)
Bạn có thể tự chia code thành nhiều file (.py) để dễ quản lý. Python cũng cung cấp sẵn nhiều thư viện mạnh mẽ như:
- `math`: Các hàm toán học.
- `datetime`: Quản lý thời gian, ngày tháng.
- `os`, `sys`: Tương tác với hệ điều hành.
- `json`: Xử lý dữ liệu dạng JSON.

### 7. Multi-threading & Multi-processing
- **Threading (Đa luồng):** Tốt cho các tác vụ I/O bound (Call API, truy vấn Database). (Lưu ý GIL trong Python làm hạn chế sức mạnh đa luồng với tác vụ tính toán).
- **Multiprocessing (Đa tiến trình):** Tốt cho các tác vụ CPU bound (Tính toán toán học nặng).

---

## Phần 5: Web Frameworks cho Hệ thống MES

Để phát triển hệ thống MES (Manufacturing Execution System), bạn cần chọn framework phù hợp. MES là hệ thống phức tạp đòi hỏi:
- Xử lý real-time data từ các thiết bị sản xuất
- Quản lý quy trình sản xuất phức tạp
- Tích hợp với nhiều hệ thống khác (ERP, SCADA)
- Bảo mật và độ tin cậy cao
- Performance tốt cho concurrent requests

### 1. FastAPI - Framework Hiện đại cho High-Performance APIs

**Ưu điểm cho MES:**
- **Performance cực cao**: Tốc độ xử lý nhanh nhờ Pydantic và ASGI, phù hợp cho real-time data processing
- **Auto-documentation**: Tự động生成 Swagger/OpenAPI docs, rất hữu ích cho integration teams
- **Type hints**: Strong typing giúp giảm bugs trong hệ thống MES phức tạp
- **Async support**: Hỗ trợ async/await cho concurrent operations
- **WebSocket support**: Cực kỳ quan trọng cho real-time monitoring và data streaming

**Nhược điểm:**
- Cần kiến thức async programming
- Community nhỏ hơn Django
- Less built-in features

**Ví dụ cho MES:**
```python
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from typing import List
import asyncio

app = FastAPI(title="MES System API")

class ProductionData(BaseModel):
    machine_id: str
    temperature: float
    pressure: float
    timestamp: str

@app.post("/api/production-data")
async def receive_production_data(data: ProductionData):
    # Xử lý real-time production data
    await process_mqtt_data(data)
    return {"status": "received"}

@app.websocket("/ws/monitoring")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Stream real-time production data
        data = await get_real_time_data()
        await websocket.send_json(data)
        await asyncio.sleep(1)
```

### 2. Django - Framework Enterprise cho Large-scale Systems

**Ưu điểm cho MES:**
- **Batteries-included**: ORM, Admin panel, Authentication, Security - tất cả built-in
- **Admin panel**: Cực kỳ mạnh mẽ cho managing production data, users, configurations
- **Maturity & Stability**: Đã được test trong nhiều enterprise systems
- **Security**: Built-in protection cho common vulnerabilities
- **Ecosystem**: Rất nhiều packages sẵn có cho enterprise needs

**Nhược điểm:**
- Performance chậm hơn FastAPI
- Learning curve cao hơn
- Less flexible cho custom APIs
- Heavy weight cho simple applications

**Ví dụ cho MES:**
```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class ProductionLine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

class Machine(models.Model):
    line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    machine_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=[
        ('running', 'Running'),
        ('idle', 'Idle'),
        ('maintenance', 'Maintenance')
    ])

# admin.py
from django.contrib import admin
from .models import ProductionLine, Machine

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ['machine_id', 'line', 'status', 'last_maintenance']
    list_filter = ['status', 'line']
    search_fields = ['machine_id']
```

### 3. Flask - Framework Lightweight cho Custom Solutions

**Ưu điểm cho MES:**
- **Flexibility**: Minimal core, cho phép custom everything
- **Easy to learn**: Simple và intuitive
- **Good for microservices**: Perfect cho distributed MES architecture
- **Lightweight**: Fast startup time, low memory footprint

**Nhược điểm:**
- Cần tự build nhiều features
- Less structured cho large teams
- More decisions cần làm

### 4. Các Framework khác phù hợp cho MES

#### a) Sanic
- Async framework tương tự FastAPI
- Performance rất cao
- Good cho high-concurrency applications

#### b) AIOHTTP
- Pure async framework
- Good cho complex async operations
- Flexible nhưng cần nhiều boilerplate

#### c) Tornado
- Mature async framework
- Good cho real-time applications
- Built-in WebSocket support

### 5. Bảng So sánh Frameworks cho MES

| Tiêu chí | FastAPI | Django | Flask | Sanic |
|---------|---------|---------|-------|-------|
| **Performance** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Learning Curve** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Built-in Features** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐ |
| **Real-time Support** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Enterprise Ready** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Community & Ecosystem** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Security Features** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

### 6. Recommendation cho MES Development

**Nếu bạn mới bắt đầu với Python:**
- Bắt đầu với **Django** để học structured development và có built-in features
- Admin panel cực kỳ hữu ích cho managing MES data

**Nếu bạn cần performance cao và real-time features:**
- Chọn **FastAPI** cho modern, high-performance APIs
- Perfect cho IoT integration và real-time monitoring

**Nếu bạn cần flexibility và microservices:**
- **Flask** cho custom solutions
- **Sanic** cho high-performance async operations

**Kết hợp approach:**
- Django cho core management system
- FastAPI cho real-time data processing APIs
- Flask cho small utility services

### 7. Kiên trúc FastAPI cho MES (Production-Ready)

#### a) Modular Monolith Architecture (Recommended)

**Kiên trúc này duccj proven trong production và optimal cho MES:**

```
mes_system/
main.py                 # Entry point
apps/
  api-gateway/
    main.py             # FastAPI REST API server
    Dockerfile
  socket/
    main.py             # WebSocket server (Socket.io style)
    Dockerfile
  worker/
    main.py             # Background jobs (Celery style)
    Dockerfile

libs/
  core/
    __init__.py
    config.py           # Settings (Pydantic BaseSettings)
    database.py         # SQLAlchemy setup + migrations
    security.py         # JWT authentication + OAuth2
    container.py        # Dependency Injection setup
    cache.py            # Redis setup
    logger.py           # Structured logging
    exceptions.py       # Custom exceptions
    middleware.py       # Global middleware
    
  modules/
    __init__.py
    
    users/
      __init__.py
      models.py         # SQLAlchemy models
      schemas.py        # Pydantic models
      services.py       # Business logic
      repositories.py   # Data access layer
      api.py           # FastAPI router
      dependencies.py  # Module dependencies
    
    machines/
      __init__.py
      models.py         # Machine entities
      schemas.py        # Machine DTOs
      services.py       # Machine business logic
      repositories.py   # Machine data access
      api.py           # Machine endpoints
      dependencies.py  # Machine dependencies
    
    production/
      __init__.py
      models.py         # Production orders, schedules
      schemas.py        # Production DTOs
      services.py       # Production logic
      repositories.py   # Production data
      api.py           # Production endpoints
      dependencies.py  # Production dependencies
    
    monitoring/
      __init__.py
      models.py         # Sensor data, metrics
      schemas.py        # Monitoring DTOs
      services.py       # Real-time processing
      repositories.py   # Time-series data
      api.py           # Monitoring endpoints
      dependencies.py  # Monitoring dependencies
    
    shared/
      __init__.py
      models.py         # Base models, enums
      schemas.py        # Common DTOs
      utils.py          # Utilities, helpers
      enums.py          # System enums
```

#### b) Key Features cho MES

**Auto API Documentation:**
```python
# FastAPI auto-generates Swagger UI
# Access: http://localhost:8000/docs
from fastapi import FastAPI
from libs.modules.users.api import router as users_router
from libs.modules.machines.api import router as machines_router

app = FastAPI(
    title="MES System API",
    description="Manufacturing Execution System",
    version="1.0.0"
)

app.include_router(users_router, prefix="/api/v1")
app.include_router(machines_router, prefix="/api/v1")
```

**Dependency Injection:**
```python
# libs/modules/machines/dependencies.py
from fastapi import Depends
from libs.core.database import get_db
from .repositories import MachineRepository
from .services import MachineService

def get_machine_repository(db = Depends(get_db)) -> MachineRepository:
    return MachineRepository(db)

def get_machine_service(
    repo: MachineRepository = Depends(get_machine_repository)
) -> MachineService:
    return MachineService(repo)
```

**Real-time WebSocket:**
```python
# apps/socket/main.py
from fastapi import WebSocket
from libs.core.cache import redis_client

@app.websocket("/ws/monitoring")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Stream real-time sensor data
        data = await redis_client.blpop("sensor_data")
        await websocket.send_json(data)
```

#### c) Performance Advantages

**Async Database Operations:**
```python
# libs/modules/machines/services.py
from sqlalchemy.ext.asyncio import AsyncSession

class MachineService:
    async def get_real_time_status(self, machine_id: str) -> dict:
        async with self.db as session:
            # Non-blocking database query
            machine = await session.get(Machine, machine_id)
            return {
                "status": machine.status,
                "last_updated": machine.updated_at,
                "efficiency": await self.calculate_efficiency(machine_id)
            }
```

**Type Safety & Validation:**
```python
# libs/modules/machines/schemas.py
from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class MachineCreate(BaseModel):
    name: str
    type: str
    location: str
    
    @validator('name')
    def validate_name(cls, v):
        if len(v) < 3:
            raise ValueError('Name must be at least 3 characters')
        return v

class MachineResponse(BaseModel):
    id: str
    name: str
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
```

#### d) Production Benefits

**High Performance:**
- **2-3x faster** than traditional Node.js/Express
- **Async native** cho real-time sensor data
- **Lower memory usage** - 40% savings

**Developer Experience:**
- **Auto-generated API docs** - không need manual documentation
- **Type hints** + Pydantic validation
- **Built-in testing** with TestClient
- **Simple deployment** - single Dockerfile

**Enterprise Ready:**
- **Modular architecture** - easy scaling
- **Dependency injection** - easy testing
- **Database migrations** - automated schema management
- **Redis caching** - performance optimization
- **WebSocket support** - real-time monitoring

#### e) Recommendation cho MES

**Modular Monolith là perfect choice cho:**
- **Medium to large MES systems** (50+ machines)
- **Teams 10-20 developers**
- **Real-time requirements** (sensor data, monitoring)
- **Future microservices migration** (easy to split modules)

**Key Advantages:**
- **Proven architecture** - used in production systems
- **Balanced complexity** - không quá simple, không quá phúc ttp
- **Easy to maintain** - clear module boundaries
- **Cost-effective** - single deployment, shared resources
- **Performance optimized** - async operations, efficient resource usage

### 8. Công nghc b sung cho MES

**Database:**
- PostgreSQL cho relational data (production orders, users)
- InfluxDB/TimescaleDB cho time-series data (sensor readings)
- Redis cho caching và real-time data

**Message Queue:**
- RabbitMQ cho reliable message delivery
- Apache Kafka cho high-throughput data streaming

**Real-time Communication:**
- WebSocket cho live monitoring
- MQTT cho IoT device communication

---

## 🎯 Gợi ý Lộ trình Thực hành:
1. Nắm vững biến, kiểu dữ liệu, vòng lặp.
2. Giải một số bài tập thuật toán cơ bản bằng Python.
3. Học cách quản lý module và tạo một project nhỏ (Ví dụ: Game đoán số, Quản lý sinh viên trên console, Ứng dụng To-Do List).
4. **Chọn framework phù hợp cho MES:**
   - **FastAPI** nếu cần performance và real-time features
   - **Django** nếu cần enterprise features và admin panel
   - **Flask** nếu cần flexibility và microservices
5. Xây dựng project MES nhỏ:
   - Production data collection API
   - Real-time monitoring dashboard
   - Machine status management system
6. Tìm hiểu chuyên sâu một hệ sinh thái (Web với Django/FastAPI, Data Science với Pandas/Numpy, AI/ML với Scikit-Learn/PyTorch).

Chúc bạn học Python hiệu quả!
