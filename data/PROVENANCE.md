# Hồ sơ nguồn dữ liệu

## Nguồn bắt buộc

- Tên bộ dữ liệu: Stroke Prediction Dataset.
- Người đăng trên Kaggle theo URL của đề: fedesoriano.
- Trang nguồn: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset .
- File chỉ định: healthcare-dataset-stroke-data.csv.
- Bản gốc trong dự án: data/raw/healthcare-dataset-stroke-data.csv.

## Trạng thái ngày 27/11/2026

Trí đã đặt CSV vào thư mục raw và chạy công cụ kiểm kê. AI đã đọc báo cáo và kiểm tra lại SHA-256 của file cục bộ: trùng với báo cáo, không có chênh lệch ở năm đại lượng đối chiếu. Kết nối tự động của AI đến Kaggle trước đó trả HTTP 404; thông tin nguồn tải và License dưới đây được ghi theo xác nhận của Trí trong cuộc trao đổi, không phải metadata AI tải được từ Kaggle.

## Điền sau khi tải bằng trình duyệt

| Thông tin | Giá trị thực tế |
|---|---|
| Người chuẩn bị và chạy kiểm kê | Huỳnh Tâm Trí, theo thao tác và kết quả cung cấp trong cuộc trao đổi |
| Thời điểm tải chính xác | Chưa ghi nhận; file đã có khi kiểm kê ngày 27/11/2026 |
| Trang nguồn được Trí sử dụng theo hướng dẫn | https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset |
| Phiên bản dataset nếu có | Chưa ghi nhận |
| License trên Data Card do Trí cung cấp | Data files © Original Authors |
| Mã loại trong danh sách License của Kaggle | copyright-authors |
| Quyền chia sẻ lại CSV vào repository | Chưa xác nhận từ điều khoản cụ thể; giữ raw ngoài Git |
| CSV có được chỉnh sửa trước khi tải vào dự án không | Chưa có thông tin bổ sung; công cụ không sửa CSV |
| SHA-256 đo từ file cục bộ | 644d473b05d2797006bd94865e4f8bb057f0c721617911613c82c8fcfc707420 |
| Kích thước file | 316.971 bytes |
| Thời điểm báo cáo kiểm kê | 27/11/2026 12:46:37, Asia/Bangkok (05:46:37 UTC) |
| Báo cáo kiểm kê | [inventory.md](inventory/inventory.md), [inventory.json](inventory/inventory.json) |

Không điền tên Trí hoặc Luân vào mục Người tải nếu người đó chưa thực hiện. Không dùng giấy phép mã của một repo khác thay giấy phép dataset, không coi nhãn Private tự tạo quyền chia sẻ dữ liệu.

Danh sách chính thức của Kaggle ghi `copyright-authors` tương ứng “Data files © Original Authors”: https://github.com/Kaggle/kaggle-cli/blob/main/docs/datasets_metadata.md#licenses . Dòng này chưa cung cấp ở đây các điều kiện cho phép tái phân phối; không tự gán CC0 hoặc CC BY cho CSV.

Thông tin máy đọc được và hash tham chiếu nằm trong [dataset_reference.json](dataset_reference.json) và [SHA256SUMS](SHA256SUMS). Hash giúp đối chiếu hai bản file; không tự chứng minh nguồn gốc hoặc giấy phép.

## Chia sẻ cho thành viên clone

Mục tiêu là có bản dữ liệu nhất quán trên hai máy. Khi xác nhận điều kiện nguồn cho phép chia sẻ CSV trong repo nhóm, thêm đúng một ngoại lệ .gitignore cho file được chỉ định, giữ ghi nguồn/điều kiện và SHA-256. Không bỏ toàn bộ quy tắc loại trừ raw hoặc dùng git add -f để bỏ qua kiểm tra.

Nếu chưa xác nhận được điều kiện, giữ CSV ở máy; hai người tải từ cùng nguồn và đối chiếu SHA-256. Nhóm vẫn có thể commit từ điển dữ liệu, hướng dẫn và báo cáo tổng hợp; clone chưa tự mang theo raw trong trường hợp này.
