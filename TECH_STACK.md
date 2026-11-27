# Công nghệ dự kiến và quyết định kiến trúc

Các lựa chọn dưới đây là đề xuất để nhóm duyệt; chưa có môi trường cài đặt hoặc benchmark. Ưu tiên chạy CPU cục bộ, miễn phí về công cụ phát triển và không phụ thuộc cloud.

| Lựa chọn | Ưu điểm | Hạn chế/chi phí | Quyết định |
|---|---|---|---|
| Python | Phù hợp NumPy, thống kê và FastAPI | Cần thống nhất phiên bản | Chọn; ưu tiên 3.12 để hai máy cùng môi trường, kiểm tra trước khi khóa |
| NumPy + SciPy | Ma trận, SVD, kiểm định; không cần GPU | Phải hiểu loss và ổn định số | Chọn cho lõi tự viết |
| pandas | Kiểm kê, làm sạch CSV | Dễ vô tình fit toàn dữ liệu | Chọn cho dữ liệu |
| scikit-learn | Pipeline, chia fold, baseline và đối chiếu | Không thay phần bắt buộc tự viết | Chọn đúng ranh giới của đề |
| matplotlib/seaborn | Hình báo cáo xuất cục bộ | Ít tương tác hơn web | Chọn cho báo cáo |
| FastAPI | Tái sử dụng Python, tài liệu API | Cần học HTTP, validation, tác vụ nền | Chọn theo 07b |
| Flask | Nhẹ, linh hoạt | Cần tự tổ chức nhiều phần kiểm tra/API | Không chọn để bám đặc tả |
| Streamlit | Nhanh cho bản thử nghiệm | Khó bám chức năng 6 màn hình và vòng đời train nền theo đề | Không chọn nền tảng chính |
| HTML/CSS/JS thuần | Không cần npm/build; chạy offline | Tự quản lý trạng thái UI | Chọn theo 07b |
| React/Vue | Hệ sinh thái giao diện lớn | Thêm build chain; 07b yêu cầu JS thuần | Không dùng |
| Plotly.js lưu cục bộ | Đủ đồ thị khoa học/tương tác | Tệp lớn hơn Chart.js | Chọn; kiểm tra giấy phép bản tải |
| CSV/NPZ/JSON | Nhẹ, dễ kiểm tra, tái lập | Không phù hợp nhiều người ghi đồng thời | Chọn lưu kết quả và hiện vật |
| SQLite/PostgreSQL | Quản lý giao dịch, truy vấn | Tăng phạm vi; chưa có nhu cầu | Chưa dùng cơ sở dữ liệu |
| pytest | Kiểm chứng thuật toán và chống rò rỉ | Phải chọn tolerance phù hợp | Dùng khi bắt đầu có mã |
| Git + GitHub Public + Projects | Lịch sử thật, Issue, PR và quản lý kế hoạch; đọc/clone công khai | Push nhánh cần quyền; phải cấu hình bảo vệ main riêng | Repository Public; nhánh nhiệm vụ + PR, Trí quyết định merge; chưa xác minh Rulesets thực tế |

Máy đang dùng có Python 3.14.7; không tự đổi Python toàn hệ thống. Cấu hình RAM/CPU của hai máy chưa được xác nhận. Bắt đầu bằng tập nhỏ và đo thời gian trước quét đủ. Không khẳng định máy đạt cấu hình dựa trên suy đoán.

Phần đọc CSV và kiểm kê hiện chỉ dùng thư viện chuẩn, hoạt động không cần requirements.txt. Chưa tạo requirements.txt với phiên bản giả định cho thuật toán/ứng dụng chưa triển khai. Khi chạy smoke test thành công trên cả hai máy, ghi đúng phiên bản vào requirements.txt; chuẩn bị wheel cho cài ngoại tuyến. Python và thư viện phải cùng phiên bản/kiến trúc trên máy chuẩn bị và máy đích.

Nguồn: [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/); [GitHub protected branches và giới hạn gói](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
