# Thiết lập GitHub Projects cho nhóm 17

## Tạo Project và quyền

Trí mở trang cá nhân GitHub → Projects → New project → Table → tên DA01 Nhom17 Research and Delivery. Repository hiện Public; **Project có visibility và quyền riêng**, có thể giữ Private để quản lý nội bộ. Thêm Luân ở Manage access với quyền Write, Trí giữ Admin; đọc được repo Public không tự có quyền sửa Project. Không tự đổi Project sang Public nếu nhóm chưa chọn. Liên kết Project vào repo và thêm Issue thật, tránh chỉ để draft item khi cần theo dõi PR/đóng góp.

Nguồn: [Creating a project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project); [Managing project access](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-access-to-your-projects).

## Các trường

Trong Table, nút + bên phải cột → New field. Giữ các trường có sẵn, không tạo bản sao. Tên trường sau đây là tên dùng trong hướng dẫn filter.

| Thông tin yêu cầu | Nơi lưu | Kiểu và cách dùng |
|---|---|---|
| Task ID | Custom Task ID | Text, DA01-001; giữ cả prefix trong title Issue |
| Task Name | Title sẵn có | Tên Issue; không tạo custom trùng |
| Description | Issue body | Mục tiêu, bối cảnh, các bước |
| Assignee | Assignees sẵn có | GitHub username thật, không nhập MSSV vào đây |
| Phase | Custom Phase | Single select: P1 Research; P2 Design; P3 Repository; P4 Projects; P5 Planning; P6 Workflow; P7 Build; P8 Tracking; P9 Finalize |
| Status | Status sẵn có, sửa options | Backlog, To Do, Researching, In Progress, In Review, Testing, Blocked, Done |
| Priority | Custom Priority | Single select: P0 Critical, P1 High, P2 Normal |
| Start Date | Custom Start Date | Date, YYYY-MM-DD |
| Due Date | Custom Due Date | Date, YYYY-MM-DD |
| Progress (%) | Custom Progress | Number 0–100; đơn vị phần trăm |
| Estimated Hours | Custom Estimated Hours | Number; để trống, không ấn định giờ/ngày |
| Actual Hours | Custom Actual Hours | Number; chỉ nhập nếu theo dõi giờ thực |
| Deliverables | Issue body | File/chức năng/kết quả phải bàn giao |
| Dependencies | Issue body và quan hệ Issue nếu có | Task ID kèm link Issue thật; chưa có link thì ghi ID |
| Acceptance Criteria | Issue body | Checklist kiểm chứng được |
| Evidence | Issue body | Link commit, PR, tài liệu, test/result; không tự xem là đã có |
| Notes | Issue body | Vướng mắc, quyết định, bước tiếp |

Có thể thêm Iteration tên Week để nhóm theo tuần. Không tạo custom text cho mọi mục dài; nội dung dài ở Issue body dễ review và không tràn Table. CSV là nguồn nhập tay, không tuyên bố GitHub Projects tự nhập CSV đầy đủ.

Nguồn về trường: [Single select](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields), [Text và number](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-text-and-number-fields), [Date](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-date-fields).

## Bảy chế độ hiển thị

| View | Layout và cấu hình |
|---|---|
| Kanban Board | Board, cột theo Status; hiện Assignees, Priority, Due Date |
| Task Table | Table, hiện Task ID, Title, Assignees, Phase, Status, Priority, hai ngày, Progress; sort Due Date |
| Project Roadmap | Roadmap, ngày bắt đầu Start Date/ngày cuối Due Date, group Phase |
| Theo thành viên | Table group Assignees; Trí có thể lọc assignee:huynhtamtri2006-gif; Luân thay username thật |
| Theo tuần | Table group Iteration Week hoặc lọc khoảng Due Date; W1 26–29/11, W2 30/11–06/12, W3 07–13/12, W4 14–20/12, W5 21–22/12 |
| Quá hạn | Table filter -status:Done due-date:<@today (nếu giao diện gợi ý token khác, chọn field Due Date từ autocomplete); chỉ việc có Due Date |
| Ưu tiên | Board hoặc Table group Priority; sort Due Date; loại Done nếu cần |

Filter ngày hỗ trợ YYYY-MM-DD và @today theo tài liệu; khi field có dấu cách dùng tên/token do GitHub autocomplete gợi ý. Kiểm tra view quá hạn bằng một Issue thử có hạn hôm qua, rồi sửa lại hạn thật. Không coi view lưu được là bằng chứng dữ liệu nhập đúng.

Nguồn: [Filtering projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects).

## Quy tắc trạng thái

Backlog → To Do khi rõ phụ thuộc/AC; Researching cho nhiệm vụ học; In Progress khi tạo hiện vật; In Review khi PR/tài liệu sẵn sàng; Testing khi kiểm tra; Done khi Trí quyết định nghiệm thu và có evidence; phần Trí làm do Trí tự kiểm tra, phần Luân làm phải được Trí review. Blocked phải ghi trở ngại, người xử lý và bước tiếp; không đổi hạn cũ chỉ để giấu trễ. Researching không bắt buộc mọi Issue đi qua; lỗi có thể quay về In Progress.

Thêm workflow “Item closed → Done” nếu phù hợp; chỉ đóng Issue khi AC đạt, không đóng tự động sớm. Không thêm full CV vào Actions. Mỗi buổi cuối ngày cập nhật cả Issue và Project; Progress không tự suy ra từ số commit.
