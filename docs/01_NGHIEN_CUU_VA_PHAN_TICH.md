# Nghiên cứu và phân tích đề tài DA-01

## Mục tiêu và phạm vi

Vấn đề: lớp stroke = 1 chỉ có 249/5.110 mẫu theo đề. Accuracy có thể cao khi bỏ sót mọi ca dương. Mục tiêu là đánh giá tác động của PCA đối với khả năng phát hiện lớp hiếm; so với LDA và dữ liệu không giảm chiều. PR-AUC hình thang là độ đo chính dự kiến theo đề; phải được nhóm xác nhận trước lần chạy đầu.

Câu hỏi: (1) k nào bắt đầu làm giảm PR-AUC/recall? (2) phương sai tích lũy có phản ánh mức giữ tín hiệu lớp hiếm không? (3) LDA 1D so với PCA ra sao? (4) xử lý BMI thiếu thay đổi kết quả thế nào? (5) hiệu chuẩn và chi phí ảnh hưởng ngưỡng cảnh báo thế nào?

Đầu ra là bằng chứng thực nghiệm tái lập và ứng dụng nghiên cứu; không đặt mục tiêu một tỷ lệ accuracy hay PR-AUC trước khi chạy.

## Tính khả thi đối với hai sinh viên

Dữ liệu bảng nhỏ theo kích thước đề; thuật toán tuyến tính và SVD không đòi GPU. Đây là đánh giá sơ bộ, chưa đo máy. Khó khăn chính là kiến thức toán, khớp mục tiêu tối ưu khi đối chiếu, chặn rò rỉ và khối lượng tích hợp. Từ 26/11 đến lịch bảo vệ 15/12/2026 chỉ còn 19 ngày. Bắt đầu từ số 0 là rủi ro tiến độ cao; không thể cam kết đạt mọi mốc trước khi biết tốc độ học và chạy thử.

Giữ một hướng mở rộng chiều sâu đầy đủ; không làm thêm dịch vụ cloud. Xây một luồng nhỏ end-to-end sau khi chốt thiết kế rồi mở rộng từng phần. Không giảm số lần đo hoặc bỏ tests để chạy theo hình thức.

## Phân tích các phương pháp

| Phương pháp | Giá trị | Hạn chế và vai trò |
|---|---|---|
| Đoán âm | Cho mốc recall = 0 để phân tích accuracy | Không là mô hình hữu ích; bắt buộc đối chứng |
| Logistic không trọng số | Đo ảnh hưởng của trọng số lớp | Có thể ưu tiên lớp đa số; không mặc định luôn đoán âm |
| Logistic có trọng số | Lõi dễ diễn giải, tự viết theo đề | Điểm số chưa chắc là xác suất đã hiệu chuẩn |
| PCA | Chiếu không dùng nhãn, nén phương sai | Có thể mất tín hiệu lớp hiếm; phải quét k |
| LDA Fisher | Dùng nhãn tìm hướng phân biệt; nhị phân tối đa 1D | Không bảo đảm thắng; one-hot có thể gây suy biến |
| Random Forest | Mốc phi tuyến mạnh | Phải tinh chỉnh công bằng, không thay lõi tự viết |
| K-means trên PCA | Mô tả nhóm hồ sơ không dùng nhãn | Cụm hình học không tự đồng nghĩa nhóm nguy cơ |
| Isotonic/PAVA và chi phí | Mở rộng nối nghiên cứu với ngưỡng | Ít ca dương có thể làm hiệu chuẩn bất ổn; cần tập riêng |

Hướng tiếp cận đề xuất: Logistic trọng số tự viết → đối chiếu đúng hàm mục tiêu → PCA/LDA tự viết → cùng fold để quét k và baseline → gom cụm → hiệu chuẩn/chi phí → ứng dụng đọc hiện vật và kết quả. Thư viện bản tương ứng chỉ mở để đối chiếu sau khi tự viết hoạt động, theo hướng dẫn giảng viên.

## Đầu vào và thu thập dữ liệu

Stroke Prediction Dataset: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset . Tải bằng tài khoản cá nhân nếu nguồn yêu cầu. Không đưa kaggle.json lên repo. Ghi URL, thời điểm tải, tên tệp, SHA-256, điều khoản sử dụng/giấy phép đang hiển thị, số dòng/cột thực tế. Cập nhật 27/11: Trí đã chuẩn bị CSV và kiểm kê, file đã được đưa vào repo theo yêu cầu của Trí; License nguồn do Trí cung cấp là Data files © Original Authors. Thông tin nguồn/bản quyền và hash được giữ ở data/PROVENANCE.md, không tự gán giấy phép mở khác cho CSV.

12 cột theo đề gồm id, 10 biến đầu vào và stroke; bỏ id. Năm biến phân loại: gender, ever_married, work_type, Residence_type, smoking_status. Ba biến liên tục: age, avg_glucose_level, bmi. Hai biến nhị phân: hypertension, heart_disease. BMI thiếu 201 ô theo đề. Cần kiểm kê trùng và quyết định Unknown là nhóm riêng hay missing; khởi đầu giữ nhóm riêng và giải trình.

Kiểm kê/EDA mô tả có thể toàn dữ liệu và phải ghi phạm vi; để không dùng tập cuối khi lựa chọn thiết kế, thực hiện EDA định hướng mô hình trên phần phát triển sau split. Biểu đồ toàn bộ 249 ca trong đề là mô tả dữ liệu, không là bằng chứng hiệu năng ngoài mẫu.

## Kết quả đầu ra

