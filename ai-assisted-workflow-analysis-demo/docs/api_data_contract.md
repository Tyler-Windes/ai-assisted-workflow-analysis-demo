#### API Data Contract

##### Purpose

This document describes the expected shape of a workflow item if the intake data were exchanged through an API or another structured integration point.

The project does not connect to a live API. This data contract documents the expected workflow record structure before any implementation work.

##### Example Payload Shape

| Field | Example |
|---|---|
| item_id | WF-001 |
| source | email |
| submitted_date | 2026-05-01 |
| request_type | Access Issue |
| description | User cannot access reporting folder |
| reported_priority | High |
| normalized_priority | High |
| assigned_team | Support |
| status | In Progress |
| customer_impact | Medium |
| system_area | Reporting |
| missing_info_flag | false |

##### Contract Notes

- `item_id` should uniquely identify each workflow record.
- `source` should use approved intake-channel values.
- `submitted_date` should use a consistent date format.
- `request_type`, `status`, `customer_impact`, and `system_area` should use controlled values where possible.
- `normalized_priority` should be derived from the submitted priority value.
- `missing_info_flag` should identify records that need analyst review.
- Resolution notes should be required before a record is treated as fully closed.

##### Review Considerations

- Required fields should be validated before reporting.
- Non-standard values should be flagged for review instead of silently accepted.
- Duplicate indicators should be reviewed before records are removed or merged.
- Manual review should remain part of the process before final recommendations are made.
