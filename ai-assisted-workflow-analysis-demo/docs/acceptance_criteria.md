#### Acceptance Criteria

##### AC-001: Priority Normalization

Given a record is submitted with priority `urgent` or `P1`,  
when the record is processed,  
then the normalized priority should be set to `High`.

##### AC-002: Closed Record Validation

Given a record has status `Closed`,  
when validation is performed,  
then resolution notes must not be blank.

##### AC-003: Ownership Validation

Given a record has status `In Progress`,  
when validation is performed,  
then assigned team must not be blank.

##### AC-004: Duplicate Review

Given a record includes a `duplicate_of` value,  
when validation is reviewed,  
then the analyst should verify that the referenced item exists and is actually related.

##### AC-005: Human Review of AI Output

Given an AI prompt produces a classification, extraction, or validation suggestion,  
when the output is used in the workflow,  
then the output must be treated as draft until reviewed by a human.

##### AC-006: Reporting Readiness

Given KPI summaries are prepared,  
when data-quality findings exist,  
then those findings should be reviewed before the KPI summary is treated as decision-ready.

