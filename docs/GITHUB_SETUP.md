# Khởi tạo GitHub từ bộ hồ sơ cục bộ

## Trạng thái đã xác minh

Trí đã khởi tạo repository, commit và push bằng tài khoản cá nhân; main cục bộ đang theo dõi origin/main. Git có sẵn; GitHub CLI chưa được xác nhận cài. Chưa xác minh Project, Issue hoặc lời mời Luân từ xa. Các bước tạo repo bên dưới dành cho dự án chưa khởi tạo; không git init hoặc tạo repo trùng lần nữa.

Tên đề xuất: ml-stroke-da01-nhom17, owner huynhtamtri2006-gif, visibility Private. Luân cung cấp username trước khi mời/gán việc thật.

## Cách bằng trình duyệt

1. Trí đăng nhập tài khoản huynhtamtri2006-gif, vào https://github.com/new . Owner chọn chính tài khoản này; Repository name nhập ml-stroke-da01-nhom17.
2. Chọn Private. Để trống lựa chọn tạo README, .gitignore, license vì bộ cục bộ đã có. Create repository.
3. Trong repository → Settings → Collaborators hoặc Collaborators and teams → Add people; nhập username Luân, gửi lời mời. Luân tự chấp nhận bằng tài khoản cá nhân. Nếu cần giảng viên xem repo Private, mời đúng tài khoản được cung cấp.
4. Kiểm tra biểu tượng Private; chưa đổi Public. Cấp quyền Project riêng theo PROJECTS_SETUP.md; có quyền repo không tự bảo đảm có quyền Project.

## Đưa bộ file lên bằng Git cá nhân

Mở PowerShell tại thư mục dự án. Thay email mẫu bằng email/noreply của chính Trí; không để nguyên email mẫu.

```powershell
Set-Location 'D:\ML - CUOI KY\do_an_DA01_nhom17'
git init -b main
git config --local user.name 'Huynh Tam Tri'
git config --local user.email 'THAY_BANG_EMAIL_GITHUB_CUA_TRI'
git status --short
git add .
git diff --cached --stat
git diff --cached
```

Đọc danh sách trước khi commit: không có kaggle.json, token, .env, mật khẩu hoặc tệp tạm Office. CSV Stroke đúng tên là ngoại lệ do Trí yêu cầu đưa vào repo kèm nguồn/hash; raw khác vẫn loại trừ. Commit có AI hỗ trợ cần ghi đúng, không tuyên bố Trí tự viết toàn bộ hoặc Luân đã hoàn thành nghiên cứu.

```powershell
git commit -m 'docs: initialize project planning with disclosed AI assistance'
git remote add origin https://github.com/huynhtamtri2006-gif/ml-stroke-da01-nhom17.git
git push -u origin main
git remote -v
git log -1 --oneline
```

Git có thể mở đăng nhập trình duyệt qua credential manager. Không gửi token trong chat, không thêm token vào URL/README. Nếu remote đã tồn tại, dùng git remote -v kiểm tra trước; không thêm origin lần hai. Nếu remote đã có commit, clone ra thư mục khác rồi copy nội dung cần thiết vào nhánh mới, không force push.

Sau đó Luân clone bằng lệnh trong CONTRIBUTING.md và đặt git config --local theo danh tính của Luân.

## Tùy chọn dùng CLI sau khi tự cài

Theo https://cli.github.com/ để cài GitHub CLI cho Windows nếu cần tự động hóa. Không bắt buộc dùng CLI để tạo repo/Projects. Khi đã cài, mở PowerShell mới:

```powershell
gh auth login --hostname github.com --web
gh auth status
gh repo view huynhtamtri2006-gif/ml-stroke-da01-nhom17 --json nameWithOwner,visibility
```

Không chạy gh repo create nếu đã tạo cùng repo trong trình duyệt. Nếu chọn CLI thay bước tạo bằng web, tại bộ thư mục đã init/commit, có thể dùng gh repo create huynhtamtri2006-gif/ml-stroke-da01-nhom17 --private --source . --remote origin --push, chỉ khi repo và origin chưa tồn tại.

## Tạo Issue sớm

Mỗi nhiệm vụ có bản nội dung trong docs/issues/ và metadata trong docs/tasks/task_manifest.csv. Task ID DA01-001 không là số Issue #1; lưu ánh xạ số thật vào docs/tasks/issue_map.json sau khi tạo.

Tạo thủ công: repository → Issues → New issue, copy title/body từ file, chọn assignee thật, milestone, rồi thêm vào Project. Nếu chưa biết username Luân để trống assignee, giữ tên người chịu trách nhiệm trong body; không gán hết cho Trí rồi gọi là đóng góp của Luân.

Tùy chọn nhập tất cả bằng tools/publish_issues.ps1 sau khi có gh. Chạy mặc định chỉ xem trước. Ví dụ (thay username Luân):

```powershell
.\tools\publish_issues.ps1 -LuanUsername 'USERNAME_LUAN'
.\tools\publish_issues.ps1 -LuanUsername 'USERNAME_LUAN' -Execute
```

Script kiểm tra đúng repo Private, đọc Issue đang có để tránh tạo trùng Task ID, tạo milestone và Issue; không tự cập nhật custom field Project. Sau mỗi lần chạy đọc issue_map.json và kiểm tra trên GitHub. Tác vụ chưa nhập vẫn là bản dự thảo cục bộ.

Nguồn: [Tạo repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository); [GitHub CLI](https://cli.github.com/).
