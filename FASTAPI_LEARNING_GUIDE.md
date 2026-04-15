# Hướng Dẫn Học FastAPI - Lộ Trình Chinh Phục Phát Triển API

## 1. FastAPI là gì?

### 1.1 Định nghĩa
**FastAPI** là framework web hiện đại của Python được thiết kế để xây dựng các API. Nó được xây dựng trên Starlette (để xử lý web) và Pydantic (để xác thực dữ liệu).

### 1.2 Cách hoạt động
```python
# Cách FastAPI hoạt động
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # 1. Tạo app instance

class Item(BaseModel):  # 2. Định nghĩa data model
    name: str
    price: float

@app.post("/items/")  # 3. Định nghĩa endpoint
async def create_item(item: Item):  # 4. Tự động validation
    return {"message": "Item created", "data": item}
```

**Luồng hoạt động:**
1. **Request** -> FastAPI nhận HTTP request
2. **Validation** -> Pydantic xác thực dữ liệu
3. **Processing** -> Function của bạn chạy
4. **Response** -> FastAPI trả về JSON response
5. **Documentation** -> Tự động tạo OpenAPI docs

---

## 2. So Sánh FastAPI với các Framework Khác

### 2.1 So Sánh Hiệu Suất

| Framework | Requests/Second | Memory Usage | Latency |
|-----------|-----------------|--------------|---------|
| **FastAPI** | ~2,800 RPS | ~120MB | ~20ms |
| Django | ~1,200 RPS | ~200MB | ~50ms |
| Flask | ~1,900 RPS | ~150MB | ~35ms |
| Express.js | ~2,100 RPS | ~180MB | ~40ms |

### 2.2 So Sánh Tính Năng

| Tính Năng | FastAPI | Django | Flask | Express.js |
|-----------|---------|--------|-------|-------------|
| **Auto Docs** | Swagger UI | Django REST | Manual | Manual |
| **Type Hints** | Built-in | Limited | None | TypeScript |
| **Validation** | Pydantic | Forms | Manual | Joi/Yup |
| **Async Support** | Native | Limited | Extension | Native |
| **Learning Curve** | Medium | High | Low | Medium |

---

## 3. 3 Điểm Nổi Bật Của FastAPI

### 3.1 Hiệu Suất Vượt Trội
```python
# Async operations - lợi thế chính
@app.get("/machines/{machine_id}")
async def get_machine(machine_id: str):
    # Database query không blocking
    machine = await db.get_machine(machine_id)
    # External API call không blocking
    status = await external_api.get_status(machine_id)
    return {"machine": machine, "status": status}
```

**Lợi ích:**
- **2-3x nhanh hơn** Django/Flask
- **Tiết kiệm memory** - 40% ít hơn
- **Concurrency tốt hơn** - xử lý hàng ngàn request

### 3.2 Trải Nghiệm Phát Triển
```python
# Tự động tạo documentation
# Truy cập: http://localhost:8000/docs
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr  # Tự động validation
    password: str
    age: int = 18  # Giá trị mặc định

@app.post("/users/")
async def create_user(user: UserCreate):
    # Pydantic tự động validate
    return {"user": user}
```

**Lợi ích:**
- **Auto API docs** - không cần viết documentation thủ công
- **Type safety** - bắt bugs ở thời gian phát triển
- **IDE support** - autocomplete và error checking

### 3.3 Tính Năng Python Hiện Đại
```python
# Python 3.8+ features
from typing import List, Optional
from datetime import datetime

class ProductionOrder(BaseModel):
    id: str
    items: List[str]
    created_at: datetime
    completed_at: Optional[datetime] = None

@app.get("/orders/")
async def get_orders() -> List[ProductionOrder]:
    return await get_all_orders()
```

---

## 4. FastAPI Tối Ưu Ở Điểm Nào?

### 4.1 Cho Real-time Applications
```python
# WebSocket cho real-time monitoring
@app.websocket("/ws/monitoring")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Stream real-time sensor data
        data = await sensor_queue.get()
        await websocket.send_json(data)
```

### 4.2 Cho Microservices
```python
# Lightweight cho microservices
app = FastAPI(title="Machine Service", version="1.0.0")

@app.get("/machines/")
async def get_machines():
    return await machine_service.get_all()

@app.post("/machines/")
async def create_machine(machine: MachineCreate):
    return await machine_service.create(machine)
```

### 4.3 Cho Data Processing APIs
```python
# Perfect cho ML/Data Science APIs
@app.post("/predict/")
async def predict(data: PredictionInput):
    # Pydantic validates input
    processed_data = preprocess(data.dict())
    prediction = await model.predict(processed_data)
    return {"prediction": prediction}
```

---

## 5. Những Gì Phải Chú Ý

### 5.1 Async/Await Learning Curve
```python
# Phân biệt sync vs async
# SAI - Blocking operation
@app.get("/data/")
def get_data():
    result = database.query("SELECT * FROM machines")  # Blocking!
    return result

# ĐÚNG - Non-blocking operation
@app.get("/data/")
async def get_data():
    result = await database.query("SELECT * FROM machines")  # Non-blocking!
    return result
```

### 5.2 Database Integration
```python
# SQLAlchemy async setup
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine("postgresql+asyncpg://...")
async_session = sessionmaker(engine, class_=AsyncSession)

# Dependency injection
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
```

