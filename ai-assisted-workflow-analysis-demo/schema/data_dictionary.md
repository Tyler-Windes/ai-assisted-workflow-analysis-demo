#### Data Dictionary

| Field | Type | Required | Allowed Values | Description | Data Quality Rule |
|---|---|---|---|---|---|
| item_id | string | yes | WF-### | Unique workflow item identifier | Must be unique |
| source | string | yes | email, form, chat, api | Intake channel | Must be approved source |
| submitted_date | date | yes | YYYY-MM-DD | Date submitted | Must be parseable |
| request_type | string | yes | controlled list recommended | Type of request | Should map to approved category |
| description | string | yes | free text | Summary of issue/request | Must not be vague or blank |
| reported_priority | string | yes | raw intake value | Priority as submitted | Must be normalized |
| normalized_priority | string | generated | High, Medium, Low, Needs Review | Standardized priority | Must be derived consistently |
| assigned_team | string | conditional | team name | Responsible team | Required if In Progress |
| status | string | yes | Open, In Progress, Closed, Needs Review | Workflow status | Must be approved status |
| resolution_notes | string | conditional | free text | Closure notes | Required if Closed |
| customer_impact | string | yes | High, Medium, Low | Business impact level | Must be approved value |
| system_area | string | yes | controlled list recommended | Affected system area | Must be standardized |
| duplicate_of | string | no | item_id | Link to original item | Must reference valid item if populated |
| missing_info_flag | boolean | yes | true, false | Indicates incomplete intake | Must be boolean |
| validation_issues | string | generated | semicolon-delimited findings | Validation findings | Should be reviewed before reporting |

##### Representation Note

The CSV demo stores boolean values as `true`/`false` text because CSV files do not preserve native boolean types. In JSON payload examples, `missing_info_flag` should be represented as a boolean.

