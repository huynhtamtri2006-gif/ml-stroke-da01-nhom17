# Từ điển dữ liệu Stroke

Đọc cùng [nguồn và hồ sơ dữ liệu](PROVENANCE.md). Tên cột giữ nguyên chữ hoa/thường của CSV. Mô tả dựa trên yêu cầu DA-01 và cấu trúc bộ dữ liệu chỉ định, cần đối chiếu Data Card Kaggle khi tải. Các mức phân loại dưới đây là mức dự kiến; công cụ kiểm kê sẽ liệt kê mức thực tế, không sửa giá trị gốc.

| Cột | Vai trò / kiểu | Ý nghĩa | Giá trị và lưu ý | Xử lý dự kiến |
|---|---|---|---|---|
| id | Định danh / số nguyên | Mã bản ghi do nguồn cung cấp | Không phải thông tin lâm sàng; kiểm tra trùng | Không làm đặc trưng |
| gender | Đầu vào / phân loại | Giới tính được ghi trong dữ liệu | Male, Female, Other; mức hiếm vẫn cần kiểm kê | One-hot, không tự xóa Other |
| age | Đầu vào / số thực | Tuổi, theo năm | Có thể có phần thập phân; không ép tất cả thành số nguyên | Chuẩn hóa trên train |
| hypertension | Đầu vào / nhị phân | Nhãn có tăng huyết áp trong hồ sơ | 0: không; 1: có, theo mô tả nguồn | Giữ nhị phân |
| heart_disease | Đầu vào / nhị phân | Nhãn có bệnh tim trong hồ sơ | 0: không; 1: có, theo mô tả nguồn | Giữ nhị phân |
| ever_married | Đầu vào / phân loại | Tình trạng từng kết hôn được ghi nhận | No, Yes | One-hot |
| work_type | Đầu vào / phân loại | Nhóm nghề nghiệp/tình trạng làm việc | children, Govt_job, Never_worked, Private, Self-employed; đối chiếu cách viết thực tế | One-hot |
| Residence_type | Đầu vào / phân loại | Loại khu vực cư trú | Rural, Urban; chữ R viết hoa trong tên cột | One-hot |
| avg_glucose_level | Đầu vào / số thực | Mức đường huyết trung bình theo nguồn | Chưa xác nhận đơn vị từ Data Card; không tự gắn mg/dL hoặc ngưỡng lâm sàng | Chuẩn hóa trên train |
| bmi | Đầu vào / số thực, có thiếu | Chỉ số khối cơ thể | Theo đề có 201 giá trị N/A; kiểm kê thực tế. Đơn vị theo định nghĩa BMI là kg/m², cần kiểm tra mô tả nguồn | Điền khuyết chỉ bằng thống kê train rồi chuẩn hóa |
| smoking_status | Đầu vào / phân loại | Tình trạng hút thuốc được ghi nhận | formerly smoked, never smoked, smokes, Unknown; Unknown thể hiện chưa có thông tin, không phải never smoked | Cấu hình đầu giữ Unknown thành mức riêng và giải trình |
| stroke | Nhãn / nhị phân | Nhãn đột quỵ của hồ sơ | 1: có nhãn đột quỵ; 0: không. Không có mốc thời gian để tự suy ra dự báo một biến cố tương lai | Tách thành y, không đưa vào X |

## Số lượng theo đề để đối chiếu

5.110 dòng; 12 cột; 4.861 nhãn 0 và 249 nhãn 1; 201 ô BMI thiếu. Đây là số từ tài liệu giảng viên, chưa phải kết quả kiểm kê của nhóm.

## Quy ước quan trọng

- Giữ nguyên CSV gốc; mọi phép biến đổi ở bộ tiền xử lý, không lưu đè bản raw.
- Không điền BMI bằng trung vị toàn bộ file rồi mới chia train/test.
- Không coi Unknown là không hút thuốc và không loại các mức hiếm chỉ vì khó xử lý.
- Không dùng id hoặc stroke làm đặc trưng. Sau khi bỏ id/tách nhãn còn 10 đặc trưng gốc; số chiều tăng sau one-hot.
- Thống kê toàn CSV là mô tả dữ liệu, không chứng minh hiệu năng mô hình hoặc nguồn gốc lâm sàng.
