# Yêu cầu hệ thống và nghiệm thu

Yêu cầu lấy từ DA-01 trang 9–17 tài liệu 07 và hướng dẫn 07b. Các đề xuất tổ chức trong docs/ chưa thay thế yêu cầu giảng viên.

| ID | Yêu cầu | Bằng chứng nghiệm thu |
|---|---|---|
| R01 | Đúng dữ liệu chỉ định; kiểm kê thực tế | Bảng dòng/cột/thiếu/trùng/lớp, nguồn và thời điểm tải |
| R02 | Ít nhất 6 biểu đồ EDA khác loại | Hình có nhãn/đơn vị, nhận xét, phân tích cột phân loại/BMI |
| R03 | Tiền xử lý không rò rỉ | Fit trong fold train, có test chứng minh |
| R04 | Logistic trọng số tự viết | Loss/gradient/L2/GD; test xác suất so thư viện sai lệch trung bình < 1e-3 khi khớp mục tiêu tối ưu |
| R05 | PCA và LDA tự viết | PCA qua SVD có inverse; kiểm chứng PCA và hướng LDA theo đề |
| R06 | Metrics tự viết | Precision/recall/F1, PR-AUC hình thang; test đồng điểm và trường hợp biên |
| R07 | Baseline đầy đủ | Đoán âm; Logistic không trọng số; Logistic balanced sklearn; Random Forest có tinh chỉnh |
| R08 | Giao thức DA-01 | 5-fold phân tầng × 5 lần, cùng bộ chia, PR-AUC chính; 25 giá trị/cấu hình |
| R09 | Khảo sát giảm chiều | k = 2…d, variance 80/90/95%, F1/PR-AUC theo k, PCA 2D/LDA 1D |
| R10 | Thống kê và ngưỡng | Trung bình ± std; Wilcoxon ghép cặp; PR curve/confusion matrix; mô tả cách chọn ngưỡng |
| R11 | Gom cụm đối chứng | Không dùng stroke khi fit; bảng kích thước, tỷ lệ stroke và hồ sơ cụm |
| R12 | Một hướng mở rộng đầy đủ | Dự kiến calibration/chi phí: PAVA/Brier/reliability/threshold tự viết, ≥3 k, tỷ số chi phí 5–100 |
| R13 | Ví dụ tính tay | 6 bệnh nhân × 2 biến, 3 dương/3 âm, PCA và LDA đủ phép tính |
| R14 | Ứng dụng 6 màn hình | Tổng quan, dự đoán, train nhỏ, giảm chiều, so sánh, ngưỡng cảnh báo |
| R15 | Báo cáo và hồ sơ | 15–25 trang, ≥3 tài liệu/≥1 tiếng Anh, slide, biên bản, tự thuật, khai báo AI |

## Chức năng và phi chức năng của ứng dụng

Màn 1: kiểm kê qua API, dữ liệu mẫu train, nguồn và câu hỏi. Màn 2: nhập/chọn mẫu, chọn baseline/tự viết/sklearn/giảm chiều, xác suất và thời gian suy luận. Màn 3: train cấu hình nhỏ tối đa 5.000 dòng và dưới 30 giây, chạy nền, có tiến độ/dừng/metrics. Màn 4: k, variance, hiệu năng, loadings, PCA/LDA. Màn 5: số liệu results/ có sai số và tải CSV. Màn 6: slider ngưỡng, FN/FP, ma trận và hai hình chiếu đồng bộ.

- N01: chạy CPU cục bộ; không cần cloud để bảo vệ.
- N02: inference dùng hiện vật đã lưu; không huấn luyện đồng bộ trong request.
- N03: toàn bộ thư viện biểu đồ lưu cục bộ; thử không mạng; README ba lệnh có gói phụ thuộc offline.
- N04: màn hình 1920px/768px; trạng thái tải/thành công/lỗi; không alert(); tương phản ≥4,5:1 và không chỉ dùng màu.
- N05: hình có tiêu đề/trục/đơn vị phù hợp; số liệu có provenance; không làm giả chuyển động PC1/PC2 khi tăng k.
- N06: API trực quan trả dưới 5.000 điểm; hình báo cáo toàn dữ liệu có thể tạo offline. Thử UX với 3 người, ghi 3 vấn đề và sửa.
- N07: không commit secret/dữ liệu thô; không lưu hồ sơ bệnh nhân do người dùng nhập trong bản demo.
- N08: app import mã gốc, không nhân bản thuật toán; có tái lập, phiên bản, seed, unit/integration tests cần thiết.

## Ngoài phạm vi

Deep learning; bệnh án thật; dự báo thời điểm đột quỵ tương lai; chẩn đoán lâm sàng; tài khoản, thanh toán, cloud, mobile. Dataset có nhãn đột quỵ, không tự chứng minh giá trị tiên lượng tương lai.