CSV/NPZ từng fold và tổng hợp; biểu đồ variance/F1/PR-AUC theo k; PCA/LDA; baseline; thống kê Wilcoxon; bảng cụm; hiệu chuẩn/chi phí; mô hình và tiền xử lý lưu cùng metadata; tests/; 6 màn hình; báo cáo Word 15–25 trang; slide, video, README và minh chứng thật.

## Kiến thức cần học và bằng chứng học tập

| Người | Kiến thức ưu tiên | Bài tập tự làm và bàn giao |
|---|---|---|
| Trí | Python/pandas, missing/one-hot/scaling, train/test, Git/Issue/PR | Giải thích vì sao fit chỉ trên train; kiểm kê CSV; một Issue nghiên cứu có nguồn và ví dụ tự viết |
| Trí | HTTP/JSON/FastAPI, HTML/CSS/JS, canvas, async job, validation | Vẽ 6 wireframe; mô tả request/response và chuỗi inference; sau thiết kế mới code |
| Luân | Vector/ma trận, đạo hàm, sigmoid/log-loss, gradient descent, L2 | Tự suy diễn gradient và kiểm tra bằng sai phân hữu hạn |
| Luân | SVD/PCA, Fisher LDA, ma trận suy biến | Tính tay ví dụ 6 điểm; giải thích Vt và centering |
| Luân | PR metrics, CV, thống kê, calibration/PAVA, Brier và chi phí | Phân biệt AP/PR-AUC; vẽ tay PR toy data; kế hoạch fold và calibration |
| Cả hai | Git cá nhân, giấy phép, provenance, tái lập, chống rò rỉ | Review chéo; ghi nguồn thực sự đọc, không chép repo |

Không cần học trọn một khóa trước khi làm: đọc đúng phần, giải bài nhỏ, ghi điều đã hiểu/chưa hiểu và điều vận dụng. Danh sách nguồn và thứ tự nằm ở SOURCES.md.

## Rủi ro và biện pháp

| Rủi ro | Dấu hiệu | Biện pháp và phụ trách |
|---|---|---|
| Thiếu thời gian | Mốc thuật toán bị trễ | Trí rà hằng ngày; giảm trang trí/cấu hình bổ sung, không bỏ yêu cầu lõi; trao đổi giảng viên khi cần |
| Rò rỉ | Fit trước split, chọn ngưỡng trên test | Luân thiết kế fold; Trí review Pipeline và test train-only |
| Ít ca dương | Recall dao động mạnh | Phân tầng; 25 lần đo; báo std và số mẫu, không giấu kết quả xấu |
| Logistic không khớp | Xác suất lệch thư viện | Khớp loss/weights/L2/bias; kiểm tra gradient và hội tụ |
| LDA suy biến | Solve lỗi hoặc hướng bất ổn | Kiểm tra rank; pinv/lstsq có giải trình; cùng quy ước với đối chiếu |
| Nhầm AP/PR-AUC | Tự viết không khớp average_precision_score | Tách hai chỉ số; đối chiếu PR-AUC bằng cùng quy tắc hình thang |
| Hiệu chuẩn quá khớp | Brier kém trên fold ngoài | Calibration tách riêng, kiểm tra đủ số ca dương, báo biến thiên |
| Mất mạng | Biểu đồ trắng/cài không được | Trí lưu JS và wheels cục bộ; kiểm tra máy khác không mạng |
| Công đóng góp sai | Commit hộ, cập nhật Done không có minh chứng | Tài khoản cá nhân, Issue/PR/link kết quả; Trí tự kiểm tra phần mình, review phần Luân và quyết định nghiệm thu; giữ đầy đủ minh chứng |
| Quyền GitHub | Chưa mời Luân, thiếu username | Ghi pending; không giả vờ đã gán Issue hoặc tạo Project |

## Những điểm cần thống nhất trước lập trình

1. PR-AUC hình thang là chính, AP phụ và tên cột khác nhau. Tài liệu chính thức xác nhận hai cách không tương đương: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html .
2. Kết hợp 80/20 với CV 5×5 như EXPERIMENT_PROTOCOL.md; tham số/ngưỡng dùng inner validation, test cuối chỉ mở sau khi khóa quyết định.
3. Cấu hình ban đầu: numeric continuous chuẩn hóa; one-hot và hai nhị phân giữ 0/1, PCA có centering; giải trình và khảo sát khi cần, không mặc định chuẩn hóa mọi dummy hiếm.
4. Một đoạn đề nêu ba cách BMI, đoạn sau yêu cầu bảng bốn cách: dự kiến thêm cờ missing thành phương án thứ tư; tránh so hiệu năng trên các test set khác nhau mà không nêu rõ.
5. LDA có nhìn nhãn: không dùng để gọi gom cụm là hoàn toàn không giám sát. Không viết sẵn LDA chắc thắng PCA.
6. Mốc và danh sách chính thức cần kiểm tra thông báo lớp; nhiệm vụ robot theo 08/08b nằm ngoài hai file đã có.

## Tiêu chí kết thúc giai đoạn 1

Hai người tự đọc ít nhất phần cốt lõi; có tóm tắt bằng lời của mình; xác nhận câu hỏi/metric/phạm vi; kiểm tra nguồn dữ liệu; ghi quyết định và rủi ro; chốt trách nhiệm; mở Issue nghiên cứu đầu tiên. Bản phân tích có AI hỗ trợ. CSV, kiểm kê và repository đã có; việc hai thành viên đọc, tự tóm tắt và chốt quyết định chưa tự được đánh dấu hoàn tất. Đề gốc nằm trong docs/specifications/ để đối chiếu.

Tham khảo học thuật: [Saito và Rehmsmeier 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118432) là bài đọc bắt buộc theo đề về đánh giá dữ liệu mất cân bằng. Không suy ra từ bài này rằng một mô hình cụ thể của nhóm sẽ đạt kết quả tốt.
