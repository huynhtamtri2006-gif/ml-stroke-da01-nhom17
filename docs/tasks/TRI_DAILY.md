# Nhiệm vụ theo ngày của Huỳnh Tâm Trí

MSSV: 2045240315. Đề tài DA-01, nhóm 17. Trí giám sát chung; người còn lại review. Đây là kế hoạch, chưa xác nhận công việc hoàn thành. Không yêu cầu số giờ/ngày.

## 2026-11-26 – DA01-001

Nhiệm vụ: Đọc đề, xác nhận phạm vi và thiết lập repo/Projects.

Giai đoạn: P1 Research; milestone: M1 Research and Setup; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: docs/notes/Tri_2026-11-26.md; repo Public; Project có quyền phù hợp; Issue đầu.

Tiêu chí nghiệm thu: Đối chiếu nhóm 17 = DA-01; ghi yêu cầu và câu hỏi; repo Public và quyền Project được kiểm tra hoặc ghi rõ phần đang chờ; không có secret.

Phụ thuộc: Không có nhiệm vụ trước. Xem nội dung Issue dự thảo tại docs/issues/DA01-001.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-11-27 – DA01-003

Nhiệm vụ: Thiết kế cấu trúc, luồng dữ liệu và wireframe 6 màn hình.

Giai đoạn: P2 Design; milestone: M1 Research and Setup; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: docs/design/wireframes; docs/design/architecture-review.md.

Tiêu chí nghiệm thu: Đủ 6 màn hình, sơ đồ offline/inference, thống nhất module theo 07b; Luân review.

Phụ thuộc: DA01-001. Xem nội dung Issue dự thảo tại docs/issues/DA01-003.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-11-28 – DA01-005

Nhiệm vụ: Thu thập CSV, kiểm kê và ghi nguồn sử dụng.

Giai đoạn: P7 Build; milestone: M1 Research and Setup; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: data/raw/CSV cục bộ; docs/data_inventory.md.

Tiêu chí nghiệm thu: Ghi nguồn/ngày/hash/license; số dòng/cột/thiếu/trùng/lớp đo thật; CSV gốc được commit theo ngoại lệ cụ thể, giữ nguồn/bản quyền/hash; không commit raw khác hoặc secret; chưa có CSV thì ghi Blocked.

Phụ thuộc: DA01-001. Xem nội dung Issue dự thảo tại docs/issues/DA01-005.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-11-29 – DA01-007

Nhiệm vụ: Phát triển bộ nạp và tiền xử lý train-only.

Giai đoạn: P7 Build; milestone: M2 Design and Data; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: data/nap.py; data/tien_xu_ly.py; tests cho tiền xử lý.

Tiêu chí nghiệm thu: Bỏ id, tách y, xử lý missing/Unknown và one-hot/scaling; test thống kê chỉ từ train, thứ tự cột ổn định.

Phụ thuộc: DA01-004, DA01-005. Xem nội dung Issue dự thảo tại docs/issues/DA01-007.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-11-30 – DA01-009

Nhiệm vụ: Hoàn thiện EDA và kiểm thử chống rò rỉ.

Giai đoạn: P7 Build; milestone: M2 Design and Data; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: analysis/kham_pha.py; hình EDA; test leakage.

Tiêu chí nghiệm thu: ≥6 loại biểu đồ có nhãn/đơn vị/nhận xét; phân tích missing BMI và 5 cột; tách EDA mô tả với chọn mô hình.

Phụ thuộc: DA01-007. Xem nội dung Issue dự thảo tại docs/issues/DA01-009.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-01 – DA01-011

Nhiệm vụ: Dựng FastAPI khung và màn hình tổng quan.

Giai đoạn: P7 Build; milestone: M3 Core and Validation; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: app/main.py; API thống kê; app/static/index.html.

Tiêu chí nghiệm thu: Số liệu lấy từ API thật; có 6 mục điều hướng, loading/error; chưa có mô hình thì thông báo rõ.

