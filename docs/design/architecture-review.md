\# Thiết kế hệ thống DA-01



\- Người phụ trách: Huỳnh Tâm Trí

\- Nhiệm vụ: DA01-003

\- Ngày thực hiện: \[điền ngày thực tế]

\- Trạng thái: Bản thiết kế dự thảo, chưa triển khai.



\## 1. Mục tiêu



Thiết kế hệ thống nghiên cứu ảnh hưởng của PCA và LDA

đến phân loại hồ sơ có nhãn đột quỵ, kèm ứng dụng minh họa.



\## 2. Luồng nghiên cứu và huấn luyện



CSV gốc → kiểm kê → chia dữ liệu → tiền xử lý

→ dùng trực tiếp hoặc giảm chiều → huấn luyện

→ đánh giá → lưu kết quả và mô hình.



Trong mỗi lượt đánh giá:

\- Chỉ học các thông số tiền xử lý từ phần train.

\- PCA học từ X\_train.

\- LDA học từ X\_train và y\_train.

\- Áp dụng các bộ biến đổi đã học sang phần đánh giá.

\- Không chọn mô hình hoặc ngưỡng bằng kết quả trên test cuối.



\## 3. Luồng dự đoán



Nhập hồ sơ → kiểm tra đầu vào → tiền xử lý đã lưu

→ giảm chiều nếu có → mô hình đã lưu

→ xác suất → ngưỡng cảnh báo → hiển thị.



Không huấn luyện lại trong yêu cầu dự đoán.

Mỗi mô hình phải đi cùng đúng bộ tiền xử lý và giảm chiều.



\## 4. Trách nhiệm các thư mục



\- data/: CSV, kiểm kê và mã nạp/tiền xử lý.

\- models/: mã thuật toán và các độ đo.

\- experiments/: cấu hình, chạy thực nghiệm và đánh giá.

\- analysis/: phân tích dữ liệu, tạo bảng và biểu đồ.

\- results/: kết quả thực nghiệm và thông tin lần chạy.

\- app/: API, giao diện và hiện vật dùng để dự đoán.

\- tests/: kiểm thử.

\- docs/: tài liệu nghiên cứu và thiết kế.



\## 5. Sáu màn hình dự kiến



1\. Tổng quan dữ liệu: số mẫu, phân bố nhãn, thiếu dữ liệu.

2\. Dự đoán: nhập hồ sơ, chọn mô hình, xem xác suất.

3\. Huấn luyện nhỏ: cấu hình, tiến độ, dừng và kết quả.

4\. Giảm chiều: PCA/LDA, hướng chiếu và thông tin liên quan.

5\. So sánh: bảng, biểu đồ kết quả và xuất CSV.

6\. Ngưỡng cảnh báo: thay đổi ngưỡng, xem FP/FN

&#x20;  và các điểm tương ứng trên hình PCA/LDA.



\## 6. Trạng thái khi chưa có kết quả



Hiển thị rõ chưa có mô hình hoặc kết quả.

Không tạo số liệu hay dự đoán giả để điền vào giao diện.



\## 7. Phần còn cần thực hiện



\- Phác thảo bố cục của từng màn hình.

\- Xác định đầu vào, đầu ra và trạng thái lỗi từng màn.

\- Đối chiếu lại REQUIREMENTS.md.



\## 8. AI hỗ trợ



AI hỗ trợ giải thích luồng xử lý và soạn bản nháp.

Trí cần đọc, đối chiếu và quyết định thiết kế.

