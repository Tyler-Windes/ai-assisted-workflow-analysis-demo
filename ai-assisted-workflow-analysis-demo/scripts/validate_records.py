from __future__ import annotations

import csv
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "processed" / "workflow_items_clean.csv"
OUTPUT_PATH = ROOT / "data" / "processed" / "workflow_items_validated.csv"
REPORT_PATH = ROOT / "reports" / "data_quality_findings.md"

VALID_PRIORITIES = {"Low", "Medium", "High", "Needs Review"}
VALID_STATUSES = {"Open", "In Progress", "Closed", "Needs Review"}
VALID_IMPACTS = {"Low", "Medium", "High"}
VALID_SYSTEM_AREAS = {
    "CRM",
    "Data Quality",
    "Identity",
    "Integration",
    "Reporting",
    "Workflow",
    "Needs Review",
}
BOOLEAN_VALUES = {"true", "false", "True", "False", ""}


def is_valid_date(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_blank(value: str | None) -> bool:
    return value is None or value.strip() == ""


def validate_row(row: dict[str, str]) -> list[str]:
    issues: list[str] = []

    item_id = row.get("item_id", "").strip()
    status = row.get("status", "").strip()
    normalized_priority = row.get("normalized_priority", "").strip()
    assigned_team = row.get("assigned_team", "").strip()
    resolution_notes = row.get("resolution_notes", "").strip()
    submitted_date = row.get("submitted_date", "").strip()
    customer_impact = row.get("customer_impact", "").strip()
    system_area = row.get("system_area", "").strip()
    missing_info_flag = row.get("missing_info_flag", "").strip()
    duplicate_of = row.get("duplicate_of", "").strip()

    required_fields = [
        "item_id",
        "source",
        "submitted_date",
        "request_type",
        "description",
        "reported_priority",
        "normalized_priority",
        "status",
        "customer_impact",
        "system_area",
        "missing_info_flag",
    ]

    for field in required_fields:
        if is_blank(row.get(field)):
            issues.append(f"Missing required field: {field}")

    if submitted_date and not is_valid_date(submitted_date):
        issues.append("Submitted date is not in YYYY-MM-DD format")

    if normalized_priority not in VALID_PRIORITIES:
        issues.append("Priority needs review")

    if status not in VALID_STATUSES:
        issues.append("Status needs review")

    if customer_impact not in VALID_IMPACTS:
        issues.append("Customer impact needs review")

    if system_area not in VALID_SYSTEM_AREAS:
        issues.append("System area needs review")

    if missing_info_flag not in BOOLEAN_VALUES:
        issues.append("Missing-info flag needs review")

    if status == "In Progress" and is_blank(assigned_team):
        issues.append("In-progress record missing assigned team")

    if status == "Closed" and is_blank(resolution_notes):
        issues.append("Closed record missing resolution notes")

    if duplicate_of and duplicate_of == item_id:
        issues.append("Duplicate reference points to same record")

    if missing_info_flag.lower() == "true":
        issues.append("Record marked as missing information")

    return issues


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_rows(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_report(rows: list[dict[str, str]]) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    issue_counter: Counter[str] = Counter()
    flagged_rows = []

    for row in rows:
        issues = [issue for issue in row.get("validation_issues", "").split("; ") if issue]
        if issues:
            flagged_rows.append(row)
            issue_counter.update(issues)

    lines: list[str] = [
        "#### Data Quality Findings",
        "",
        "This report is based on fictional sample data.",
        "",
        f"Records reviewed: {len(rows)}",
        "",
        f"Records with findings: {len(flagged_rows)}",
        "",
        "##### Summary by Issue Type",
        "",
    ]

    if issue_counter:
        for issue, count in sorted(issue_counter.items()):
            lines.append(f"- {issue}: {count}")
    else:
        lines.append("- No validation findings identified")

    lines.extend(
        [
            "",
            "##### Record-Level Findings",
            "",
        ]
    )

    if flagged_rows:
        for row in flagged_rows:
            lines.extend(
                [
                    f"###### {row.get('item_id', 'Unknown')}",
                    "",
                    f"- Status: {row.get('status', '')}",
                    f"- Priority: {row.get('normalized_priority', '')}",
                    f"- Assigned team: {row.get('assigned_team', '') or 'Unassigned'}",
                    f"- Issues: {row.get('validation_issues', '')}",
                    "",
                ]
            )
    else:
        lines.append("- No record-level findings identified")

    REPORT_PATH.write_bytes(("\r\n".join(lines).rstrip() + "\r\n").encode("utf-8"))


def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Cleaned input file not found: {INPUT_PATH}. Run clean_workflow_data.py first."
        )

    rows = read_rows(INPUT_PATH)

    if not rows:
        raise ValueError("No rows found in cleaned input file.")

    for row in rows:
        row["validation_issues"] = "; ".join(validate_row(row))

    fieldnames = list(rows[0].keys())
    if "validation_issues" not in fieldnames:
        fieldnames.append("validation_issues")

    write_rows(OUTPUT_PATH, rows, fieldnames)
    write_report(rows)

    print(f"Wrote {OUTPUT_PATH}")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()




