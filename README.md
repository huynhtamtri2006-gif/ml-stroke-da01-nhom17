# Cảnh báo sớm đột quỵ bằng học máy trên hồ sơ sức khỏe cộng đồng

**Nghiên cứu ảnh hưởng của PCA và LDA đến khả năng phát hiện lớp đột quỵ hiếm**

Đồ án kết thúc học phần **Học máy** — Mã đề tài **DA-01** — **Nhóm 17, lớp 15DHTH07**

Khoa Công nghệ Thông tin — Trường Đại học Công Thương TP. Hồ Chí Minh (HUIT)

Học kỳ 1, năm học **2026–2027**

Repository: **[ml-stroke-da01-nhom17](https://github.com/huynhtamtri2006-gif/ml-stroke-da01-nhom17)**

Repository lưu trữ quá trình nghiên cứu và phát triển đồ án, từ phân tích dữ liệu, tự xây dựng thuật toán đến thực nghiệm và ứng dụng minh họa. Người mới tham gia có thể làm theo hướng dẫn bên dưới để tải tài liệu, xác định nhiệm vụ và đóng góp bằng tài khoản GitHub cá nhân.

> > **Trạng thái hiện tại:** repository đã có bộ dữ liệu Stroke Prediction Dataset dạng CSV, tài liệu nghiên cứu, từ điển dữ liệu, công cụ kiểm kê và kế hoạch phân công. Thành viên được cấp quyền có thể clone repository để đọc tài liệu, kiểm tra dữ liệu và bắt đầu phân tích. Phần thuật toán học máy và ứng dụng minh họa sẽ được xây dựng theo từng giai đoạn.

## 1. Thành viên và trách nhiệm

| STT | Họ và tên | MSSV | Trách nhiệm triển khai | GitHub |
|---|---|---|---|---|
| 1 | Huỳnh Tâm Trí | 2045240315 | Giám sát nhiệm vụ; thu thập và tiền xử lý dữ liệu; thiết kế hệ thống; ứng dụng; tích hợp và kiểm tra tiến độ | [huynhtamtri2006-gif](https://github.com/huynhtamtri2006-gif) |
| 2 | Cao Minh Luân | 2001240263 | Nghiên cứu và tự viết thuật toán; thiết kế thực nghiệm; đánh giá thống kê; hiệu chuẩn xác suất và phân tích kết quả | Chờ bổ sung username |

Mỗi nhiệm vụ có một người chịu trách nhiệm chính và người còn lại kiểm tra. Trí giám sát công việc theo phân công triển khai. Danh sách giảng viên ghi Luân là nhóm trưởng và nhóm có 3 thành viên; phương án làm việc cho hai người không thay đổi hồ sơ đăng ký chính thức.

## 2. Mục tiêu và câu hỏi nghiên cứu

Đề tài sử dụng hồ sơ sức khỏe dạng bảng để nghiên cứu bài toán phân lớp nhị phân với nhãn `stroke`. Theo mô tả đề, số ca đột quỵ chiếm khoảng 4,87% dữ liệu; vì vậy, một mô hình có accuracy cao vẫn có thể bỏ sót phần lớn hoặc toàn bộ lớp dương.

Các mục tiêu chính:

- Phân tích dữ liệu, sự mất cân bằng và ảnh hưởng của giá trị thiếu.
- Tự viết Logistic Regression có trọng số lớp bằng NumPy.
- Tự viết PCA qua SVD và LDA Fisher để khảo sát tác động của giảm chiều.
- Kiểm chứng bản tự viết với thư viện, so sánh các baseline trên cùng giao thức.
- Gom cụm hồ sơ bệnh nhân, sau đó mô tả tỷ lệ đột quỵ trong từng cụm.
- Thực hiện hướng mở rộng hiệu chuẩn xác suất và lựa chọn ngưỡng theo chi phí.
- Xây dựng ứng dụng 6 màn hình để minh họa dữ liệu, mô hình và kết quả nghiên cứu.

**Câu hỏi trung tâm:** PCA giữ các hướng có phương sai lớn có làm mất thông tin phân biệt lớp đột quỵ hiếm không? Hiệu năng thay đổi từ số chiều `k` nào, và kết quả khác LDA một chiều như thế nào?

Độ đo chính theo đề là **PR-AUC hình thang của lớp `stroke = 1`**. Precision, recall và F1 được báo cáo bổ sung. AP được ghi riêng nếu sử dụng, không coi là cùng phép tính với PR-AUC hình thang.

## 3. Dữ liệu đầu vào và sản phẩm đầu ra

**Nguồn chỉ định:** [Stroke Prediction Dataset trên Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset).

**Tên file:** `healthcare-dataset-stroke-data.csv`.

| Nội dung | Thông tin theo đề |
|---|---|
| Kích thước | 5.110 dòng, 12 cột |
| Đầu vào mô hình | 10 đặc trưng sau khi bỏ `id` và tách nhãn |
| Nhãn | `stroke`: 0 hoặc 1 |
| Lớp dương | 249 mẫu |
| Giá trị thiếu | 201 ô ở cột `bmi` |

Các con số trên đã khớp [kiểm kê CSV ngày 27/11/2026](data/inventory/inventory.md). File gốc là `data/raw/healthcare-dataset-stroke-data.csv`, được chọn để đưa vào repo theo yêu cầu của Trí; xem [hướng dẫn dữ liệu và đối chiếu hash](data/README.md). Một số [nhận xét ban đầu](docs/INITIAL_DATA_FINDINGS.md) giúp hai người bắt đầu phân tích. Thông tin bản quyền của tác giả gốc được giữ trong [hồ sơ nguồn](data/PROVENANCE.md).

Sản phẩm dự kiến gồm mã thuật toán, bài kiểm thử, kết quả từng fold và bảng tổng hợp, biểu đồ nghiên cứu, hiện vật mô hình, ứng dụng minh họa, báo cáo Word, slide và minh chứng đóng góp.

## 4. Quy trình nghiên cứu và xây dựng

```text
Đọc yêu cầu và chốt giao thức đánh giá
                  |
                  v
Tải dữ liệu -> Kiểm kê -> Chia dữ liệu phân tầng
                  |
                  v
Khám phá dữ liệu và thiết kế tiền xử lý
                  |
                  v
Tự viết Logistic Regression, PCA, LDA và các độ đo
                  |
                  v
Kiểm thử và đối chiếu với thư viện
                  |
                  v
Quét k, chạy baseline và đánh giá 5-fold x 5 lần lặp
                  |
                  v
Gom cụm, phân tích thống kê, hiệu chuẩn và chọn ngưỡng
                  |
                  v
Tích hợp ứng dụng 6 màn hình -> Kiểm thử -> Báo cáo và bảo vệ
```

Các phép điền khuyết, mã hóa, chuẩn hóa và giảm chiều phải được khớp trên phần huấn luyện tương ứng. Không dùng dữ liệu đánh giá để chọn ngưỡng hoặc hiệu chuẩn. Chi tiết tại [giao thức thực nghiệm](docs/EXPERIMENT_PROTOCOL.md).

## 5. Cấu trúc repository

```text
ml-stroke-da01-nhom17/
├── .github/                 # Mẫu Issue và Pull Request
├── docs/                    # Nghiên cứu, thiết kế và hướng dẫn làm việc
│   ├── issues/              # Nội dung dự thảo cho từng nhiệm vụ
│   └── tasks/               # Kế hoạch cá nhân và danh mục nhiệm vụ CSV
├── data/                    # Hướng dẫn dữ liệu; nơi phát triển bộ nạp/tiền xử lý
│   └── raw/                 # CSV Stroke được chọn để commit; raw khác vẫn gitignore
├── models/                  # Nơi phát triển thuật toán tự viết và bản đối chiếu
├── experiments/             # Nơi phát triển cấu hình và trình chạy thực nghiệm
├── analysis/                # Nơi phát triển phân tích dữ liệu và sinh hình
├── app/                     # Nơi phát triển ứng dụng 6 màn hình
├── tests/                   # Nơi bổ sung kiểm thử thuật toán và tích hợp
├── results/                 # Nơi lưu kết quả có nguồn gốc sau khi chạy thực tế
├── reports/
│   └── planning/            # Hai file Word nhiệm vụ theo ngày
├── presentations/           # Nơi lưu slide và kịch bản thuyết trình
├── tools/                   # Công cụ hỗ trợ quản lý nhiệm vụ
├── README.md                # Giới thiệu và hướng dẫn sử dụng repository
├── REQUIREMENTS.md          # Yêu cầu và tiêu chí nghiệm thu
├── TECH_STACK.md            # Công nghệ dự kiến và lý do lựa chọn
├── PROJECT_PLAN.md          # Kế hoạch, milestones và phụ thuộc
├── TASK_ASSIGNMENTS.md      # Phân công theo ngày của hai thành viên
├── TEAM_MEMBERS.md          # Thông tin và trách nhiệm thành viên
├── RESEARCH_LOG.md          # Nhật ký nghiên cứu thực tế
├── WEEKLY_PROGRESS.md       # Mẫu báo cáo tiến độ ngày, tuần và giai đoạn
├── CONTRIBUTION_REPORT.md   # Minh chứng đóng góp cá nhân
├── CONTRIBUTING.md          # Quy trình Git, PR và review
└── CHANGELOG.md             # Lịch sử thay đổi
```

Các thư mục thuật toán và ứng dụng hiện chứa hướng dẫn chuẩn bị, chưa có phần triển khai. Cấu trúc dùng `data/`, `models/`, `experiments/` và `app/` ở thư mục gốc theo tài liệu 07b, không tạo thêm `src/` trùng chức năng.

## 6. Hướng dẫn tải và sử dụng repository

## Hướng dẫn sử dụng dữ liệu

### 1. Clone repository

Thành viên cần được cấp quyền truy cập repository Private trước khi thực hiện:

```powershell
git clone https://github.com/huynhtamtri2006-gif/ml-stroke-da01-nhom17.git
cd ml-stroke-da01-nhom17
```

Nếu đã clone trước đó, lưu hoặc commit các thay đổi đang làm, sau đó cập nhật nhánh main:

```powershell
git switch main
git pull --ff-only
```

### 2. Mở bộ dữ liệu

File CSV gốc được lưu tại:

```text
data/raw/healthcare-dataset-stroke-data.csv
```

Có thể xem trực tiếp trên GitHub, mở bằng trình đọc CSV hoặc nạp vào Python để phân tích. Giữ nguyên file gốc; thực hiện làm sạch và biến đổi trong mã tiền xử lý.

### 3. Đọc tài liệu mô tả

- [Từ điển dữ liệu](data/DATA_DICTIONARY.md): ý nghĩa và lưu ý của 12 cột.
- [Hồ sơ nguồn dữ liệu](data/PROVENANCE.md): nguồn Kaggle, thông tin bản quyền và mã SHA-256.
- [Báo cáo kiểm kê](data/inventory/inventory.md): kích thước, phân bố nhãn, giá trị thiếu và bản ghi trùng.
- [Nhận xét ban đầu](docs/INITIAL_DATA_FINDINGS.md): các vấn đề cần khảo sát.
- [Hướng dẫn phân tích](docs/DATA_ANALYSIS_START.md): thứ tự thực hiện dành cho thành viên.

### 4. Kiểm kê trên máy cá nhân

Tại thư mục gốc repository, chạy:

```powershell
python data/kiem_ke.py
```

Công cụ chỉ sử dụng thư viện chuẩn Python, không cần cài thêm thư viện. Báo cáo được tạo tại:

```text
data/inventory/inventory.md
data/inventory/inventory.json
```

Kết quả tham chiếu:

| Nội dung | Giá trị |
|---|---:|
| Số dòng | 5.110 |
| Số cột | 12 |
| Nhãn không đột quỵ | 4.861 |
| Nhãn đột quỵ | 249 |
| Giá trị thiếu ở cột BMI | 201 |
| Bản ghi trùng toàn bộ | 0 |

Đây là kết quả kiểm kê dữ liệu, chưa phải kết quả đánh giá mô hình.

### 5. Bắt đầu thực hiện nhiệm vụ

Đọc [phân công nhiệm vụ](TASK_ASSIGNMENTS.md) và [quy định đóng góp](CONTRIBUTING.md), sau đó tạo nhánh riêng cho công việc được giao.

Trước khi xây dựng mô hình, thống nhất cách chia dữ liệu và tuân thủ [giao thức thực nghiệm](docs/EXPERIMENT_PROTOCOL.md). Các bước điền khuyết, mã hóa, chuẩn hóa và giảm chiều chỉ được khớp trên phần huấn luyện tương ứng.

### Nguồn và bản quyền

Dữ liệu được lấy từ [Stroke Prediction Dataset của fedesoriano trên Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset).

Thông tin License hiển thị tại nguồn: **Data files © Original Authors**. Bản quyền dữ liệu thuộc tác giả gốc; nhóm không nhận là dữ liệu tự thu thập và không gán giấy phép mở khác cho CSV.

## 7. Ứng dụng minh họa dự kiến

| Màn hình | Chức năng chính |
|---|---|
| 1. Tổng quan | Nguồn dữ liệu, câu hỏi nghiên cứu, kiểm kê và phân bố lớp |
| 2. Thử mô hình | Nhập/chọn mẫu, chọn mô hình, xem dự đoán và thời gian suy luận |
| 3. Huấn luyện và đánh giá | Chạy cấu hình nhỏ ở nền, tiến độ, dừng và bảng độ đo |
| 4. Phân tích giảm chiều | Chọn k, phương sai tích lũy, hình chiếu và hiệu năng |
| 5. So sánh kết quả | Bảng baseline/tự viết/thư viện, sai số và xuất CSV |
| 6. Ngưỡng cảnh báo | Thay ngưỡng, xem ca bỏ sót/báo nhầm và hình PCA/LDA đồng bộ |

Công nghệ dự kiến: Python, NumPy/SciPy, pandas, scikit-learn cho phần được phép, FastAPI, HTML/CSS/JavaScript thuần và Plotly.js lưu cục bộ. Ứng dụng nạp mô hình đã lưu; thí nghiệm đầy đủ chạy ngoại tuyến.

## 8. Kế hoạch, quản lý và kết quả thực nghiệm

Kế hoạch theo ngày được lập từ **26/11 đến 22/12/2026**, gồm **54 nhiệm vụ dự thảo**, chia 27 nhiệm vụ mỗi người. Theo tài liệu hướng dẫn, lịch bảo vệ là **15/12/2026**, nhóm 17 ở khung **20:05–20:21**, hạn nộp **22/12/2026**; nhóm cần theo dõi thông báo lớp nếu có thay đổi.

- [Kế hoạch và milestones](PROJECT_PLAN.md).
- [Thiết lập repository và nhập Issue](docs/GITHUB_SETUP.md).
- [Thiết lập GitHub Projects, trường và các view](docs/PROJECTS_SETUP.md).
- [Kiểm tra hiện vật ở bước khởi động](docs/CHECKPOINT_01.md).

**Chưa có kết quả thực nghiệm để công bố.** Khi có kết quả thật, mục này sẽ bổ sung PR-AUC, F1, precision, recall, biến thiên qua các lần đo, kiểm định và liên kết đến cấu hình cùng file số liệu. Không dùng số của đề hoặc bảng minh họa làm kết quả mô hình.

## 9. Nguồn tham khảo và minh bạch đóng góp

Tài liệu nền gồm giáo trình học phần, hướng dẫn DA-01, tài liệu scikit-learn, bài nghiên cứu về precision–recall và các nguồn trong [SOURCES.md](docs/SOURCES.md). Repository khác chỉ dùng để học và tham khảo; việc tái sử dụng tài sản phải tuân thủ giấy phép và ghi nguồn.

Mỗi thành viên sử dụng tài khoản GitHub cá nhân, tự ghi nhận công việc và hiểu phần mình phụ trách. Đánh giá đóng góp dựa trên chất lượng, khối lượng, trách nhiệm, thời hạn và hiện vật thực tế, không chỉ dựa vào số commit.

Bộ tài liệu khởi động có AI hỗ trợ; xem [khai báo sử dụng AI](docs/AI_USAGE.md). Tài liệu dự thảo chưa phải bằng chứng thành viên đã hoàn thành nghiên cứu hoặc lập trình. Phạm vi đồ án là nghiên cứu và minh họa học thuật, chưa có đánh giá để sử dụng cho quyết định lâm sàng.
