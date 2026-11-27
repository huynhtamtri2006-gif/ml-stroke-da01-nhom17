# Rà soát trước khi bàn giao cho Luân

Ngày 27/11/2026. Phạm vi: đủ đầu vào để nghiên cứu và phát triển DA-01 từ đầu; không phải nghiệm thu đồ án cuối kỳ.

## Kết luận

Đủ dữ liệu và tài liệu để bắt đầu nghiên cứu/triển khai sau khi cập nhật các file rà soát lên GitHub. Các kiểm tra kỹ thuật bên dưới đã đạt trong bản sao tách biệt. Thuật toán học máy, wireframe, EDA, mô hình và kết quả vẫn là công việc hai thành viên phải thực hiện.

## Dữ liệu và nguồn

CSV gốc có 5.110 dòng, 12 cột; 4.861 nhãn0, 249 nhãn1; BMI thiếu201; không trùng dòng/id. Hash tham chiếu `644d473b05d2797006bd94865e4f8bb057f0c721617911613c82c8fcfc707420`. File được Git theo dõi, .gitattributes bảo toàn byte raw, nguồn/bản quyền được ghi trong data/PROVENANCE.md. Hai PDF gốc được chép nguyên byte trong docs/specifications/.

## Điều chỉnh trong lần rà soát

- Bổ sung PDF gốc và bảng đối chiếu REQUIREMENT_COVERAGE để Luân đọc yêu cầu sau clone.
- Sửa các đoạn còn ghi chưa có dữ liệu/chưa tạo repo và quy định loại trừ raw đã lỗi thời; không sửa bản CHECKPOINT lịch sử, thêm liên kết đến trạng thái mới.
- Bổ sung tương tác riêng DA-01, mức kiểm chứng PCA/LDA và vấn đề one-hot có mức cực hiếm.
- Rà phụ thuộc kỹ thuật của54 nhiệm vụ, đồng bộ CSV/Issue dự thảo/Markdown và hai Word Times New Roman13; không đổi ngày dự kiến thành ngày hoàn thành hoặc gán đóng góp giả.
- Thêm HANDOFFS và START_HERE cho người mới; kiểm kê cá nhân lưu data/processed/ để không đổi timestamp báo cáo tham chiếu đã commit.
- Sửa lỗi định dạng README, giữ nội dung do Trí đã chỉnh trên GitHub.

## Kiểm tra kỹ thuật

- CSV trong commit hiện tại có hash đúng bản tham chiếu; 5.110×12, nhãn4861/249, BMI thiếu201.
- Kiểm kê chạy thành công trong thư mục sao chép tách biệt; không cần thư viện ngoài.
- Bốn bài kiểm thử công cụ đều đạt trong bản sao; chưa có hoặc kiểm thử thuật toán học máy.
- 54 Task ID duy nhất; phụ thuộc không vòng, ngày phụ thuộc không sau ngày nhiệm vụ; CSV/Issue dự thảo/Markdown đã đồng bộ.
- Hai Word đồng bộ nội dung phụ thuộc, các text run Times New Roman cỡ13; chưa kiểm tra dàn trang bằng Microsoft Word.
- Tất cả đích liên kết Markdown nội bộ tồn tại; liên kết web không được thử lại toàn bộ trong lần rà soát này.
- Hai PDF trong repo giống nguyên byte file được cung cấp.

Đây là kiểm tra cục bộ và bản sao thư mục, không phải đăng nhập/clone thực từ GitHub bằng tài khoản Luân. Các file rà soát mới chưa được commit/push thay Trí.

## Phần còn cần hai người xác nhận

Repository đã được Trí chuyển Public; Luân có thể clone ngay. Còn cần xác nhận username/quyền collaborator để Luân push nhánh, quyền Project và cấu hình Rulesets; chưa kiểm tra các quyền từ xa. Hai người cần thống nhất môi trường học máy và ghi quyết định giao thức trước chạy mô hình đầu; đọc CSV/kiểm kê không cần thêm thư viện.

Slide chương2–4, giáo trình/rubric trong các tài liệu03/11 và nhiệm vụ riêng08/08b chưa được cung cấp. Gói hiện đủ bắt đầu nghiên cứu DA-01; bổ sung tài liệu lớp trước chốt báo cáo/chấm điểm. Không cần dataset thứ hai cho phạm vi DA-01 hiện được giao.

## Bước tiếp

Trí commit/push phần rà soát; mời Luân. Luân clone, đọc START_HERE, kiểm kê/test công cụ và đọc PDF DA-01. Cả hai review giao thức, chốt nhiệm vụ rồi làm song song theo HANDOFFS. Nếu đã có Issue từ xa, sửa nội dung phụ thuộc theo bản mới, không tạo trùng.
