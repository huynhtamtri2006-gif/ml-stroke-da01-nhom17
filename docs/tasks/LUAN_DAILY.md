# Nhiệm vụ theo ngày của Cao Minh Luân

MSSV: 2001240263. Đề tài DA-01, nhóm 17. Trí giám sát chung, tự kiểm tra phần mình, review phần Luân và quyết định nghiệm thu/merge. Đây là kế hoạch, chưa xác nhận công việc hoàn thành. Không yêu cầu số giờ/ngày.

## 2026-11-26 – DA01-002

Nhiệm vụ: Nghiên cứu mất cân bằng, PR-AUC và yêu cầu thuật toán.

Giai đoạn: P1 Research; milestone: M1 Research and Setup; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: docs/notes/Luan_2026-11-26.md; danh sách câu hỏi.

Tiêu chí nghiệm thu: Tóm tắt bằng lời mình từ bài Saito và đề; phân biệt accuracy/recall/PR-AUC/AP; ghi nguồn và phần còn chưa hiểu.

Phụ thuộc: Không có nhiệm vụ trước. Xem nội dung Issue dự thảo tại docs/issues/DA01-002.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-11-27 – DA01-004

Nhiệm vụ: Chốt giao thức, độ đo và suy diễn Logistic trọng số.

Giai đoạn: P2 Design; milestone: M1 Research and Setup; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: docs/notes/protocol-decision.md; công thức loss/gradient.

Tiêu chí nghiệm thu: Chốt trước lần chạy: 80/20 + CV5x5, train-only fit, inner tuning; giải thích weights/L2/bias và PR-AUC hình thang.

Phụ thuộc: DA01-002. Xem nội dung Issue dự thảo tại docs/issues/DA01-004.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-11-28 – DA01-006

Nhiệm vụ: Thiết lập môi trường và bài tập NumPy/gradient.

Giai đoạn: P7 Build; milestone: M1 Research and Setup; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: docs/environment-check.md; bài tập tự làm trong docs/notes/.

Tiêu chí nghiệm thu: Ghi Python/thư viện thực; giải thích hình dạng ma trận và gradient; kiểm tra ví dụ nhỏ, không dùng lõi sklearn thay NumPy.

Phụ thuộc: DA01-002. Xem nội dung Issue dự thảo tại docs/issues/DA01-006.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-11-29 – DA01-008

Nhiệm vụ: Tự viết weighted Logistic loss và gradient.

Giai đoạn: P7 Build; milestone: M2 Design and Data; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: models/logistic.py bước loss/gradient; tests gradient.

Tiêu chí nghiệm thu: Ổn định số, L2 không phạt bias, gradient khớp sai phân; có giải thích từng phần và test.

Phụ thuộc: DA01-004, DA01-006. Xem nội dung Issue dự thảo tại docs/issues/DA01-008.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-11-30 – DA01-010

Nhiệm vụ: Hoàn thiện gradient descent và đối chiếu Logistic.

Giai đoạn: P7 Build; milestone: M2 Design and Data; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: models/logistic.py; models/doi_chieu.py; test Logistic.

Tiêu chí nghiệm thu: Bản NumPy chạy trước đối chiếu; khớp loss/weights/L2; xác suất MAE <1e-3 khi hội tụ; ghi kiểm tra thật.

Phụ thuộc: DA01-007, DA01-008. Xem nội dung Issue dự thảo tại docs/issues/DA01-010.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-01 – DA01-012

Nhiệm vụ: Nghiên cứu và tự viết PCA qua SVD.

Giai đoạn: P7 Build; milestone: M3 Core and Validation; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: models/giam_chieu.py phần PCA; tests PCA.

Tiêu chí nghiệm thu: Có centering, transform/inverse, variance; test so sklearn sau tự viết; xử lý dấu và cơ sở suy biến.

Phụ thuộc: DA01-004, DA01-006. Xem nội dung Issue dự thảo tại docs/issues/DA01-012.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-02 – DA01-014

Nhiệm vụ: Tự viết LDA Fisher và kiểm chứng.