Phụ thuộc: DA01-003, DA01-005, DA01-007. Xem nội dung Issue dự thảo tại docs/issues/DA01-011.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-02 – DA01-013

Nhiệm vụ: Làm màn dự đoán và hợp đồng hiện vật.

Giai đoạn: P7 Build; milestone: M3 Core and Validation; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: app/api/du_doan.py; màn 2; docs/artifact-contract.md.

Tiêu chí nghiệm thu: Dùng pipeline/model lưu thật, validate input, thời gian; không fit trong request; Luân kiểm tra đầu ra.

Phụ thuộc: DA01-007, DA01-010, DA01-011. Xem nội dung Issue dự thảo tại docs/issues/DA01-013.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-03 – DA01-015

Nhiệm vụ: Thiết kế train demo chạy nền và trạng thái/dừng.

Giai đoạn: P7 Build; milestone: M3 Core and Validation; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: app/api/huan_luyen.py; màn 3.

Tiêu chí nghiệm thu: Tác vụ không chặn HTTP, có job/progress/cancel, cấu hình nhỏ giới hạn; test lỗi và dừng.

Phụ thuộc: DA01-010, DA01-013. Xem nội dung Issue dự thảo tại docs/issues/DA01-015.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-04 – DA01-017

Nhiệm vụ: Làm màn giảm chiều và sinh hình từ kết quả.

Giai đoạn: P7 Build; milestone: M3 Core and Validation; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: màn 4; analysis/ve_hinh.py phiên bản đầu.

Tiêu chí nghiệm thu: Hiện variance/loadings/k; dữ liệu chưa có ghi chưa có; PC1-PC2 không chuyển động giả; đọc result schema đúng.

Phụ thuộc: DA01-003, DA01-011, DA01-012, DA01-014, DA01-016. Xem nội dung Issue dự thảo tại docs/issues/DA01-017.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-05 – DA01-019

Nhiệm vụ: Gom cụm bệnh nhân và phân tích hồ sơ cụm.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: analysis/phan_cum.py; bảng cụm.

Tiêu chí nghiệm thu: K-means trên PCA không dùng nhãn khi fit/chọn cụm; số mẫu/ca dương/tỷ lệ và diễn giải thật.

Phụ thuộc: DA01-007, DA01-012. Xem nội dung Issue dự thảo tại docs/issues/DA01-019.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-06 – DA01-021

Nhiệm vụ: Khảo sát BMI và xây màn so sánh.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: phương án BMI; màn 5 đọc results; CSV export.

Tiêu chí nghiệm thu: So phương án có số mẫu rõ; bảng/biểu đồ có sai số; không tính lại thí nghiệm trong request.

Phụ thuộc: DA01-007, DA01-019, DA01-020. Xem nội dung Issue dự thảo tại docs/issues/DA01-021.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-07 – DA01-023

Nhiệm vụ: Làm màn ngưỡng cảnh báo và hai hình chiếu.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: màn 6; ma trận và FP/FN; liên kết PCA/LDA.

Tiêu chí nghiệm thu: Slider đồng bộ cùng mẫu/score, ma trận tính đúng, ghi nguồn dữ liệu, không báo hiệu năng train là test.

Phụ thuộc: DA01-013, DA01-014, DA01-017, DA01-020. Xem nội dung Issue dự thảo tại docs/issues/DA01-023.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-08 – DA01-025

Nhiệm vụ: Tích hợp hiện vật và kiểm thử API lỗi/đầu vào.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: integration tests; app import mã gốc.

Tiêu chí nghiệm thu: Save/load giữ dự đoán; không copy preprocessing; invalid input/error/cancel được kiểm tra.

Phụ thuộc: DA01-007, DA01-013, DA01-015, DA01-023, DA01-024. Xem nội dung Issue dự thảo tại docs/issues/DA01-025.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-09 – DA01-027

