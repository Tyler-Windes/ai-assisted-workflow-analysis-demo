#### AI-Assisted Workflow Analysis Demo

##### Project Summary

This project works through a small, fictional workflow-intake dataset with inconsistent records, missing ownership, unclear priority labels, and incomplete closure notes.

The focus is on the analysis process: identifying data-quality issues, defining clearer intake rules, documenting review steps, and producing simple reporting outputs.

##### Business Problem

A fictional operations team receives workflow records from multiple intake channels. The records are useful, but inconsistent. Some have missing ownership, inconsistent priority labels, duplicate indicators, vague descriptions, incomplete closure notes, and inconsistent system-area names.

Without a structured intake model and validation process, the team cannot reliably prioritize work, report KPIs, or identify process improvement opportunities.

##### What Is Included

- A fictional workflow-intake dataset
- Cleaning and validation scripts
- A data dictionary and JSON schema
- SQL examples for quality checks and KPI review
- Requirements, user stories, and acceptance criteria
- Prompt examples for classification and validation review
- Stakeholder and data-quality summaries

##### Repository Structure

| Folder | Contents |
|---|---|
| `data/` | Raw and processed fictional sample data |
| `schema/` | JSON schema and data dictionary |
| `sql/` | Table definitions, quality checks, KPI queries, and gap-analysis queries |
| `docs/` | Requirements, process map, current/future analysis, API data-contract notes, validation, and audit trail |
| `prompts/` | Prompt templates and review notes |
| `reports/` | KPI, data-quality, and stakeholder summaries |
| `scripts/` | Cleaning and validation scripts |

##### Workflow

1. Raw workflow intake records are received as CSV data.
2. Cleaning logic normalizes priority, status, and system-area values.
3. Validation logic flags missing fields, inconsistent values, ownership gaps, duplicate indicators, and closure documentation gaps.
4. SQL examples query the cleaned data for quality checks, KPIs, and gap analysis.
5. Analyst documentation translates findings into requirements, user stories, acceptance criteria, process improvements, and stakeholder summaries.
6. Prompt examples outline classification, extraction, and validation-review support.
7. Manual review remains required before final decisions.

##### Suggested Reading Order

Start with:

1. `docs/business_context.md`
2. `README.md`
3. `schema/data_dictionary.md`
4. `reports/stakeholder_summary.md`
5. `docs/requirements.md`
6. `docs/user_stories.md`
7. `docs/acceptance_criteria.md`
8. `sql/02_data_quality_checks.sql`
9. `docs/api_data_contract.md`
10. `prompts/prompt_safety_notes.md`

Then inspect the scripts and outputs.

##### Run the Scripts

From the repository root, run `python .\scripts\clean_workflow_data.py`, then run `python .\scripts\validate_records.py`.

Outputs:

- `data/processed/workflow_items_clean.csv`
- `data/processed/workflow_items_validated.csv`
- `reports/data_quality_findings.md`

##### Limitations

This is a sample project using fictional sample data. It is not connected to a live ticketing system, production database, private employer system, or real customer environment.

Prompt examples are limited to classification, extraction, and validation-review support. They are not autonomous decision-making tools. Final classification, prioritization, and recommendations require manual review.

##### Project Status

This repository uses fictional data to show a practical analysis workflow. It is not a production system.


