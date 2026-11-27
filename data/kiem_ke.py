"""Kiểm kê CSV gốc bằng thư viện chuẩn; không biến đổi dữ liệu hay fit mô hình."""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
from statistics import median
import sys

ROOT = Path(__file__).resolve().parents[1]
FILENAME = "healthcare-dataset-stroke-data.csv"
SOURCE = "https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset"
COLUMNS = [
    "id", "gender", "age", "hypertension", "heart_disease", "ever_married",
    "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status", "stroke",
]
CATEGORICAL = ["gender", "ever_married", "work_type", "Residence_type", "smoking_status"]
NUMERIC = ["age", "avg_glucose_level", "bmi"]
MISSING = {"", "n/a", "na", "nan", "null"}


def is_missing(value: str) -> bool:
    # 'Unknown' là giá trị quan sát của smoking_status, không tự coi là ô thiếu.
    return value.strip().lower() in MISSING


def inspect_csv(path: Path) -> dict:
    raw_bytes = path.read_bytes()
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        names = reader.fieldnames or []
        if len(names) != len(set(names)) or set(names) != set(COLUMNS):
            raise ValueError(f"CSV phải có đúng 12 tên cột: {', '.join(COLUMNS)}. Đã đọc: {names}")
        rows = list(reader)
    if not rows:
        raise ValueError("CSV không có dòng dữ liệu.")
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError("Có dòng thừa/thiếu trường; kiểm tra dấu phân cách hoặc file đã chỉnh sửa.")

    missing = {column: sum(is_missing(row[column]) for row in rows) for column in COLUMNS}
    if any(missing[column] for column in COLUMNS if column != "bmi"):
        raise ValueError("Có giá trị thiếu ngoài bmi; kiểm tra CSV và nguồn trước khi phân tích.")
    for column in ("stroke", "hypertension", "heart_disease"):
        observed = {row[column].strip() for row in rows}
        if not observed <= {"0", "1"}:
            raise ValueError(f"Cột {column} có giá trị ngoài 0/1: {sorted(observed)}")

    summaries = {}
    for column in NUMERIC:
        values = []
        for line, row in enumerate(rows, start=2):
            if is_missing(row[column]):
                continue
            try:
                value = float(row[column])
            except ValueError as exc:
                raise ValueError(f"{column}, dòng {line} không phải số.") from exc
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{column}, dòng {line} có giá trị âm/không hữu hạn.")
            values.append(value)
        summaries[column] = {
            "non_missing": len(values),
            "min": min(values) if values else None,
            "median": median(values) if values else None,
            "max": max(values) if values else None,
        }

    labels = Counter(row["stroke"].strip() for row in rows)
    full_records = [tuple(row[column] for column in COLUMNS) for row in rows]
    without_ids = [tuple(row[column] for column in COLUMNS if column != "id") for row in rows]
    counts = {
        "rows": len(rows), "columns": len(names),
        "stroke_0": labels.get("0", 0), "stroke_1": labels.get("1", 0),
        "bmi_missing": missing["bmi"],
    }
    expected = {"rows": 5110, "columns": 12, "stroke_0": 4861, "stroke_1": 249, "bmi_missing": 201}
    warnings = [f"{key}: đo được {counts[key]}, đề ghi {value}" for key, value in expected.items() if counts[key] != value]
    if names != COLUMNS:
        warnings.append("Thứ tự cột khác bản mô tả; tên cột vẫn đầy đủ.")
    return {
        "source_url": SOURCE,
        "filename": path.name,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "bytes": len(raw_bytes), "column_names": names,
        "counts": counts, "expected_from_assignment": expected,
        "positive_rate": labels.get("1", 0) / len(rows),
        "missing_by_column": missing,
        "duplicate_full_rows": len(rows) - len(set(full_records)),
        "duplicate_rows_excluding_id": len(rows) - len(set(without_ids)),
        "duplicate_ids": len(rows) - len({row["id"] for row in rows}),
        "categorical_counts": {column: dict(sorted(Counter(row[column] for row in rows).items())) for column in CATEGORICAL},
        "numeric_summary": summaries,
        "bmi_missing_by_stroke": {label: sum(is_missing(row["bmi"]) and row["stroke"].strip() == label for row in rows) for label in ("0", "1")},
        "warnings": warnings,
        "scope": "Mô tả toàn bộ CSV; không phải kết quả huấn luyện hoặc đánh giá mô hình.",
    }


