# Dữ liệu phục vụ DA-01

Mục tiêu: hai thành viên sử dụng cùng CSV gốc, hiểu từng cột và có công cụ kiểm kê trước khi phân tích.

**Máy của Trí đã có CSV thật và báo cáo kiểm kê ngày 27/11/2026.** Số lượng khớp đề, hash đã đối chiếu. CSV chưa được theo dõi trong Git: người clone cần tải riêng theo các bước dưới. Xem [báo cáo kiểm kê](inventory/inventory.md), [hồ sơ nguồn](PROVENANCE.md) và [nhận xét ban đầu](../docs/INITIAL_DATA_FINDINGS.md).

## Lấy bộ dữ liệu chỉ định

1. Mở https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset .
2. Đăng nhập Kaggle nếu được yêu cầu. Đọc mục License và ghi vào [PROVENANCE.md](PROVENANCE.md); đây là điều kiện để quyết định có đưa CSV lên repo nhóm hay không.
3. Bấm Download, giải nén tệp nhận được, tìm đúng healthcare-dataset-stroke-data.csv.
4. Copy nguyên file vào data/raw/healthcare-dataset-stroke-data.csv. Không mở rồi lưu lại bằng Excel trước kiểm kê vì có thể đổi byte/định dạng.

License do Trí đọc từ trang nguồn: **Data files © Original Authors**. Chưa xác nhận điều kiện cho phép tái phân phối CSV vào repo; không đổi nó thành CC0/CC BY.

## Kiểm tra ngay

Mở PowerShell ở thư mục gốc dự án:

```powershell
python data/kiem_ke.py
```

Nếu máy chỉ dùng py launcher, có thể thay python bằng py. Không cần cài thư viện bổ sung. Báo cáo số liệu thật sẽ ở data/inventory/inventory.md và inventory.json. Công cụ không sửa raw, không fit model và không sinh dữ liệu giả thay dataset.

Đối chiếu SHA-256 trên máy Luân với bản tham chiếu của Trí:

```powershell
Get-FileHash 'data/raw/healthcare-dataset-stroke-data.csv' -Algorithm SHA256
```

Hash cần giống (không phân biệt hoa/thường): `644d473b05d2797006bd94865e4f8bb057f0c721617911613c82c8fcfc707420`. Nếu khác, kiểm tra phiên bản và byte của file; không sửa dữ liệu chỉ để ép số lượng khớp. Thông tin tham chiếu ở [dataset_reference.json](dataset_reference.json).

## Tài liệu cần đọc

- [Từ điển 12 cột](DATA_DICTIONARY.md).
- [Hồ sơ nguồn và quyết định chia sẻ](PROVENANCE.md).
- [Hướng dẫn bắt đầu phân tích cho Trí và Luân](../docs/DATA_ANALYSIS_START.md).
- [Giao thức thực nghiệm](../docs/EXPERIMENT_PROTOCOL.md).

## File nào được đưa lên GitHub?

Tài liệu và mã kiểm kê có thể commit. CSV raw hiện vẫn bị .gitignore loại trừ. Khi điều kiện nguồn được xác nhận cho phép chia sẻ, thêm ngoại lệ chỉ cho file CSV này, giữ source/license/hash rồi commit; nếu chưa xác nhận thì hai người tải riêng và đối chiếu hash. Không đưa kaggle.json, token hoặc .env lên repo.

Kết quả kiểm kê thật hiện có: 5.110 dòng, 12 cột, 249 stroke = 1, 4.861 stroke = 0, 201 BMI thiếu; không có trùng dòng/id. Khi dùng bản mới, chạy lại và lưu báo cáo đúng bản đó. Không ghi kiểm kê của Trí là công việc Luân đã thực hiện.
