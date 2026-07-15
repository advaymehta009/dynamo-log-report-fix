import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Ground truth computed independently from environment/access.log:
# 6 requests total; IPs 192.168.0.1, 192.168.0.2, 10.0.0.5 -> 3 unique;
# /index.html x3, /about.html x2, /api/login x1 -> top_path = /index.html
EXPECTED = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def _load_report():
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_is_valid_json():
    """Criterion 1: /app/report.json exists and is valid JSON."""
    report = _load_report()
    assert isinstance(report, dict), "report.json does not contain a JSON object"


def test_report_has_required_keys():
    """Criterion 2: the JSON object contains exactly total_requests, unique_ips, top_path."""
    report = _load_report()
    assert set(report.keys()) == set(EXPECTED.keys()), (
        f"expected keys {set(EXPECTED.keys())}, got {set(report.keys())}"
    )


def test_total_requests():
    """Criterion 3: total_requests matches the number of requests in access.log."""
    report = _load_report()
    assert report["total_requests"] == EXPECTED["total_requests"], (
        f"expected total_requests={EXPECTED['total_requests']}, got {report['total_requests']}"
    )


def test_unique_ips():
    """Criterion 4: unique_ips matches the number of distinct client IPs in access.log."""
    report = _load_report()
    assert report["unique_ips"] == EXPECTED["unique_ips"], (
        f"expected unique_ips={EXPECTED['unique_ips']}, got {report['unique_ips']}"
    )


def test_top_path():
    """Criterion 5: top_path matches the single most frequently requested path in access.log."""
    report = _load_report()
    assert report["top_path"] == EXPECTED["top_path"], (
        f"expected top_path={EXPECTED['top_path']!r}, got {report['top_path']!r}"
    )