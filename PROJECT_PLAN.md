# Kế hoạch triển khai và các cổng nghiệm thu

Bắt đầu kế hoạch 26/11/2026. Bảo vệ theo tài liệu: 15/12/2026, nhóm 17 20:05–20:21; nộp 22/12/2026. Chưa xác nhận thông báo điều chỉnh từ lớp. Không đặt số giờ/ngày theo yêu cầu Trí; từng nhiệm vụ có ngày, người phụ trách, đầu ra và AC. Xem task_manifest.csv và hai file Word theo người.

| Milestone | Hạn | Phạm vi | Điều kiện qua cổng |
|---|---|---|---|
| M1 Research and Setup | 28/11 | P1 nghiên cứu; P3 repo; P4 Projects; P5 kế hoạch; P6 workflow | Hai người đọc, chốt mục tiêu/metric, dữ liệu có nguồn; repo Public và Project/Issue có quyền đóng góp phù hợp |
| M2 Design and Data | 30/11 | P2 kiến trúc; dữ liệu/EDA; bắt đầu P7 | Hợp đồng module, wireframe, kiểm kê và pipeline train-only |
| M3 Core and Validation | 04/12 | Logistic/PCA/LDA/metrics và kiểm chứng | Tests đối chiếu đạt; baseline có kế hoạch tuning; chưa cần tuyên bố kết quả thắng |
| M4 Experiments and Application | 10/12 | Quét k, baseline, cụm, calibration, 6 màn hình | Đủ record 25/cấu hình, thống kê, một mở rộng đầy đủ và app tích hợp |
| M5 Defense Readiness | 14/12 | P9 kiểm thử, báo cáo, slide, demo | Máy khác/offline, UX 3 người, báo cáo 15–25 trang, video, diễn tập |
| M6 Submission | 22/12 | Bảo vệ và hoàn thiện theo phản hồi thực | Bản nộp/Release đúng hiện vật, đủ minh chứng và tự thuật |

P8 theo dõi xuyên suốt; giai đoạn 3–6 chuẩn bị quản lý ngay từ những công việc nghiên cứu đầu, không chờ lập trình. Ngày kế hoạch không là ngày xác nhận hoàn thành.

Chi tiết bàn giao giữa hai người: [HANDOFFS.md](docs/HANDOFFS.md). Các phụ thuộc trong 54 nhiệm vụ đã được rà soát và đồng bộ; công việc giao diện có thể làm khung trước rồi tích hợp khi có mô hình/kết quả thật.

## Phụ thuộc và đường găng

Chốt giao thức → nạp/tiền xử lý → thuật toán/test → quét k/baseline → thống kê/mở rộng → đóng gói/bảo vệ. Song song: Trí thiết kế giao diện và API sau khi có hợp đồng; Luân viết công thức/thuật toán; Trí làm cụm khi có PCA; Luân làm calibration khi có xác suất. Bàn giao sớm bản nhỏ end-to-end, không đợi quét hết k mới tích hợp app.

Nếu trễ: ghi Blocked và tác động vào Issue; Trí điều phối và quyết định phương án; Luân góp ý khi được yêu cầu. Có thể bỏ trang trí và cấu hình ngoài yêu cầu; không bỏ thuật toán tự viết, tests, baseline, giao thức 25 lần đo, mở rộng hoặc 6 màn hình. Nếu không đủ năng lực/thời gian thì báo giảng viên bằng thông tin thật, không bịa tiến độ.
