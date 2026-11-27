# Bắt đầu phân tích khi đã có dữ liệu

## Việc đã chuẩn bị

Từ điển cột ở data/DATA_DICTIONARY.md; hồ sơ nguồn ở data/PROVENANCE.md; công cụ kiểm kê data/kiem_ke.py. Công cụ chỉ dùng thư viện chuẩn Python, không cần pandas, không huấn luyện mô hình, không sửa CSV, không tự điền ô thiếu.

## 1. Đặt CSV đúng vị trí

Từ trang Kaggle được chỉ định, tải và giải nén. Đặt healthcare-dataset-stroke-data.csv vào data/raw/. Không đổi sang bộ synthetic/competition có tên gần giống. Không dùng bản đã oversample hoặc làm sạch sẵn; giữ nguyên nhãn và giá trị N/A.

## 2. Chạy kiểm kê từ thư mục gốc

```powershell
python data/kiem_ke.py
```

Hai file inventory.md và inventory.json được tạo trong data/inventory/ khi schema hợp lệ. Exit code 0: các số đối chiếu khớp; 1: thiếu file hoặc lỗi định dạng; 2: đã kiểm kê nhưng số lượng khác đề, cần giải trình. Không sửa CSV cho khớp số đề.

Đọc báo cáo để biết kích thước, nhãn, missing, bản ghi trùng/id trùng, các mức phân loại, thống kê min/median/max, BMI thiếu theo nhãn và SHA-256. Các thống kê này mô tả toàn CSV, không được lấy làm tham số điền khuyết/chuẩn hóa trước khi chia dữ liệu.

## 3. Trí và Luân cùng xác nhận

| Trí | Luân | Sản phẩm chung |
|---|---|---|
| Ghi nguồn/giấy phép/ngày tải, kiểm kê kiểu/missing/trùng | Kiểm tra nhãn, tỷ lệ dương, phân biệt PR-AUC và accuracy | Hồ sơ nguồn + báo cáo kiểm kê có review |
| Đề xuất xử lý BMI và Unknown; giải thích lựa chọn | Review nguy cơ leakage, seed, phân tầng và ngưỡng | Quyết định tiền xử lý và giao thức trước chạy mô hình |
| Chuẩn bị biểu đồ EDA sau khi chốt phạm vi | Chuẩn bị lý thuyết Logistic/PCA/LDA và ví dụ tính tay | Nhật ký nguồn đã đọc và câu hỏi còn vướng |

## 4. Câu hỏi phân tích đầu tiên

1. Số mẫu thực có đúng đề không? Chênh lệch nằm ở đâu?
2. Đoán tất cả là 0 cho accuracy và recall dương thế nào?
3. BMI thiếu ở hai lớp có tỷ lệ khác nhau không? Nếu bỏ dòng thì mất bao nhiêu ca dương?
4. Unknown có bao nhiêu mẫu? Vì sao không gộp nó vào never smoked?
5. Các mức hiếm như Other có đủ mẫu để kết luận theo nhóm không?
6. Tuổi/đường huyết/BMI có lệch, ngoại lệ hoặc liên hệ đáng chú ý không?
7. One-hot dự kiến tạo bao nhiêu chiều, thang đo ảnh hưởng PCA thế nào?
8. Có cột hoặc thao tác nào vô tình đưa nhãn/thống kê test vào mô hình không?

EDA mô tả toàn bộ dữ liệu phải ghi rõ; EDA định hướng mô hình nên dựa trên phần phát triển sau split, giữ test cuối ngoài lựa chọn thiết kế. Không vẽ dữ liệu giả như kết quả thật.

## 5. Thứ tự triển khai tiếp

Đọc REQUIREMENTS.md và EXPERIMENT_PROTOCOL.md → chốt split/metric → viết bộ nạp/tiền xử lý train-only → kiểm thử → tự viết thuật toán từng phần → đối chiếu → thí nghiệm. Chưa chạy lệnh cài requirements.txt hoặc train/app vì các thành phần đó chưa có.

## 6. Clone để dùng chung

Một lần chuẩn bị CSV hợp lệ và điều kiện chia sẻ: Trí bổ sung đúng file raw được phép vào repo, commit kèm nguồn và kiểm kê, rồi push. Luân clone hoặc git pull --ff-only và chạy lại kiểm kê. So SHA-256 giữa hai máy; báo cáo khác thời điểm tạo là bình thường nhưng hash raw và các số thống kê phải giống.

Nếu CSV không được phép đưa vào repo hoặc điều kiện chưa rõ, người clone vẫn cần tải CSV riêng; không tuyên bố chỉ clone đã có toàn bộ dữ liệu. Đường dẫn là tương đối nên có thể dùng ở thư mục bất kỳ.
