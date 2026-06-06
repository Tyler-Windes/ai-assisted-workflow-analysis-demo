#### Audit Trail

| Step | Input | Transformation | Output | Review Point |
|---|---|---|---|---|
| Raw intake | `workflow_intake_sample.csv` | None | Raw dataset | Confirm fictional data only |
| Cleaning | Raw CSV | Normalize priority, status, and system-area values | `workflow_items_clean.csv` | Review normalization rules |
| Validation | Clean CSV | Apply quality checks | `workflow_items_validated.csv` | Review flagged records |
| Reporting | Validated CSV | Summarize findings | KPI and quality reports | Review before stakeholder use |
| Documentation | Findings and reports | Translate into requirements and recommendations | Docs folder | Confirm claims are supported |
| AI support | Prompt examples | Draft classification/extraction/validation support | Prompt outputs if used | Human review required |

