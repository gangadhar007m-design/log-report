import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_TOTAL = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def test_report_exists():
    """Criterion 1: /app/report.json exists and contains valid JSON."""
    assert REPORT_PATH.exists(), "no report.json found"


def test_report_valid_json():
    """Criterion 1: /app/report.json contains valid JSON."""
    data = json.loads(REPORT_PATH.read_text())
    assert isinstance(data, dict), "report.json is not a JSON object"


def test_total_requests():
    """Criterion 2: total_requests equals the number of non-empty log lines."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["total_requests"] == EXPECTED_TOTAL, (
        f"total_requests: expected {EXPECTED_TOTAL}, got {data['total_requests']}"
    )


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"unique_ips: expected {EXPECTED_UNIQUE_IPS}, got {data['unique_ips']}"
    )


def test_top_path():
    """Criterion 4: top_path equals the most-requested URL path."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["top_path"] == EXPECTED_TOP_PATH, (
        f"top_path: expected {EXPECTED_TOP_PATH}, got {data['top_path']}"
    )
