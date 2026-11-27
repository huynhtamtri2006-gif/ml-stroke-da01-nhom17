"""Kiểm tra công cụ trên dữ liệu nhỏ tự tạo trong thư mục tạm, không phải dataset thật."""

import contextlib
import csv
import hashlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("kiem_ke", ROOT / "data" / "kiem_ke.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "toy.csv"

    def write_rows(self, header=None, bad_label=False):
        rows = [
            [1, "Female", 21.5, 0, 0, "No", "Private", "Urban", 80, "N/A", "Unknown", 0],
            [2, "Male", 60, 1, 0, "Yes", "Self-employed", "Rural", 120, 25, "never smoked", 1],
        ]
        if bad_label:
            rows[1][-1] = 2
        with self.path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(header or module.COLUMNS)
            writer.writerows(rows)

    def test_unknown_missing_and_source_preservation(self):
        self.write_rows()
        before = self.path.read_bytes()
        info = module.inspect_csv(self.path)
        self.assertEqual(info["counts"]["bmi_missing"], 1)
        self.assertEqual(info["missing_by_column"]["smoking_status"], 0)
        self.assertEqual(info["categorical_counts"]["smoking_status"]["Unknown"], 1)
        self.assertEqual(info["counts"]["stroke_1"], 1)
        self.assertEqual(info["numeric_summary"]["age"]["min"], 21.5)
        self.assertEqual(info["sha256"], hashlib.sha256(before).hexdigest())
        self.assertEqual(before, self.path.read_bytes())

    def test_wrong_header_and_invalid_label_fail(self):
        bad_header = module.COLUMNS.copy()
        bad_header[0] = "unexpected"
        self.write_rows(header=bad_header)
        with self.assertRaises(ValueError):
            module.inspect_csv(self.path)
        self.write_rows(bad_label=True)
        with self.assertRaises(ValueError):
            module.inspect_csv(self.path)

    def test_missing_file_does_not_create_report(self):
        output = Path(self.temp.name) / "out"
        with contextlib.redirect_stderr(io.StringIO()):
            status = module.main(["--input", str(self.path), "--output-dir", str(output)])
        self.assertEqual(status, 1)
        self.assertFalse(output.exists())

    def test_noncanonical_counts_are_reported_not_claimed_correct(self):
        self.write_rows()
        output = Path(self.temp.name) / "out"
        with contextlib.redirect_stdout(io.StringIO()):
            status = module.main(["--input", str(self.path), "--output-dir", str(output)])
        self.assertEqual(status, 2)
        self.assertTrue((output / "inventory.json").exists())
        self.assertIn("đo được 2", (output / "inventory.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
