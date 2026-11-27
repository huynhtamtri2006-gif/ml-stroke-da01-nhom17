# Quy trình đóng góp của hai thành viên

main giữ bản có thể kiểm tra; mỗi Issue một nhánh ngắn. Không cần develop. Tên: docs/da01-001-research, feat/da01-017-logistic, fix/da01-020-gradient, test/da01-018-leakage. Task ID khác số Issue GitHub: thay #NUMBER bằng số thật khi liên kết.

Commit: docs(research): summarize PR-AUC rationale; feat(logistic): add weighted loss; test(pca): verify reconstruction. Dùng git config --local với tên thật và email GitHub cá nhân/noreply. Không cấu hình danh tính của người khác, không commit hộ để tạo đóng góp.

## Một vòng làm việc

```powershell
git switch main
git pull --ff-only
git switch -c docs/da01-001-research
# Chỉnh file, đọc lại thay đổi và chạy kiểm tra phù hợp
git status
git diff
git add docs/RESEARCH_FILE.md
git commit -m "docs(research): document findings for DA01-001"
git push -u origin docs/da01-001-research
```

Đường dẫn docs/RESEARCH_FILE.md là ví dụ, thay bằng file thật mình vừa viết. PR ghi Fixes #NUMBER khi hoàn tất Issue; dùng Refs #NUMBER nếu chỉ một phần. Trí là người giám sát và quyết định nghiệm thu/merge. PR của Luân phải được Trí review; Luân không tự merge vào main. Trí tự kiểm tra PR của mình và quyết định merge, không cần Luân phê duyệt. Luân có thể góp ý khi được yêu cầu. Tự kiểm tra không có nghĩa là GitHub cho phép tác giả tự Approve PR. Nêu mục tiêu, thay đổi, cách kiểm tra, minh chứng và giới hạn. Chỉ merge sau đạt AC, có minh chứng và Trí quyết định nghiệm thu; PR của Luân cần Trí review trước; có thể squash nếu vẫn giữ tác giả thực tế và minh chứng.

## Clone và đồng bộ

```powershell
git clone https://github.com/huynhtamtri2006-gif/ml-stroke-da01-nhom17.git
cd ml-stroke-da01-nhom17
git switch main
git pull --ff-only
```

Clone chỉ sau repo thật được tạo và được cấp quyền. Không dùng git pull để trộn một remote README khác vào bộ khởi tạo; tạo remote rỗng như GITHUB_SETUP.md.

## Merge conflict

Commit/cất thay đổi đang làm trước; ở nhánh nhiệm vụ chạy git fetch origin rồi git merge origin/main. Dùng git status tìm file xung đột, mở từng vùng <<<<<<< ======= >>>>>>>, đọc hai ý định và giữ nội dung đúng, xóa marker, chạy lại kiểm tra. git add từng file đã sửa, git commit, git push. Nếu chưa hiểu, dùng git merge --abort để quay về trước merge và nhờ người còn lại đọc; không dùng reset --hard hoặc force push lên main. File Word là nhị phân: chia người biên tập, không chỉnh đồng thời.

## Kết thúc buổi làm

Cập nhật Issue với: việc thực làm, kết quả/đường dẫn/commit/PR, kiểm tra đã chạy, lỗi và bước tiếp. Ghi Actual Hours chỉ nếu nhóm muốn theo dõi; không bắt buộc số giờ/ngày. Cập nhật Status và Progress có căn cứ. Đang chờ review không là Done; thiếu acceptance/evidence không ghi 100%.

Review kiểm tra đúng yêu cầu, hiểu công thức, không leakage, tests thật, source/license, không secret. Không chấm thành viên theo số commit đơn thuần. Repository hiện Public: bất kỳ ai có thể đọc/clone; chỉ thành viên có quyền phù hợp mới push được vào repo. Luân push nhánh nhiệm vụ và tạo PR; Trí đọc và quyết định merge main. Public không tự chặn push main: Trí cần bật Rulesets/bảo vệ nhánh phù hợp để cưỡng chế quy trình; chưa xác minh cấu hình thực tế.

## Quyền nghiệm thu và bảo vệ main

Chỉ Trí quyết định merge vào main. Luân làm trên nhánh riêng và gửi PR; góp ý kỹ thuật không đồng nghĩa có quyền nghiệm thu hoặc merge. Tài liệu không tự thay đổi quyền GitHub. Cần kiểm tra Ruleset để chỉ Trí được cập nhật main qua PR/bypass, không cấp quyền bypass cho Luân. Nếu PR của Trí bị chặn vì thiếu approval, Trí có thể dùng quyền bypass đã được cấp sau khi tự kiểm tra; không ghi giả rằng Luân đã duyệt.