Giai đoạn: P7 Build; milestone: M3 Core and Validation; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: models/giam_chieu.py phần LDA; tests LDA.

Tiêu chí nghiệm thu: Tính scatter/hướng chiếu 1D, xử lý suy biến; cosine đối chiếu ≥0.999 theo quy ước khớp.

Phụ thuộc: DA01-012. Xem nội dung Issue dự thảo tại docs/issues/DA01-014.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-03 – DA01-016

Nhiệm vụ: Tự viết metrics và runner chia fold.

Giai đoạn: P7 Build; milestone: M3 Core and Validation; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: models/metrics.py; experiments/cau_hinh.py; runner/test.

Tiêu chí nghiệm thu: PR-AUC hình thang từ score có xử lý ties; seed một chỗ; đúng 25 bộ chia phân tầng; inner tuning thiết kế rõ.

Phụ thuộc: DA01-004, DA01-007, DA01-010, DA01-012, DA01-014. Xem nội dung Issue dự thảo tại docs/issues/DA01-016.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-04 – DA01-018

Nhiệm vụ: Cài đủ baseline và cấu hình tinh chỉnh công bằng.

Giai đoạn: P7 Build; milestone: M3 Core and Validation; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: baseline configs; tests đối chiếu; kết quả pilot.

Tiêu chí nghiệm thu: Đoán âm, unweighted LR, balanced sklearn, RF; pilot thật có provenance; không gọi pilot là kết quả cuối.

Phụ thuộc: DA01-007, DA01-010, DA01-016. Xem nội dung Issue dự thảo tại docs/issues/DA01-018.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-05 – DA01-020

Nhiệm vụ: Chạy quét k và baseline vòng đầy đủ đầu tiên.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: results/fold_metrics.csv; metadata và nhật ký chạy.

Tiêu chí nghiệm thu: Đủ 25 lần đo cho MỖI cấu hình bắt buộc; cùng fold; preprocessing train-only; không chọn threshold trên evaluation. Thiếu record thì chưa nghiệm thu, ghi rõ phần thiếu.

Phụ thuộc: DA01-009, DA01-010, DA01-012, DA01-014, DA01-016, DA01-018. Xem nội dung Issue dự thảo tại docs/issues/DA01-020.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-06 – DA01-022

Nhiệm vụ: Phân tích quét k và kiểm định ghép cặp.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: results/summary.csv; bảng p-value; docs/analysis/k_findings.md.

Tiêu chí nghiệm thu: Mean ± std, Wilcoxon cùng cặp, ghi giới hạn CV/tuning; không kết luận thắng khi thiếu bằng chứng.

Phụ thuộc: DA01-020. Xem nội dung Issue dự thảo tại docs/issues/DA01-022.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-07 – DA01-024

Nhiệm vụ: Nghiên cứu và tự viết Brier/reliability/PAVA.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: models/calibration.py; tests PAVA/Brier.

Tiêu chí nghiệm thu: Calibration tách phần fit; PAVA đơn điệu và xử lý ties; reliability/Brier test trên ví dụ nhỏ.

Phụ thuộc: DA01-016, DA01-020. Xem nội dung Issue dự thảo tại docs/issues/DA01-024.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-08 – DA01-026

Nhiệm vụ: Thực nghiệm hiệu chuẩn và tối ưu ngưỡng theo chi phí.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: results/calibration.csv; reliability ≥3 k; threshold tables.

Tiêu chí nghiệm thu: Quét tỷ số 5–100, Brier theo k cạnh PR-AUC, không fit/tune trên outer evaluation/test cuối.

Phụ thuộc: DA01-020, DA01-024. Xem nội dung Issue dự thảo tại docs/issues/DA01-026.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-09 – DA01-028

Nhiệm vụ: Tổng hợp kết quả chính và mở rộng.

Giai đoạn: P7 Build; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: hình/bảng calibration, k, baseline; dự thảo kết luận.