Nhiệm vụ: Hoàn thiện 6 màn hình và hỗ trợ khảo sát BMI.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: app đầy đủ; đồ thị BMI và ảnh giao diện.

Tiêu chí nghiệm thu: Đủ chức năng 07b; mọi số dẫn về results; dưới 5000 điểm web; so BMI không giấu thay đổi quần thể.

Phụ thuộc: DA01-021, DA01-023, DA01-025, DA01-026. Xem nội dung Issue dự thảo tại docs/issues/DA01-027.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-10 – DA01-029

Nhiệm vụ: Kiểm tra responsive, offline và train demo.

Giai đoạn: P9 Finalize; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: checklist 1920/768; JS cục bộ; log demo.

Tiêu chí nghiệm thu: Train nhỏ <30 giây và ≤5000 dòng được đo; loading/error, contrast ≥4.5:1 được kiểm tra; lỗi ghi Issue.

Phụ thuộc: DA01-027, DA01-028. Xem nội dung Issue dự thảo tại docs/issues/DA01-029.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-11 – DA01-031

Nhiệm vụ: Thử với 3 người và viết phần dữ liệu/ứng dụng.

Giai đoạn: P9 Finalize; milestone: M5 Defense Readiness; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: biên bản UX; báo cáo các phần Trí; ảnh 6 màn.

Tiêu chí nghiệm thu: 3 người ×10 phút; ghi 3 vấn đề và sửa; phần báo cáo đúng hiện vật, không bịa phản hồi.

Phụ thuộc: DA01-029. Xem nội dung Issue dự thảo tại docs/issues/DA01-031.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-12 – DA01-033

Nhiệm vụ: Hoàn thiện báo cáo chung và tính tay LDA.

Giai đoạn: P9 Finalize; milestone: M5 Defense Readiness; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: bản Word 15–25 trang; phép tính LDA; checklist hồ sơ.

Tiêu chí nghiệm thu: Kiểm tra phép tính chéo; đủ ≥3 nguồn/≥1 tiếng Anh, khai báo AI, biên bản và phân công thật.

Phụ thuộc: DA01-031, DA01-032. Xem nội dung Issue dự thảo tại docs/issues/DA01-033.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-13 – DA01-035

Nhiệm vụ: Chạy máy khác và chuẩn bị hướng dẫn offline.

Giai đoạn: P9 Finalize; milestone: M5 Defense Readiness; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: README_APP; bộ cài offline; ảnh/checklist máy khác.

Tiêu chí nghiệm thu: Người khác chạy theo hướng dẫn thật; đúng 3 lệnh khi đủ gói; không CDN, không secret.

Phụ thuộc: DA01-029, DA01-033. Xem nội dung Issue dự thảo tại docs/issues/DA01-035.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-14 – DA01-037

Nhiệm vụ: Diễn tập demo và quay video dự phòng.

Giai đoạn: P9 Finalize; milestone: M5 Defense Readiness; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: video; kịch bản demo; danh mục sao lưu.

Tiêu chí nghiệm thu: 6 màn chạy được, kịch bản 3 phút; cùng Luân tập tổng 13 phút; sửa lỗi xác minh được.

Phụ thuộc: DA01-033, DA01-035, DA01-036. Xem nội dung Issue dự thảo tại docs/issues/DA01-037.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-15 – DA01-039

Nhiệm vụ: Tham gia bảo vệ và ghi nhận phản hồi thật.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: ghi chú bảo vệ nếu buổi diễn ra; danh sách góp ý.

Tiêu chí nghiệm thu: Theo lịch lớp thực tế; demo phần dữ liệu/app; không ghi đã bảo vệ nếu chưa diễn ra.

Phụ thuộc: DA01-037, DA01-038. Xem nội dung Issue dự thảo tại docs/issues/DA01-039.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-16 – DA01-041

Nhiệm vụ: Phân loại góp ý và cập nhật kế hoạch nộp.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: Issue sửa lỗi hoặc checklist rà soát nếu không có góp ý.

