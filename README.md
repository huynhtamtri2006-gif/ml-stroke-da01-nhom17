# Đồ án Học máy DA-01 của nhóm 17

Nghiên cứu tác động của PCA và LDA đến phát hiện lớp đột quỵ hiếm trên Stroke Prediction Dataset. Hiện là bộ hồ sơ khởi động: chưa có mã thuật toán, dữ liệu CSV, mô hình hoặc kết quả thực nghiệm.

| Thành viên | MSSV | Vai trò | GitHub |
|---|---|---|---|
| Huỳnh Tâm Trí | 2045240315 | Giám sát nhiệm vụ; dữ liệu, kiến trúc, ứng dụng, tích hợp | huynhtamtri2006-gif |
| Cao Minh Luân | 2001240263 | Thuật toán, thực nghiệm, thống kê, hiệu chuẩn | Chưa cung cấp |

Trí giám sát công việc theo yêu cầu hiện tại. Danh sách giảng viên ghi Luân là nhóm trưởng và nhóm có 3 thành viên; bảng phân công triển khai cho hai người không tự sửa hồ sơ chính thức.

## Bắt đầu tại đây

1. Đọc [nghiên cứu giai đoạn 1](docs/01_NGHIEN_CUU_VA_PHAN_TICH.md).
2. Hai người đối chiếu [yêu cầu](REQUIREMENTS.md), [giao thức](docs/EXPERIMENT_PROTOCOL.md), rồi ghi quyết định thật trong RESEARCH_LOG.md.
3. Làm theo [hướng dẫn GitHub](docs/GITHUB_SETUP.md) để tạo repository Private và Projects.
4. Đọc [nhiệm vụ](TASK_ASSIGNMENTS.md) và mở file theo ngày trong docs/tasks/.
5. Chỉ bắt đầu lập trình khi nghiệm thu nghiên cứu, phạm vi và thiết kế.

## Cấu trúc theo đặc tả giảng viên

data/ → tiền xử lý; models/ → thuật toán; experiments/ → thí nghiệm; analysis/ → phân tích; app/ → ứng dụng; tests/ → kiểm chứng; results/ → số liệu; docs/ → nghiên cứu/thiết kế; reports/ → báo cáo; presentations/ → slide. Không tạo src/ song song để tránh hai nơi chứa cùng mã; giữ đường dẫn gốc theo tài liệu 07b.

## Trạng thái chạy

Chưa có lệnh huấn luyện hoặc chạy ứng dụng. README không tuyên bố dự án đã hoạt động. Quy trình cài đặt sẽ được bổ sung từng bước theo docs/ENVIRONMENT.md; requirements.txt được khóa sau khi kiểm tra môi trường thật.

## Câu hỏi nghiên cứu

PCA giữ phương sai lớn có đánh mất hướng phân biệt lớp hiếm không? Ở k nào hiệu năng thay đổi? LDA một chiều khác PCA thế nào? Độ đo chính dự kiến: PR-AUC hình thang của stroke = 1, theo đề. Chưa có kết luận mô hình thắng.

## Phạm vi

Logistic có trọng số, PCA và LDA tự viết bằng NumPy; metrics tự viết; kiểm chứng thư viện; baseline; 25 lần đo/cấu hình; gom cụm; mở rộng hiệu chuẩn/chi phí; ứng dụng 6 màn hình. Không làm deep learning, xác thực người dùng, cloud hoặc hệ thống khám bệnh.

## Nguồn và tính trung thực

Số 5.110 dòng, 249 nhãn dương và 201 BMI thiếu là số liệu của đề, chưa kiểm kê CSV. Dữ liệu gốc không commit. Tài liệu AI là bản dự thảo để nhóm kiểm tra và học; không phải minh chứng rằng thành viên đã nghiên cứu, lập trình hay đạt kết quả. Xem CONTRIBUTION_REPORT.md và docs/AI_USAGE.md.
