# Kết quả kiểm kê ban đầu ngày 27/11/2026

Nguồn số liệu: [inventory.json](../data/inventory/inventory.json), tạo bằng công cụ kiểm kê trên CSV cục bộ của Trí. Đây là mô tả toàn dữ liệu, không phải kết quả học máy hoặc ghi nhận Luân đã phân tích.

| Đại lượng | Đo được |
|---|---:|
| Dòng / cột | 5.110 / 12 |
| stroke = 0 | 4.861 |
| stroke = 1 | 249 |
| Tỷ lệ nhãn dương | 4,8728% |
| BMI thiếu | 201 |
| Dòng trùng toàn bộ | 0 |
| Dòng trùng sau bỏ id | 0 |
| id trùng | 0 |
| smoking_status = Unknown | 1.544 |
| gender = Other | 1 |

Các số lượng cần đối chiếu khớp tài liệu đề. SHA-256 đã kiểm tra với file raw: `644d473b05d2797006bd94865e4f8bb057f0c721617911613c82c8fcfc707420`.

## Vấn đề cần nghiên cứu trước tiền xử lý

Trong 249 ca dương có 40 BMI thiếu, tương đương 16,06%. Trong 4.861 ca âm có 161 BMI thiếu, tương đương 3,31%. Nếu loại tất cả dòng thiếu BMI, sẽ loại 40 ca dương và 161 ca âm; do đó không được bỏ dòng âm thầm. Đây là khác biệt mô tả, chưa là kết luận nguyên nhân của thiếu dữ liệu hoặc quan hệ nhân quả.

Unknown của smoking_status có 1.544 mẫu. Cấu hình ban đầu giữ thành mức riêng và giải trình, không coi là never smoked. Mức gender = Other chỉ có 1 mẫu, không đủ cơ sở để đánh giá hiệu năng theo nhóm này một cách đáng tin.

Accuracy của quy tắc luôn đoán âm trên toàn CSV là 4.861/5.110 = 95,1272%, trong khi recall lớp dương là 0. Đây là phép tính baseline từ nhãn, không phải kết quả huấn luyện.

Median trong báo cáo chỉ mô tả toàn CSV; không dùng các giá trị này làm tham số điền khuyết hoặc chuẩn hóa khi chưa chia dữ liệu. Các quyết định mô hình phải tuân theo giao thức train-only/validation đã chốt.

## Trách nhiệm tiếp theo

Trí ghi nguồn và review kiểm kê; Luân tải bản từ cùng nguồn, đối chiếu hash và đọc giao thức. Sau review, cả hai ghi nghiên cứu thực vào RESEARCH_LOG.md, chốt xử lý missing/Unknown và split trước khi triển khai thuật toán. Nội dung phân tích trong file này có AI hỗ trợ, không tự ghi là công việc Luân đã làm.
