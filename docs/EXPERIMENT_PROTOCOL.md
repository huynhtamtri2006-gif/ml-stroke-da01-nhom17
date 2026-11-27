# Giao thức thực nghiệm dự thảo trước lần chạy đầu

## Phân chia và chống rò rỉ

Giữ riêng 20% phân tầng làm test cuối. Trên 80% phát triển, tạo 5 lần lặp, mỗi lần 5-fold phân tầng; lưu seed 20262027…20262031 và chỉ số mẫu của 25 cặp train/evaluation. Đây là cách đề xuất kết hợp yêu cầu 80/20 và giao thức riêng DA-01, cần nhóm chốt trước chạy.

Schema one-hot phải được thống nhất trước chạy để cùng k có ý nghĩa trên mọi fold. Có thể khai báo các mức từ mô tả nguồn đã chốt, không suy ra từ tập đánh giá; hoặc có quy tắc train-only và giới hạn k hợp lệ được báo cáo rõ. Mức Other chỉ có một mẫu, có thể không xuất hiện trong train của một fold; không fit encoder toàn CSV để chữa sự khác nhau số cột. Nếu dùng schema cố định, cột zero/phụ thuộc tuyến tính phải được xử lý đúng trong PCA/LDA và kiểm thử.

Mỗi outer fold: fit toàn bộ imputation/encoder/scaler/PCA hoặc LDA chỉ trên outer train. Nếu cần tuning, dùng inner split/CV trong outer train; chọn C/lambda, RF params, class weights và ngưỡng ở trong. Không chọn siêu tham số từ outer evaluation rồi báo nó là hiệu năng độc lập. Dùng cùng outer fold để so cấu hình; ngân sách tuning tương đương.

Quét từng k là khảo sát cấu hình; kết luận mô hình k tốt nhất phải dựa thêm test cuối chưa mở hoặc lựa chọn k bên trong inner CV. Test cuối không được dùng để chọn ngưỡng, hiệu chuẩn hay chỉnh màu/quy tắc theo hiệu năng.

## Hiệu chuẩn và ngưỡng

Trong outer train, tách phần fit mô hình, calibration và threshold-validation; tất cả phân tầng. Bộ tiền xử lý và mô hình chỉ fit trên phần fit tương ứng, PAVA fit trên calibration, chọn ngưỡng bằng threshold-validation. Outer evaluation chỉ đánh giá chuỗi đã khóa. Phân chia này giảm số ca dương mỗi phần, nên báo kích thước và biến thiên. Nếu dùng cross-fitting để tận dụng dữ liệu, phải thiết kế và kiểm thử rõ trước, không tự thay đổi giữa chừng.

## Độ đo và cách báo cáo

PR-AUC hình thang là chính theo đề, đầu vào là điểm số/xác suất liên tục, không phải nhãn 0/1. Precision/recall/F1 phụ thuộc ngưỡng; AP là cột khác. Xử lý nhóm điểm số bằng nhau trước tính PR; bảo đảm thứ tự recall khi tích phân. Baseline score hằng có PR-AUC hình thang phụ thuộc quy ước điểm đầu/cuối; không khẳng định nó luôn bằng tỷ lệ dương. Tỷ lệ dương là đường tham chiếu no-skill và baseline AP khi score hằng.

Lưu config_id, seed, fold, k, metric, thời gian, số mẫu dương/âm, threshold, phiên bản/seed/hash input. Báo mean ± sample std trên 25 giá trị; 20% test cuối là kết quả riêng, không gắn nhầm std của CV vào nó.

Wilcoxon ghép cặp trên cùng 25 fold theo đề; đặt alpha trước (đề xuất 0.05). Nêu rõ fold CV có tương quan, p-value có giới hạn diễn giải. Nếu so nhiều cặp, dùng hiệu chỉnh phù hợp như Holm, báo cả chênh lệch và p-value; không chọn riêng cặp có lợi. Không khác biệt có ý nghĩa thì ghi chưa đủ bằng chứng phân biệt.

## Cấu hình tối thiểu

Đoán âm; Logistic không trọng số; Logistic trọng số tự viết full; PCA 2…d + Logistic trọng số; LDA 1D + Logistic trọng số; Logistic balanced sklearn; RF. Baseline/tuning ghi ở config. Khảo sát BMI trình bày riêng; nếu bỏ dòng làm đổi quần thể test, ghi rõ và tạo phép so trên mẫu chung phù hợp.

Gom cụm K-means trên PCA không nhìn stroke, thống kê nhãn sau. Chọn số cụm bằng tiêu chí không dùng nhãn. Phân tích toàn dữ liệu phải được gọi là mô tả, không là hiệu năng kiểm tra.

## Kiểm chứng thuật toán

Logistic: so cùng loss/normalization/class weights/L2/bias, gradient sai phân hữu hạn, xác suất MAE <1e-3 theo đề khi hội tụ. PCA: centering, variance, projection/reconstruction, xử lý dấu; phổ có trị riêng bằng nhau nên so không gian chiếu thay vì buộc một cơ sở duy nhất. LDA: cùng prior/định nghĩa scatter, cosine tuyệt đối ≥0.999 với quy ước khớp; xử lý hạng thiếu rõ ràng. Metrics: cùng quy tắc hình thang, ties và endpoint.

CSV và báo cáo kiểm kê đã có. Chưa có kết quả mô hình, p-value hoặc cấu hình thắng; mọi giá trị đánh giá sau này phải được sinh bằng chương trình và liên kết hiện vật gốc. Protocol này vẫn là thiết kế cần hai thành viên xác nhận trước lần chạy đầu, không phải bằng chứng CV đã thực hiện.
