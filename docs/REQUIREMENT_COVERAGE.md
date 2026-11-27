# Đối chiếu yêu cầu DA-01 với kế hoạch

Căn cứ [PDF gốc](specifications/README.md), rà soát 27/11/2026. Bảng này xác nhận độ bao phủ của kế hoạch, không xác nhận thuật toán/thực nghiệm đã làm xong. Rubric chính thức trong tài liệu03/11 chưa được cung cấp để đối chiếu riêng.

| Yêu cầu | Căn cứ | Tài liệu/nhiệm vụ | Trạng thái |
|---|---|---|---|
| Nhóm17 làm DA-01 | 07 tr4 | README/TEAM_MEMBERS | Đã đối chiếu; phân công2 người không tự đổi danh sách lớp3 người |
| CSV5110×12, 249 dương, 201 BMI thiếu | 07 tr9,14 | R01, data/, DA01-005 | Có CSV, kiểm kê/hash; raw được Git theo dõi |
| ≥6 biểu đồ khác loại, nhãn/đơn vị/nhận xét | 07 tr14–15 | R02, DA01-009 | Kế hoạch; chưa có EDA |
| Tiền xử lý/chia không rò rỉ | 07 tr11,15; 07b tr7–8,22 | R03/R08, protocol, DA01-004/007/009/016 | Có thiết kế, chưa có split/transformer |
| Logistic trọng số/L2/GD tự viết và đối chiếu | 07 tr10,15 | R04, DA01-008/010 | Chưa triển khai |
| PCA SVD/dựng ngược; LDA S_W/S_B/Fisher và tests | 07 tr10,15–16 | R05, DA01-012/014 | Chưa triển khai |
| Precision/recall/F1/PR-AUC hình thang tự viết | 07 tr10 | R06, DA01-016 | Có quy ước, AP ghi riêng |
| Đủ baseline, tinh chỉnh nghiêm túc | 07 tr10 | R07, DA01-018/020 | Kế hoạch |
| 5-fold phân tầng×5 =25 đo/cấu hình | 07 tr11 | R08/R10, DA01-016/020/022 | Dùng yêu cầu riêng DA-01, không giảm còn5 |
| k2…d, variance80/90/95, F1/PR-AUC theo k | 07 tr10,16 | R09, DA01-012/017/020/022 | Kế hoạch |
| PCA2D/LDA1D, lớp hiếm, phân tích hướng bị loại | 07 tr10,13,16 | R09, DA01-017/022/028 | Kết luận phải đo thực tế |
| Mean±std/Wilcoxon/PR curve/ngưỡng/confusion matrix | 07 tr11 | R10, DA01-016/020/022/023 | Kế hoạch |
| Gom cụm và tỷ lệ stroke từng cụm | 07 tr9,13,16 | R11, DA01-019 | K-means được dùng thư viện, không nhìn nhãn khi fit |
| Một mở rộng đầy đủ | 07 tr11–12 | R12, DA01-024/026/028 | Chọn chiều sâu: PAVA/Brier/reliability/threshold tự viết, ≥3 k, chi phí5–100; học Platt/isotonic |
| So cách xử lý BMI thiếu | 07 tr13,16 | DA01-007/021/027 | Có nhận xét40 ca dương thiếu BMI; chưa chạy so sánh |
| Ví dụ tay6 bệnh nhân,2 biến,3 dương/3 âm | 07 tr12–13 | R13, DA01-032/033 | Phải dùng age/avg_glucose_level chuẩn hóa, covariance/eigen/projection và LDA |
| 5 màn chung + màn ngưỡng riêng DA-01 | 07 tr17;07b tr11–18 | R14/N01…N08; DA01-003/011/013/015/017/021/023/025/027/029 | Có đặc tả; chưa có wireframe/app |
| Ba lệnh tái lập, offline, JS cục bộ, UX3 người | 07b tr15–18,22,25 | DA01-029/031/035/036 | Nghiệm thu ở giai đoạn phát triển |
| Word15–25 trang, slide13 phút, ≥3 nguồn/≥1 tiếng Anh | 07b tr21,25 | R15, DA01-031…038 | Có nguồn/kế hoạch, chưa có báo cáo kết quả |
| ≥2 biên bản, tự thuật, đóng góp, khai báo AI | 07b tr4,25 | R15, DA01-045…048 và nhật ký | Có mẫu, không tạo thành tích giả |

## Điểm cần diễn giải khi thực hiện

- Đề yêu cầu PR-AUC hình thang nhưng dẫn average_precision_score: dùng PR-AUC chính, AP riêng, không ép bằng nhau.
- Đoạn chung ghi≥5 lần, DA-01 ghi25: dùng25.
- Có đoạn nêu3 cách BMI, đoạn cuối yêu cầu bảng4: kế hoạch thêm trung vị kèm cờ thiếu; ghi rõ quần thể test khi so phương án bỏ dòng.
- Nhóm BMI khuyết không có BMI gốc để vẽ boxplot: thể hiện missing hoặc phân bố age/glucose theo cờ thiếu; nếu vẽ sau điền phải ghi rõ, không bịa BMI gốc.
- Không viết sẵn LDA chắc chắn thắng hoặc Logistic không trọng số luôn đoán âm: kết luận theo kết quả thật.
- Lịch trong PDF: bảo vệ15/12, nộp22/12; kiểm tra thông báo lớp nếu có điều chỉnh. Nhiệm vụ robot theo08/08b là phần riêng chưa được cung cấp.
