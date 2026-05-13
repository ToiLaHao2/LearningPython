# Warehouse Management System Simulation - WMSS (MES Layer / Python)

Dự án này là tầng **MES (Manufacturing Execution System)** - "Người điều phối" trong hệ thống mô phỏng tự động hóa nhà kho đa ngôn ngữ (Polyglot Microservices).

## 🧩 Vai trò trong hệ thống

MES đóng vai trò trung gian, chịu trách nhiệm về logic tính toán phức tạp và điều phối nhiệm vụ:

- **ERP / WMS (Node.js):** Đóng vai trò là "Bộ não chiến lược" - Quản lý logic hàng hóa và ra lệnh.
- **MES (Python):** Đóng vai trò "Người điều phối" - Lập lịch, tìm đường (Pathfinding) và phân bổ tác vụ.
- **AGV Control Service (Golang):** Đóng vai trò "Hệ cơ bắp" - Điều khiển và tính toán tọa độ di chuyển thực tế.

## 🛠 Công nghệ sử dụng

- **Python 3.10+**: Ngôn ngữ hiện đại, mạnh mẽ cho xử lý thuật toán và AI.
- **FastAPI**: Framework hiệu suất cao, hỗ trợ tốt cho AsyncIO và gRPC.
- **gRPC**: Giao tiếp nội bộ tốc độ cao với tầng Node.js (WMS).
- **Kafka**: Hệ thống Event-stream để điều phối trạng thái AGV theo thời gian thực.
- **Redis**: Caching bản đồ kho hàng (NavMesh) để tối ưu hóa tốc độ tìm đường.

## 🚀 Các Module chính

- `libs/modules/pathfinding`: Triển khai thuật toán **A* Pathfinding** để tính toán đường đi ngắn nhất cho AGV trên lưới NavMesh.
- `apps/api_gateway`: Tầng giao tiếp (HTTP/gRPC) để tiếp nhận lệnh từ hệ thống WMS.

## 🔄 Luồng xử lý chính

1. Nhận yêu cầu di chuyển từ WMS (qua gRPC).
2. Lấy dữ liệu Layout kho từ Redis.
3. Tính toán lộ trình tối ưu bằng thuật toán A*.
4. Gửi danh sách Waypoints cho tầng AGV Control (Go) để thực thi.

## 💻 Hướng dẫn phát triển

### 1. Thiết lập môi trường

```bash
# Di chuyển vào thư mục MES
cd MES

# Tạo môi trường ảo
python -m venv .venv

# Kích hoạt môi trường (Windows)
.venv\Scripts\activate

# Cài đặt thư viện
pip install -r requirements.txt
```

### 2. Chạy ứng dụng (Development mode)

```bash
uvicorn apps.api_gateway.main:app --reload
```

## 🧠 Thuật toán A* (A-Star Pathfinding)

Tầng MES sử dụng thuật toán **A*** làm hạt nhân để tính toán lộ trình cho AGV. A* là một thuật toán tìm kiếm đồ thị phổ biến và cực kỳ hiệu quả cho bài toán tìm đường đi ngắn nhất.

### Nguyên lý hoạt động

Thuật toán đánh giá các Node (ô lưới) dựa trên hàm chi phí tổng quát:
`f(n) = g(n) + h(n)`

Trong đó:

- `f(n)`: Tổng chi phí ước tính để đi từ điểm xuất phát đến đích thông qua Node `n`.
- `g(n)`: Chi phí thực tế đã tiêu tốn để đi từ điểm xuất phát đến Node `n`.
- `h(n)`: **Hàm Heuristic** - Ước lượng chi phí từ Node `n` đến đích. Đây là "bộ não" của thuật toán, giúp A* định hướng tìm kiếm thông minh thay vì mở rộng mù quáng. Trong thực tế, hàm Heuristic còn giúp hệ thống cân nhắc các yếu tố như: vật cản xuất hiện bất ngờ, các lối rẽ, hay luồng giao thông chồng chéo của các AGV khác.

### Hàm Heuristic: Khoảng cách Manhattan

Do đặc thù của hệ thống kho hàng (Grid), AGV chỉ có thể di chuyển theo 4 hướng trực giao (Lên, Xuống, Trái, Phải), hoàn toàn không thể đi chéo. Vì vậy, **Khoảng cách Manhattan** được lựa chọn làm hàm Heuristic vì nó phản ánh chính xác nhất thực tế di chuyển:

`h(n) = |x_n - x_end| + |y_n - y_end|`

Việc sử dụng Manhattan giúp thuật toán chạy nhanh, tối ưu và đảm bảo luôn tìm ra đường đi ngắn nhất tuyệt đối (admissible heuristic).

### Tại sao chọn A* thay vì Dijkstra hay các thuật toán khác?

- **So với Dijkstra:** Dijkstra có xu hướng tìm kiếm mọi hướng như giọt nước loang ra, gây lãng phí tài nguyên tính toán. A* nhờ có hàm Heuristic sẽ được "hút" thẳng về phía đích, giúp tốc độ nhanh hơn vượt trội trong môi trường không gian rộng lớn như kho bãi.
- **So với BFS/DFS:** BFS loang mù quáng và rất chậm. DFS tìm được đường nhưng hiếm khi là đường đi ngắn nhất.
- **Khả năng mở rộng (Collision Avoidance):** Trong tương lai, A* rất dễ tùy biến. Bằng cách cộng thêm "hình phạt" (penalty weight) vào hàm `g(n)` tại những ô đang có AGV khác đi qua, thuật toán sẽ tự động giúp AGV tính toán và tìm một "đường vòng" để tránh kẹt xe.

## 🔮 Tầm nhìn & Định hướng phát triển

Sau khi hệ thống nền tảng với thuật toán A* hoàn thiện, dự án sẽ hướng tới việc tích hợp trí tuệ nhân tạo (AI) để nâng cấp kho hàng thành một hệ thống **Smart Warehouse** thực thụ:

- **AI-Driven Scheduling:** Thay thế việc lập lịch thủ công bằng các mô hình học máy để điều phối hàng ngàn nhiệm vụ cùng lúc, đảm bảo thời gian hoàn thành là ngắn nhất.
- **Slot Optimization (Tối ưu hóa vị trí):** Sử dụng AI để phân tích dữ liệu lịch sử xuất/nhập, từ đó gợi ý vị trí sắp xếp hàng hóa một cách khoa học (ví dụ: hàng hay xuất sẽ để gần lối đi), giúp giảm 30-50% quãng đường di chuyển của AGV.
- **Traffic Intelligence:** Nâng cấp thuật toán tìm đường kết hợp với học sâu (Deep Learning) để AGV có thể tự học cách xử lý các tình huống giao thông phức tạp, tránh ùn tắc và va chạm một cách chủ động.
