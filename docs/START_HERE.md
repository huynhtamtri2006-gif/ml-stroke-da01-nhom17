# Bắt đầu sau khi nhận repository

Gói đã có CSV gốc, từ điển, công cụ/báo cáo kiểm kê, hai PDF yêu cầu, kế hoạch và nhiệm vụ cá nhân. Đủ để hai người bắt đầu nghiên cứu và chuẩn bị triển khai; chưa có thuật toán học máy hoặc ứng dụng hoàn chỉnh.

## 1. Luân clone repo và nhận quyền đóng góp

Repository hiện là **Public** theo cập nhật của Trí: Luân có thể đọc và clone ngay, không cần lời mời để tải về. Để push nhánh vào repository này, Trí vẫn cần thêm Luân làm collaborator và Luân chấp nhận lời mời bằng tài khoản cá nhân. Đọc/clone và push là hai quyền khác nhau; Public không tự cho mọi người quyền sửa repo.

Luân làm trên nhánh riêng và tạo Pull Request để Trí kiểm tra, không push trực tiếp hoặc tự merge vào main. Việc chặn bằng Rulesets phải được Trí cấu hình riêng; tài liệu này không xác nhận quy tắc đã bật trên GitHub.

```powershell
git clone https://github.com/huynhtamtri2006-gif/ml-stroke-da01-nhom17.git
cd ml-stroke-da01-nhom17
python --version
```

Nếu đã clone, lưu/commit thay đổi đang làm trước rồi cập nhật main theo CONTRIBUTING.md. Không git init lại.

## 2. Kiểm tra dữ liệu trên máy Luân

```powershell
python data/kiem_ke.py --output-dir data/processed/kiem_ke_ca_nhan
python -m unittest discover -s tests -p "test_kiem_ke.py" -v
```

Nếu dùng py launcher thì thay python bằng py. Không cần cài thư viện bổ sung. Báo cáo cá nhân ở data/processed/ bị gitignore, tránh làm đổi timestamp của bản tham chiếu đã commit. Cần có 5110 dòng, 12 cột, stroke0=4861, stroke1=249, BMI thiếu201; SHA-256 khớp data/dataset_reference.json. Đây là kiểm kê và test công cụ, không phải kiểm thử mô hình.

## 3. Đọc và thống nhất trước khi lập trình

1. [PDF gốc](specifications/README.md): DA-01 ở 07 trang9–17; 07b là hướng dẫn chung.
2. [Phân tích](01_NGHIEN_CUU_VA_PHAN_TICH.md), [yêu cầu](../REQUIREMENTS.md), [bảng đối chiếu](REQUIREMENT_COVERAGE.md).
3. [Nguồn học](SOURCES.md), [giao thức](EXPERIMENT_PROTOCOL.md), [kiến trúc](ARCHITECTURE.md), [môi trường](ENVIRONMENT.md).
4. [Bàn giao](HANDOFFS.md) và [nhiệm vụ theo ngày](../TASK_ASSIGNMENTS.md).

Cả hai tự ghi câu hỏi/điều đã hiểu vào RESEARCH_LOG.md. Chốt metric/split, missing/Unknown, schema one-hot và hợp đồng fit/transform/predict_proba. Thống nhất môi trường học máy trước khi làm model; chưa có requirements.txt khóa cho phần chưa triển khai.

## 4. Việc đầu tiên của mỗi người

- Trí: review kiểm kê và hồ sơ nguồn; thiết kế luồng/wireframe6 màn; chuẩn bị bộ nạp/tiền xử lý sau khi chốt giao thức.
- Luân: đọc đề và PR-AUC/mất cân bằng; dự thảo giao thức/công thức Logistic; bài tập NumPy/gradient.
- Cả hai: review chéo, tạo/cập nhật Issue thật và nhật ký; có CSV/repo không tự đồng nghĩa đã hoàn tất các phần nghiên cứu.

Ngày trong lịch là kế hoạch; đầu vào có sớm được bắt đầu sớm, trễ thì ghi tình trạng thật. Hướng dẫn Projects đã có, chưa kiểm tra Project/Issue thực tế từ xa. Dùng nhánh và danh tính cá nhân, không ghi lịch sử thay người còn lại.
