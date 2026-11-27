# Bàn giao và phụ thuộc giữa Trí và Luân

Rà soát ngày 27/11/2026. Phụ thuộc là đầu vào để nghiệm thu phần tích hợp. Hai người vẫn có thể học, làm ví dụ nhỏ hoặc dựng khung giao diện song song. Ngày là mốc kế hoạch; khi đầu vào có sớm được bắt đầu sớm. Nếu thiếu đầu vào, ghi Blocked và phần đang chờ; không tạo dự đoán/kết quả giả.

| Bàn giao | Người cung cấp | Người tiếp nhận và nhiệm vụ | Đầu vào tối thiểu |
|---|---|---|---|
| Đề và dữ liệu | Trí | Luân nghiên cứu DA01-004/006/008 | PDF gốc, CSV, từ điển, hash/kiểm kê; hiện đã có |
| Giao thức | Luân soạn, hai người chốt | Trí/Luân làm DA01-007/008/016 | Split/seed/metric, tuning/ngưỡng, chống rò rỉ |
| Tiền xử lý | Trí | Luân làm DA01-010/016/018/020 | Train-only fit/transform, thứ tự cột, tests, cách lưu/nạp |
| Logistic | Luân | Trí làm DA01-013/015 | predict_proba, bản chạy được và hiện vật; baseline tích hợp bổ sung sau |
| PCA và LDA | Luân | Trí làm DA01-017/019/023 | Hướng chiếu, variance/loadings và tests; gom cụm dùng PCA, không nhìn nhãn khi fit |
| Metrics và runner | Luân | Hai người làm DA01-017/018/020 | Định nghĩa PR-AUC, 25 split và schema CSV kết quả |
| Kết quả chính | Luân | Trí làm DA01-021/023/027 | CSV từng fold, mean/std, config/seed/threshold thật |
| Calibration/chi phí | Luân | Trí làm DA01-025/027 | PAVA đã test để tích hợp sớm; kết quả DA01-026 trước nghiệm thu đủ |
| App và hình/bảng | Trí | Luân và cả nhóm làm DA01-029/033/034/037 | Chuỗi inference đúng, hình truy về results, trạng thái lỗi rõ |
| Báo cáo và gói nộp | Cả hai | Người còn lại review DA01-033…054 | Số liệu thật, kiểm thử/máy khác/offline, minh chứng/tự thuật |

## Cách làm song song

Trí thiết kế wireframe/API và tiền xử lý trong lúc Luân học công thức, viết loss/gradient bằng ví dụ nhỏ. Luân có thể tự viết PCA/LDA trước khi Logistic hoàn chỉnh; chạy thí nghiệm thật cần bộ tiền xử lý và giao thức chung. UI được dựng trước kết quả, nhưng phải ghi chưa có mô hình/số liệu thay vì trả dự đoán giả.

Task màn dự đoán đầu tiên DA01-013 có thể nối Logistic trước; đến DA01-027 phải có đủ lựa chọn baseline/tự viết/thư viện/giảm chiều theo đề. Khung UI chưa đồng nghĩa nghiệm thu đầy đủ chức năng.

## Hợp đồng cần chốt trước mã nguồn

X là ma trận số, y là stroke tách riêng, không đưa id/stroke vào đặc trưng. Preprocessor có fit/transform/feature_names/lưu-nạp. Classifier chỉ rõ xác suất lớp1 và trạng thái hiệu chuẩn; threshold tách khỏi PR-AUC. Kết quả có config_id, seed, fold, k, metrics, threshold và thời gian. Mỗi PR được người còn lại review, kể cả PR của Trí.

Phụ thuộc đã đồng bộ trong [CSV](tasks/task_manifest.csv), các Issue dự thảo, Markdown và hai Word cá nhân. Nếu đã tạo Issue trên GitHub, cập nhật body theo file dự thảo; script nhập hiện chỉ tránh tạo trùng, không tự sửa Issue cũ.
