#### Classification Prompt

Use this prompt to classify workflow intake records into the approved request types.

##### Task

Classify each workflow intake record into one approved request type:

- Access Issue
- Data Quality Issue
- Process Exception
- Reporting Request
- System Error
- Other
- Needs Review

##### Rules

- Do not invent missing facts.
- If the description is unclear, classify the record as `Needs Review`.
- If more than one category may apply, choose the most specific category and include a confidence note.
- Return structured JSON only.
- Do not make final business decisions.

##### Output Format

Return the following fields:

| Field | Description |
|---|---|
| item_id | Workflow item identifier |
| recommended_request_type | Suggested request type |
| confidence | High, Medium, or Low |
| reason | Short explanation for the classification |
| human_review_required | True or false |

##### Review Requirement

Prompt output should be treated as draft classification support. Final classification requires manual review.
