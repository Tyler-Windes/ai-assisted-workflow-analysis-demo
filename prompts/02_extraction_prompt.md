#### Extraction Prompt

Extract structured workflow fields from the provided intake note.

##### Fields to Extract

- request_type
- system_area
- priority_signal
- customer_impact_signal
- missing_information
- duplicate_indicator
- recommended_human_review_question

##### Rules

- Use null when information is not present.
- Do not infer facts beyond the note.
- Do not invent ownership, priority, impact, or closure details.
- Flag ambiguous records for human review.
- Return JSON only.

##### Human Review Requirement

Extracted fields are draft support only. A human reviewer must confirm the final structured record.