def markdown_report(info: dict) -> str:
    counts = info["counts"]
    lines = [
        "# Kiểm kê dữ liệu gốc", "",
        f"Nguồn: {info['source_url']}", "",
        f"File: `{info['filename']}`; {info['bytes']} bytes.", "",
        f"SHA-256: `{info['sha256']}`", "",
        f"Thời điểm tạo báo cáo UTC: {info['generated_at_utc']}", "",
        "## Đối chiếu yêu cầu", "", "| Đại lượng | Đo thực tế | Theo đề |", "|---|---:|---:|",
    ]
    lines += [f"| {key} | {value} | {info['expected_from_assignment'][key]} |" for key, value in counts.items()]
    lines += ["", f"Tỷ lệ stroke = 1: {info['positive_rate']:.4%}.", "",
              f"Dòng trùng toàn bộ: {info['duplicate_full_rows']}; trùng khi bỏ id: {info['duplicate_rows_excluding_id']}; id trùng: {info['duplicate_ids']}.", "",
              "## Ô thiếu", "", "| Cột | Số ô thiếu |", "|---|---:|"]
    lines += [f"| {key} | {value} |" for key, value in info["missing_by_column"].items()]
    lines += ["", "Unknown của smoking_status được giữ là một mức, không gộp với ô trống.", "",
              "## Thống kê biến số", "", "| Cột | Không thiếu | Min | Median | Max |", "|---|---:|---:|---:|---:|"]
    lines += [f"| {key} | {value['non_missing']} | {value['min']} | {value['median']} | {value['max']} |" for key, value in info["numeric_summary"].items()]
    lines += ["", "Median ở đây chỉ mô tả CSV; không dùng để điền khuyết trước khi chia dữ liệu.", "",
              "## Mức của biến phân loại", "", "| Cột | Giá trị | Số mẫu |", "|---|---|---:|"]
    for column, values in info["categorical_counts"].items():
        lines += [f"| {column} | {key.replace('|', '/')} | {value} |" for key, value in values.items()]
    lines += ["", f"BMI thiếu theo stroke: {info['bmi_missing_by_stroke']}.", "", "## Cảnh báo đối chiếu", ""]
    lines += [f"- {text}" for text in info["warnings"]] or ["Không có chênh lệch so với năm đại lượng kiểm tra của đề."]
    lines += ["", info["scope"], "", "Nguồn tải và điều kiện chia sẻ cần ghi riêng trong data/PROVENANCE.md; công cụ không xác thực giấy phép hay chứng minh nguồn chỉ bằng số dòng."]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data" / "raw" / FILENAME)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data" / "inventory")
    args = parser.parse_args(argv)
    if not args.input.is_file():
        print(f"CHƯA CÓ CSV: {args.input}\nTải đúng file từ nguồn Kaggle trong data/README.md, giữ nguyên bản gốc.", file=sys.stderr)
        return 1
    try:
        info = inspect_csv(args.input)
    except (ValueError, OSError, UnicodeError, csv.Error) as exc:
        print(f"KHÔNG KIỂM KÊ ĐƯỢC: {exc}", file=sys.stderr)
        return 1
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "inventory.json").write_text(json.dumps(info, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "inventory.md").write_text(markdown_report(info), encoding="utf-8")
    print(json.dumps(info["counts"], ensure_ascii=False))
    print(f"SHA-256: {info['sha256']}\nBáo cáo: {args.output_dir.resolve()}")
    if info["warnings"]:
        print("CÓ CHÊNH LỆCH: " + "; ".join(info["warnings"]))
        return 2
    print("KHỚP số lượng theo đề. Đây chưa phải kiểm chứng mô hình hoặc xác thực nguồn dữ liệu.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
