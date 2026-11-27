# Kiểm kê dữ liệu gốc

Nguồn: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

File: `healthcare-dataset-stroke-data.csv`; 316971 bytes.

SHA-256: `644d473b05d2797006bd94865e4f8bb057f0c721617911613c82c8fcfc707420`

Thời điểm tạo báo cáo UTC: 2026-11-27T05:46:37+00:00

## Đối chiếu yêu cầu

| Đại lượng | Đo thực tế | Theo đề |
|---|---:|---:|
| rows | 5110 | 5110 |
| columns | 12 | 12 |
| stroke_0 | 4861 | 4861 |
| stroke_1 | 249 | 249 |
| bmi_missing | 201 | 201 |

Tỷ lệ stroke = 1: 4.8728%.

Dòng trùng toàn bộ: 0; trùng khi bỏ id: 0; id trùng: 0.

## Ô thiếu

| Cột | Số ô thiếu |
|---|---:|
| id | 0 |
| gender | 0 |
| age | 0 |
| hypertension | 0 |
| heart_disease | 0 |
| ever_married | 0 |
| work_type | 0 |
| Residence_type | 0 |
| avg_glucose_level | 0 |
| bmi | 201 |
| smoking_status | 0 |
| stroke | 0 |

Unknown của smoking_status được giữ là một mức, không gộp với ô trống.

## Thống kê biến số

| Cột | Không thiếu | Min | Median | Max |
|---|---:|---:|---:|---:|
| age | 5110 | 0.08 | 45.0 | 82.0 |
| avg_glucose_level | 5110 | 55.12 | 91.88499999999999 | 271.74 |
| bmi | 4909 | 10.3 | 28.1 | 97.6 |

Median ở đây chỉ mô tả CSV; không dùng để điền khuyết trước khi chia dữ liệu.

## Mức của biến phân loại

| Cột | Giá trị | Số mẫu |
|---|---|---:|
| gender | Female | 2994 |
| gender | Male | 2115 |
| gender | Other | 1 |
| ever_married | No | 1757 |
| ever_married | Yes | 3353 |
| work_type | Govt_job | 657 |
| work_type | Never_worked | 22 |
| work_type | Private | 2925 |
| work_type | Self-employed | 819 |
| work_type | children | 687 |
| Residence_type | Rural | 2514 |
| Residence_type | Urban | 2596 |
| smoking_status | Unknown | 1544 |
| smoking_status | formerly smoked | 885 |
| smoking_status | never smoked | 1892 |
| smoking_status | smokes | 789 |

BMI thiếu theo stroke: {'0': 161, '1': 40}.

## Cảnh báo đối chiếu

Không có chênh lệch so với năm đại lượng kiểm tra của đề.

Mô tả toàn bộ CSV; không phải kết quả huấn luyện hoặc đánh giá mô hình.

Nguồn tải và điều kiện chia sẻ cần ghi riêng trong data/PROVENANCE.md; công cụ không xác thực giấy phép hay chứng minh nguồn chỉ bằng số dòng.