Tiêu chí nghiệm thu: Mỗi thay đổi có nguồn yêu cầu và hạn; không tạo phản hồi giảng viên giả.

Phụ thuộc: DA01-039, DA01-040. Xem nội dung Issue dự thảo tại docs/issues/DA01-041.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-17 – DA01-043

Nhiệm vụ: Sửa ứng dụng/hướng dẫn theo lỗi đã xác nhận.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: PR sửa thật hoặc biên bản rà soát.

Tiêu chí nghiệm thu: Có tái hiện/test trước sau khi sửa; nếu không có lỗi ghi đúng không phát sinh.

Phụ thuộc: DA01-041, DA01-042. Xem nội dung Issue dự thảo tại docs/issues/DA01-043.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-18 – DA01-045

Nhiệm vụ: Tổng hợp minh chứng đóng góp của Trí.

Giai đoạn: P8 Tracking; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: CONTRIBUTION_REPORT phần Trí; link Issue/PR/tài liệu.

Tiêu chí nghiệm thu: Chỉ công việc thực làm, có review Luân; không đánh giá bằng số commit đơn thuần.

Phụ thuộc: DA01-043. Xem nội dung Issue dự thảo tại docs/issues/DA01-045.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-19 – DA01-047

Nhiệm vụ: Viết tự thuật cá nhân và kiểm tra hồ sơ nhóm.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: tự thuật Trí; checklist biên bản/phân công/AI.

Tiêu chí nghiệm thu: Dựa minh chứng xác minh; không gán công AI hoặc người khác; hồ sơ chính thức đúng danh sách.

Phụ thuộc: DA01-045, DA01-046. Xem nội dung Issue dự thảo tại docs/issues/DA01-047.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-20 – DA01-049

Nhiệm vụ: Rà soát gói nộp trên máy nhận.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: checklist file, hướng dẫn, ảnh/video, không secret.

Tiêu chí nghiệm thu: Người khác mở được; đường dẫn tương đối; không kèm raw trái phép hoặc credential.

Phụ thuộc: DA01-043, DA01-044, DA01-047, DA01-048. Xem nội dung Issue dự thảo tại docs/issues/DA01-049.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-21 – DA01-051

Nhiệm vụ: Chuẩn bị bản Release và mô tả hiện vật.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: draft release notes; danh sách tệp/SHA-256.

Tiêu chí nghiệm thu: Chưa publish nếu chưa nghiệm thu; phân biệt source, results, model và dữ liệu gốc.

Phụ thuộc: DA01-049, DA01-050. Xem nội dung Issue dự thảo tại docs/issues/DA01-051.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

## 2026-12-22 – DA01-053

Nhiệm vụ: Nộp bài và tạo Release sau nghiệm thu.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: Release v1.0.0 và minh chứng nộp nếu thực hiện.

Tiêu chí nghiệm thu: Đúng hạn thông báo lớp; chỉ tạo tag/release khi thật đạt; lưu bằng chứng nộp, không suy đoán.

Phụ thuộc: DA01-051, DA01-052. Xem nội dung Issue dự thảo tại docs/issues/DA01-053.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; người còn lại review. Chưa có minh chứng thì không ghi Done.

Ngày trong bảng là mốc kế hoạch; có thể bắt đầu sớm khi đầu vào đã sẵn sàng. Phụ thuộc dùng để nghiệm thu phần tích hợp; phần nghiên cứu/khung giao diện có thể làm song song. Xem docs/HANDOFFS.md.

## Nghiệm thu và bảo vệ

Giải thích được phần mình làm; ghi công đúng người và phần AI hỗ trợ; hoàn thành hồ sơ thật, không tạo commit hộ hoặc tự thuật thành tích chưa thực hiện. Lịch bảo vệ/nộp theo tài liệu lớp cần theo dõi nếu có thay đổi.
