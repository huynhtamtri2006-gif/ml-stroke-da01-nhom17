# tests

Hiện có kiểm thử công cụ kiểm kê dữ liệu. Chạy từ thư mục gốc, không cần pytest:

```powershell
python -m unittest discover -s tests -p "test_kiem_ke.py" -v
```

Test dùng dữ liệu nhỏ tự tạo trong thư mục tạm để kiểm tra missing/Unknown, schema/nhãn sai, thiếu file, hash/bảo toàn raw và cảnh báo số lượng khác đề. Kết quả test không phải kiểm kê dataset hoặc thực nghiệm mô hình.

Chưa có test Logistic/PCA/LDA/metrics học máy, train-only preprocessing và save/load; sẽ bổ sung cùng thuật toán. Chưa thêm CI ở bước này.