Tiêu chí nghiệm thu: Các câu kết luận có số thật và uncertainty; phân biệt AP/PR-AUC; đủ hướng mở rộng và ghi thất bại.

Phụ thuộc: DA01-022, DA01-026. Xem nội dung Issue dự thảo tại docs/issues/DA01-028.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-10 – DA01-030

Nhiệm vụ: Khóa cấu hình và đánh giá test cuối.

Giai đoạn: P9 Finalize; milestone: M4 Experiments and Application; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: manifest cấu hình khóa; kết quả test cuối riêng.

Tiêu chí nghiệm thu: Chốt mọi quyết định trước mở test; không dùng test để sửa ngưỡng; phân biệt CV mean/std với số test cuối.

Phụ thuộc: DA01-028. Xem nội dung Issue dự thảo tại docs/issues/DA01-030.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-11 – DA01-032

Nhiệm vụ: Viết phương pháp/kết quả và ví dụ tính tay PCA.

Giai đoạn: P9 Finalize; milestone: M5 Defense Readiness; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: bản báo cáo phần Luân; phép tính PCA 6 điểm.

Tiêu chí nghiệm thu: Công thức có nguồn, 6 bệnh nhân 2 biến/3+3; đủ covariance/eigen/projection; bảng khớp CSV.

Phụ thuộc: DA01-022, DA01-028, DA01-030. Xem nội dung Issue dự thảo tại docs/issues/DA01-032.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-12 – DA01-034

Nhiệm vụ: Review thống kê và soạn slide/câu hỏi bảo vệ.

Giai đoạn: P9 Finalize; milestone: M5 Defense Readiness; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: slide bản đầu; câu hỏi/đáp; review báo cáo.

Tiêu chí nghiệm thu: Giải thích được weights/PCA/LDA/calibration/leakage; mọi số khớp hiện vật; hạn chế được nêu.

Phụ thuộc: DA01-028, DA01-032. Xem nội dung Issue dự thảo tại docs/issues/DA01-034.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-13 – DA01-036

Nhiệm vụ: Kiểm tra tái lập và manifest phiên bản.

Giai đoạn: P9 Finalize; milestone: M5 Defense Readiness; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: requirements khóa; log tái lập; manifest kết quả.

Tiêu chí nghiệm thu: Ghi Python/packages/seed/hash thật; tạo lại bảng/hình từ results; chỉ báo checks đã thực chạy.

Phụ thuộc: DA01-028, DA01-030, DA01-034. Xem nội dung Issue dự thảo tại docs/issues/DA01-036.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-14 – DA01-038

Nhiệm vụ: Diễn tập thuật toán, kết luận và review cuối.

Giai đoạn: P9 Finalize; milestone: M5 Defense Readiness; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: slide cuối; bảng kiểm nghiệm thu; câu trả lời.

Tiêu chí nghiệm thu: Cả hai trả lời chéo được, không đọc số bịa; ghi hạng mục chưa đạt, không tự tick đủ.

Phụ thuộc: DA01-034, DA01-036, DA01-037. Xem nội dung Issue dự thảo tại docs/issues/DA01-038.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-15 – DA01-040

Nhiệm vụ: Trình bày nghiên cứu và ghi câu hỏi/kết quả trao đổi.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P0 Critical. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: ghi chú câu hỏi, phản hồi và hành động tiếp.

Tiêu chí nghiệm thu: Giải thích phần thuật toán/thực nghiệm; chỉ ghi phản hồi thật và ai trả lời.

Phụ thuộc: DA01-037, DA01-038. Xem nội dung Issue dự thảo tại docs/issues/DA01-040.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-16 – DA01-042

Nhiệm vụ: Rà soát phương pháp theo góp ý và kết quả thật.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: danh sách sửa báo cáo/thuật toán nếu cần.

Tiêu chí nghiệm thu: Phân biệt sửa trình bày với cần chạy lại; không chỉnh số để đẹp.

Phụ thuộc: DA01-039, DA01-040. Xem nội dung Issue dự thảo tại docs/issues/DA01-042.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-17 – DA01-044

