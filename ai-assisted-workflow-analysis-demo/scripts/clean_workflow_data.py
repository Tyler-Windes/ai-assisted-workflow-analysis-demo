import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "workflow_intake_sample.csv"
OUT = ROOT / "data" / "processed" / "workflow_items_clean.csv"

PRIORITY_MAP = {
    "urgent": "High",
    "asap": "High",
    "p1": "High",
    "high": "High",
    "p2": "Medium",
    "medium": "Medium",
    "med": "Medium",
    "p3": "Low",
    "low": "Low",
}

STATUS_MAP = {
    "open": "Open",
    "in progress": "In Progress",
    "in-progress": "In Progress",
    "closed": "Closed",
}

SYSTEM_AREA_MAP = {
    "crm": "CRM",
    "reporting": "Reporting",
    "integration": "Integration",
    "identity": "Identity",
    "workflow": "Workflow",
    "data quality": "Data Quality",
    "unknown": "Needs Review",
}

OUTPUT_FIELDS = [
    "item_id",
    "source",
    "submitted_date",
    "request_type",
    "description",
    "reported_priority",
    "normalized_priority",
    "assigned_team",
    "status",
    "resolution_notes",
    "customer_impact",
    "system_area",
    "duplicate_of",
    "missing_info_flag",
]


def normalize_priority(value: str) -> str:
    return PRIORITY_MAP.get((value or "").strip().lower(), "Needs Review")


def normalize_status(value: str) -> str:
    return STATUS_MAP.get((value or "").strip().lower(), "Needs Review")


def normalize_system_area(value: str) -> str:
    cleaned = (value or "").strip().lower()
    return SYSTEM_AREA_MAP.get(cleaned, cleaned.title() if cleaned else "Needs Review")


def normalize_bool(value: str) -> str:
    cleaned = (value or "").strip().lower()
    if cleaned in {"true", "yes", "1"}:
        return "true"
    if cleaned in {"false", "no", "0"}:
        return "false"
    return "true"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    with RAW.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        for key, value in list(row.items()):
            row[key] = (value or "").strip()

        row["normalized_priority"] = normalize_priority(row.get("reported_priority", ""))
        row["status"] = normalize_status(row.get("status", ""))
        row["system_area"] = normalize_system_area(row.get("system_area", ""))
        row["missing_info_flag"] = normalize_bool(row.get("missing_info_flag", ""))

    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
