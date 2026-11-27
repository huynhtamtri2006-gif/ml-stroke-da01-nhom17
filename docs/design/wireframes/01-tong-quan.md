\# Phác thảo màn hình 1 — Tổng quan dữ liệu



\- Người phụ trách: Huỳnh Tâm Trí

\- Nhiệm vụ: DA01-003

\- Trạng thái: Thiết kế dự thảo, chưa lập trình.



\## 1. Mục đích



Giúp người xem hiểu nguồn dữ liệu, quy mô, phân bố nhãn

và các vấn đề cần xử lý trước khi huấn luyện.



\## 2. Bố cục dự kiến



```text

+------------------------------------------------------+

| DA-01 — Phân tích dữ liệu đột quỵ                     |

+------------------------------------------------------+

| Tổng quan | Dự đoán | Huấn luyện | Giảm chiều          |

| So sánh kết quả | Ngưỡng cảnh báo                     |

+------------------------------------------------------+

| Nguồn dữ liệu và giới thiệu bài toán                  |

+------------------------------------------------------+

| Số hồ sơ | Số cột | Nhãn 1 | BMI thiếu                 |

+------------------------------------------------------+

| Biểu đồ số lượng hồ sơ theo nhãn stroke               |

+------------------------------------------------------+

| Bảng thống kê dữ liệu thiếu                          |

+------------------------------------------------------+

| Bảng ít nhất 5 hồ sơ mẫu thuộc tập train              |

+------------------------------------------------------+

| Nhận xét và giới hạn của dữ liệu                     |

+------------------------------------------------------+

```



\## 3. Nội dung hiển thị



\### Nguồn và bài toán

\- Tên: Stroke Prediction Dataset.

\- Có liên kết nguồn và thông tin bản quyền.

\- Giới thiệu mục tiêu phân loại hồ sơ có nhãn đột quỵ.



\### Các thẻ thống kê

\- Tổng số hồ sơ.

\- Tổng số cột.

\- Số hồ sơ stroke = 1 và tỷ lệ tương ứng.

\- Số giá trị BMI thiếu.



Các giá trị được lấy từ API thống kê dữ liệu thật.

Không viết cố định các con số vào giao diện.



\### Biểu đồ phân bố nhãn

\- Trục ngang: nhãn 0 và 1.

\- Trục dọc: số hồ sơ.

\- Hiển thị số lượng và tỷ lệ bằng chữ.

\- Không chỉ dùng màu để phân biệt hai lớp.



\### Bảng dữ liệu thiếu

\- Tên cột.

\- Số lượng giá trị thiếu.

\- Tỷ lệ thiếu.

\- Unknown trong smoking\_status được trình bày riêng,

&#x20; không tự đổi thành never smoked.



\### Bảng hồ sơ mẫu

\- Hiển thị ít nhất 5 mẫu từ tập train.

\- Có đủ đặc trưng và nhãn.

\- Ghi rõ đây là mẫu thuộc tập train.

\- Chỉ hiển thị mẫu sau khi đã xác định tập train.



\## 4. Luồng hoạt động



Mở trang → gọi API thống kê → nhận dữ liệu

→ hiển thị thẻ thống kê, bảng và biểu đồ.



API dự kiến:

\- GET /api/thong-ke

\- GET /api/mau



Đây là thiết kế, các API chưa được triển khai.



\## 5. Trạng thái cần xử lý



\- Đang tải: hiển thị thông báo đang tải dữ liệu.

\- Thành công: hiển thị dữ liệu trả về.

\- Lỗi: thông báo nguyên nhân dễ hiểu và nút thử lại.

\- Chưa có tập train: chưa hiển thị hồ sơ mẫu,

&#x20; giải thích cần hoàn thành bước chia dữ liệu.



\## 6. Tiêu chí kiểm tra khi lập trình



\- Số liệu khớp dữ liệu được API đọc.

\- Ghi rõ thống kê toàn CSV và mẫu thuộc tập train.

\- Có tiêu đề, nhãn và chú giải.

\- Đọc được trên màn hình rộng và màn hình 768px.

\- Không phụ thuộc tài nguyên biểu đồ trên Internet.



\## 7. AI hỗ trợ



AI hỗ trợ soạn bản phác thảo.

Trí đọc, điều chỉnh và quyết định thiết kế.



\## 8. Giải thích các quyết định thiết kế



\### 8.1. Vì sao màn hình tổng quan chưa đưa ra dự đoán?



Màn hình này giúp người xem hiểu quy mô, phân bố nhãn

và dữ liệu thiếu trước khi xây dựng mô hình.



Ví dụ, 249 hồ sơ có nhãn đột quỵ là số đếm từ CSV,

không phải kết quả dự đoán của mô hình.



Chức năng dự đoán hồ sơ mới thuộc màn hình Dự đoán.



\### 8.2. Vì sao lấy thống kê qua API?



Giao diện gửi yêu cầu đến backend qua API.

Backend đọc dữ liệu hoặc báo cáo kiểm kê tương ứng,

sau đó trả số liệu để giao diện hiển thị.



Luồng dự kiến:

Mở trang → gọi API → backend lấy thống kê

→ trả kết quả → giao diện hiển thị.



Không viết cố định các con số vào giao diện,

tránh hiển thị số cũ khi dữ liệu thay đổi.



Kết quả API cần được đối chiếu với công cụ kiểm kê.

Hiện API chưa được triển khai.



\### 8.3. Vì sao bảng mẫu chỉ lấy từ train?



Tập train phục vụ phát triển và học mô hình.

Tập test được giữ riêng để đánh giá cuối cùng.



Dùng mẫu train để minh họa giúp hạn chế việc xem test

rồi điều chỉnh phương pháp theo chính tập test đó.



Nếu chưa chia dữ liệu, chưa hiển thị mẫu train

và cần giải thích rõ trên giao diện.



Thống kê toàn CSV được dùng để mô tả dữ liệu.

Các thông số tiền xử lý và giảm chiều phải được học

từ phần train tương ứng.



\## 9. Nguồn hỗ trợ phần giải thích



AI hỗ trợ giải thích và soạn nội dung bổ sung.

Trí đọc, đối chiếu và quyết định sử dụng trong thiết kế.