Nhiệm vụ: Sửa phân tích/báo cáo theo vấn đề đã xác nhận.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: PR tài liệu hoặc kết quả chạy lại nếu cần.

Tiêu chí nghiệm thu: Mọi bảng mới có provenance; không chạy lại rộng nếu không có lý do.

Phụ thuộc: DA01-041, DA01-042. Xem nội dung Issue dự thảo tại docs/issues/DA01-044.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-18 – DA01-046

Nhiệm vụ: Tổng hợp minh chứng đóng góp của Luân.

Giai đoạn: P8 Tracking; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: CONTRIBUTION_REPORT phần Luân; link Issue/PR/test/result.

Tiêu chí nghiệm thu: Tự tổng hợp việc thật bằng tài khoản cá nhân; Trí kiểm tra AC và evidence.

Phụ thuộc: DA01-044. Xem nội dung Issue dự thảo tại docs/issues/DA01-046.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-19 – DA01-048

Nhiệm vụ: Viết tự thuật cá nhân và kiểm tra tài liệu tham khảo.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: tự thuật Luân; bibliography/license review.

Tiêu chí nghiệm thu: Nguồn thực vận dụng, giấy phép đúng; Trí review tính trung thực.

Phụ thuộc: DA01-045, DA01-046. Xem nội dung Issue dự thảo tại docs/issues/DA01-048.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-20 – DA01-050

Nhiệm vụ: Rà soát test, cấu hình và kết luận lần cuối.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: log kiểm tra có chọn lọc; bảng kết quả cuối.

Tiêu chí nghiệm thu: Không còn khác biệt giữa Word/slide/results; lỗi có thật mới chạy lại tests liên quan.

Phụ thuộc: DA01-043, DA01-044, DA01-047, DA01-048. Xem nội dung Issue dự thảo tại docs/issues/DA01-050.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-21 – DA01-052

Nhiệm vụ: Review Release candidate và tái lập tối thiểu.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: review bản dự kiến; manifest ký nhận bằng Issue/PR.

Tiêu chí nghiệm thu: Kiểm tra nạp mô hình/hình/báo cáo; ghi giới hạn và phần chưa chạy.

Phụ thuộc: DA01-049, DA01-050, DA01-051. Xem nội dung Issue dự thảo tại docs/issues/DA01-052.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

## 2026-12-22 – DA01-054

Nhiệm vụ: Đối chiếu bản nộp và chốt báo cáo đóng góp.

Giai đoạn: P9 Finalize; milestone: M6 Submission; ưu tiên: P1 High. Bắt đầu và hạn trong ngày ghi trên; nếu chưa xong cập nhật Issue thật và nguyên nhân.

Sản phẩm bàn giao: xác nhận bản nộp/manifest; hồ sơ Luân cuối.

Tiêu chí nghiệm thu: Bản nộp khớp Release; bảng công việc phản ánh kết quả thật; vấn đề còn lại được ghi rõ.

Phụ thuộc: DA01-052, DA01-053. Xem nội dung Issue dự thảo tại docs/issues/DA01-054.md; gắn số/link Issue thật sau khi nhập GitHub.

Cuối buổi: ghi việc tự làm, điều đã học, evidence, kiểm tra, khó khăn và bước tiếp; Trí kiểm tra và quyết định nghiệm thu (tự kiểm tra nếu là phần Trí làm). Chưa có minh chứng thì không ghi Done.

Ngày trong bảng là mốc kế hoạch; có thể bắt đầu sớm khi đầu vào đã sẵn sàng. Phụ thuộc dùng để nghiệm thu phần tích hợp; phần nghiên cứu/khung giao diện có thể làm song song. Xem docs/HANDOFFS.md.

## Nghiệm thu và bảo vệ

Giải thích được phần mình làm; ghi công đúng người và phần AI hỗ trợ; hoàn thành hồ sơ thật, không tạo commit hộ hoặc tự thuật thành tích chưa thực hiện. Lịch bảo vệ/nộp theo tài liệu lớp cần theo dõi nếu có thay đổi.