### 5.3 Error Handling
```python
from fastapi import HTTPException

@app.get("/machines/{machine_id}")
async def get_machine(machine_id: str):
    machine = await get_machine_by_id(machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine
```

---

## 6. Nhược Điểm Của FastAPI

### 6.1 Nhược Điểm Chính
- **Ecosystem nhỏ hơn** so với Django/Flask
- **Ít tutorials hơn** và ví dụ
- **Async complexity** cho beginners
- **Limited admin interface** (không có built-in admin)

### 6.2 Khi Không Nên Dùng FastAPI
- **Simple CRUD apps** - Flask có thể tốt hơn
- **Full-stack applications** - Django có admin panel
- **Rapid prototyping** - Flask đơn giản hơn
- **Team không familiar với async**

---

## 7. Hướng Dẫn Học FastAPI

### 7.1 Lộ Trình Học Tập

#### Step 1: Python Fundamentals (1-2 tuần)
```python
# Cần nắm vững Python basics
- Variables, types, functions
- Classes và OOP
- Async/await concepts
- Type hints
```

#### Step 2: FastAPI Basics (1 tuần)
```python
# Hello World
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Run: uvicorn main:app --reload
```

#### Step 3: Pydantic Models (3 ngày)
```python
from pydantic import BaseModel, validator

class Machine(BaseModel):
    name: str
    power: int
    status: str
    
    @validator('power')
    def power_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Power must be positive')
        return v
```

#### Step 4: Database Integration (1 tuần)
```python
# SQLAlchemy + FastAPI
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Machine(Base):
    __tablename__ = "machines"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    power = Column(Integer)
```

#### Step 5: Advanced Features (2 tuần)
```python
# Authentication, WebSocket, Background tasks
from fastapi import Depends, WebSocket
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

### 7.2 Projects Thực Hành

#### Project 1: Simple To-Do API (1 tuần)
```python
# CRUD operations
@app.post("/todos/")
async def create_todo(todo: TodoCreate):
    return await todo_service.create(todo)

@app.get("/todos/")
async def get_todos():
    return await todo_service.get_all()
```

#### Project 2: Machine Monitoring API (2 tuần)
```python
# Real-time monitoring
@app.websocket("/ws/machines")
async def machine_monitoring(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await get_machine_data()
        await websocket.send_json(data)
```

#### Project 3: Production Management API (3 tuần)
```python
# Complex business logic
@app.post("/production/orders/")
async def create_order(order: OrderCreate):
    # Validate inventory
    # Schedule production
    # Send notifications
    return await order_service.create(order)
```

### 7.3 Best Practices

#### Code Organization
```python
# Project structure
mes_system/
main.py
app/
    __init__.py
    api/
        __init__.py
        v1/
            __init__.py
            endpoints/
                machines.py
                production.py
    core/
        __init__.py
        config.py
        database.py
        security.py
    models/
        __init__.py
        machine.py
        production.py
    schemas/
        __init__.py
        machine.py
        production.py
```

#### Testing
```python
# Unit tests
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_machines():
    response = client.get("/machines/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

---

## 8. Resources Học Tập

### 8.1 Official Resources
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Pydantic Documentation**: https://pydantic-docs.helpmanual.io/
- **Starlette Documentation**: https://www.starlette.io/

### 8.2 Courses
- **FastAPI by TestDriven.io**: Khóa học toàn diện
- **FastAPI on Udemy**: Nhiều lựa chọn
- **YouTube tutorials**: Nội dung miễn phí

### 8.3 Books
- **Building Data Science Applications with FastAPI**
- **Web Development with FastAPI**

### 8.4 Community
- **GitHub Discussions**: https://github.com/tiangolo/fastapi/discussions
- **Reddit**: r/FastAPI
- **Discord**: FastAPI community

---

## 9. Tips cho MES Development

### 9.1 Real-time Data Handling
```python
# Sensor data streaming
@app.websocket("/ws/sensors")
async def sensor_stream(websocket: WebSocket):
    await websocket.accept()
    async for data in sensor_stream:
        await websocket.send_json({
            "timestamp": datetime.now(),
            "data": data
        })
```

### 9.2 Performance Optimization
```python
# Caching cho frequent requests
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

FastAPICache.init(RedisBackend(redis_client))

@app.get("/machines/{machine_id}")
@cache(expire=60)  # Cache 60 giây
async def get_machine(machine_id: str):
    return await machine_service.get_by_id(machine_id)
```

### 9.3 Error Handling cho Production
```python
# Custom exception handlers
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body}
    )
```

---

## 10. Kết Luận

### 10.1 Khi nào nên dùng FastAPI?
- **High-performance APIs** cần thiết
- **Real-time applications** (WebSocket)
- **Microservices architecture**
- **Data science/ML APIs**
- **Type safety quan trọng**

### 10.2 Key Takeaways
- **Performance leader** trong Python frameworks
- **Modern Python features** integration
- **Excellent developer experience**
- **Growing ecosystem**
- **Perfect cho MES systems**

### 10.3 Next Steps
1. **Master Python async/await**
2. **Build small projects**
3. **Learn Pydantic deeply**
4. **Practice database integration**
5. **Explore deployment options**

**FastAPI là tương lai của Python web development - đặc biệt cho các hệ thống hiệu suất cao như MES!**
