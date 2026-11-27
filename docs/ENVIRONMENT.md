# Chuẩn bị môi trường sau khi chốt nghiên cứu

Hiện có tài liệu, CSV và công cụ kiểm kê dùng thư viện chuẩn Python; có thể đọc/kiểm kê ngay, không cần cài toàn bộ thư viện học máy. Chưa xác nhận môi trường học máy chung trên hai máy hoặc chạy test thuật toán. Máy AI kiểm tra có Python 3.14.7; phiên bản đích đề xuất cho phần học máy là 3.12, cần hai người kiểm tra và thống nhất, không tự thay Python hệ thống.

## Bước kiểm tra

```powershell
git --version
py -0p
python --version
```

Nếu không có py launcher, dùng đường dẫn python.exe đã cài. Không xóa/đổi môi trường Python hệ thống. Khi Python 3.12 sẵn có, tại root dự án:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip --version
```

Dùng đường dẫn đầy đủ như trên thì không phải thay PowerShell ExecutionPolicy để activate. Sau khi nhóm duyệt thư viện, cài vào .venv: numpy, scipy, pandas, scikit-learn, matplotlib, seaborn, fastapi, uvicorn, pytest, httpx. Không cài đồng loạt trong giai đoạn phân tích nếu chưa cần.

Sau cài chạy import/version smoke test, ghi lỗi thật, sửa tương thích rồi khóa requirements.txt. Có thể dùng pip freeze trong venv sạch để ghi nhận phiên bản đã kiểm chứng, sau đó thử lại trên máy còn lại. Không ghi “đã khóa và chạy được” khi chưa thử.

Lỗi phổ biến: ModuleNotFoundError → kiểm tra đúng .venv/python; không tìm Python 3.12 → cài từ nguồn chính thức hoặc thống nhất phiên bản có sẵn; quyền activate → dùng đường dẫn python trực tiếp; thiếu wheel khi offline → chuẩn bị trên cùng Python/OS/kiến trúc. Không cài thư viện vào base Conda chỉ để chữa lỗi dự án.

Chưa có lệnh chạy app/experiment. Mỗi thành phần sau này kèm giải thích, một bài kiểm thử có ý nghĩa và hướng dẫn chạy trước khi chuyển thành phần tiếp theo.
