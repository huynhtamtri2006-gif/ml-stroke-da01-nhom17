# Cảnh báo sớm đột quỵ bằng học máy trên hồ sơ sức khỏe cộng đồng

**Nghiên cứu ảnh hưởng của PCA và LDA đến khả năng phát hiện lớp đột quỵ hiếm**

Đồ án kết thúc học phần **Học máy** — Mã đề tài **DA-01** — **Nhóm 17, lớp 15DHTH07**

Khoa Công nghệ Thông tin — Trường Đại học Công Thương TP. Hồ Chí Minh (HUIT)

Học kỳ 1, năm học **2026–2027**

Repository: **[ml-stroke-da01-nhom17](https://github.com/huynhtamtri2006-gif/ml-stroke-da01-nhom17)**

Repository lưu trữ quá trình nghiên cứu và phát triển đồ án, từ phân tích dữ liệu, tự xây dựng thuật toán đến thực nghiệm và ứng dụng minh họa. Người mới tham gia có thể làm theo hướng dẫn bên dưới để tải tài liệu, xác định nhiệm vụ và đóng góp bằng tài khoản GitHub cá nhân.

> **Trạng thái hiện tại:** đã có bộ tài liệu khởi động, kế hoạch và phân công. Chưa có mã thuật toán, ứng dụng chạy được, dữ liệu CSV, mô hình đã huấn luyện hoặc kết quả thực nghiệm. Các chức năng và sản phẩm bên dưới là phạm vi dự kiến thực hiện.

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

Các con số trên cần được đối chiếu với CSV tải thực tế. Dữ liệu gốc lưu cục bộ tại `data/raw/`, không đưa lên GitHub. Xem [hướng dẫn dữ liệu](data/README.md) trước khi tải, sử dụng hoặc chia sẻ.

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
│   └── raw/                 # Dữ liệu gốc cục bộ, được gitignore
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

### Bước 1: Nhận quyền truy cập

Repository ở chế độ Private theo kế hoạch của nhóm. Thành viên cần được chủ repository mời và chấp nhận lời mời bằng tài khoản GitHub cá nhân trước khi clone.

### Bước 2: Clone về máy

Mở PowerShell hoặc terminal tại thư mục muốn lưu dự án:

```powershell
git clone https://github.com/huynhtamtri2006-gif/ml-stroke-da01-nhom17.git
cd ml-stroke-da01-nhom17
```

Nếu đã có thư mục làm việc của dự án, tiếp tục dùng thư mục đó; không cần clone lần nữa. Trên máy của Trí, thư mục ban đầu là `D:\ML - CUOI KY\do_an_DA01_nhom17`.

### Bước 3: Đọc tài liệu theo thứ tự

| Thứ tự | Tài liệu | Mục đích |
|---|---|---|
| 1 | [Bắt đầu tại đây](docs/START_HERE.md) | Nắm thứ tự công việc ban đầu |
| 2 | [Nghiên cứu và phân tích đề tài](docs/01_NGHIEN_CUU_VA_PHAN_TICH.md) | Hiểu bài toán, kiến thức, giải pháp và rủi ro |
| 3 | [Yêu cầu hệ thống](REQUIREMENTS.md) | Xác định sản phẩm và tiêu chí phải đạt |
| 4 | [Nguồn học tập](docs/SOURCES.md) | Chọn tài liệu cần đọc và ghi nguồn |
| 5 | [Giao thức thực nghiệm](docs/EXPERIMENT_PROTOCOL.md) | Hiểu cách chia dữ liệu, đánh giá và tránh rò rỉ |
| 6 | [Thiết kế kiến trúc](docs/ARCHITECTURE.md) và [công nghệ](TECH_STACK.md) | Hiểu các thành phần trước khi lập trình |
| 7 | [Phân công nhiệm vụ](TASK_ASSIGNMENTS.md) | Tìm nhiệm vụ theo người và theo ngày |
| 8 | [Quy định đóng góp](CONTRIBUTING.md) | Làm việc bằng nhánh, commit, PR và review |

### Bước 4: Mở kế hoạch cá nhân

- **Huỳnh Tâm Trí:** [kế hoạch theo ngày](docs/tasks/TRI_DAILY.md) hoặc [file Word](reports/planning/03_Nhiem_vu_Huynh_Tam_Tri_theo_ngay.docx).
- **Cao Minh Luân:** [kế hoạch theo ngày](docs/tasks/LUAN_DAILY.md) hoặc [file Word](reports/planning/04_Nhiem_vu_Cao_Minh_Luan_theo_ngay.docx).

Từng nhiệm vụ có Task ID, đầu ra, phụ thuộc và tiêu chí nghiệm thu. Nội dung Issue dự thảo nằm trong `docs/issues/`; danh mục tổng hợp nằm ở [task_manifest.csv](docs/tasks/task_manifest.csv).

Task ID như `DA01-001` không phải số Issue GitHub `#1`. Liên kết số Issue thật sau khi tạo; bản kế hoạch không tự chứng minh nhiệm vụ đã được thực hiện.

### Bước 5: Làm việc trên nhánh riêng

Ví dụ bắt đầu nhiệm vụ nghiên cứu `DA01-001`, khi thư mục làm việc không có thay đổi chưa lưu:

```powershell
git switch main
git pull --ff-only
git switch -c docs/da01-001-research
```

Thay Task ID và tên nhánh theo nhiệm vụ của mình. Tự ghi nội dung nghiên cứu hoặc triển khai, kiểm tra thay đổi, commit bằng danh tính cá nhân, push nhánh và mở Pull Request để người còn lại review. Các lệnh chi tiết và xử lý xung đột nằm trong [CONTRIBUTING.md](CONTRIBUTING.md).

### Bước 6: Ghi nhận kết quả sau mỗi buổi làm

1. Cập nhật Issue bằng việc thực làm, kết quả kiểm tra và vướng mắc.
2. Ghi nguồn đã đọc và điều đã vận dụng vào [RESEARCH_LOG.md](RESEARCH_LOG.md).
3. Cập nhật [báo cáo tiến độ](WEEKLY_PROGRESS.md) và trạng thái trên Projects nếu đã thiết lập.
4. Gắn link tài liệu, commit, PR, test hoặc kết quả vào [minh chứng đóng góp](CONTRIBUTION_REPORT.md).
5. Chỉ chuyển Done khi đạt tiêu chí và đã được kiểm tra.

### Bước 7: Chuẩn bị môi trường và chạy các thành phần sau này

Đọc [ENVIRONMENT.md](docs/ENVIRONMENT.md) để kiểm tra Python và chuẩn bị môi trường riêng khi bắt đầu lập trình. Dữ liệu thô, môi trường Python và hiện vật bị gitignore không tự xuất hiện sau khi clone.

Hiện chưa có `requirements.txt` đã khóa, lệnh huấn luyện hoặc lệnh chạy ứng dụng. Hướng dẫn cài đặt và chạy sẽ được bổ sung cùng từng thành phần đã kiểm chứng; chưa chạy các lệnh mẫu dành cho phần mã chưa tồn tại.

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
