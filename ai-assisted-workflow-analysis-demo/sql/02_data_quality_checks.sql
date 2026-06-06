-- Records missing ownership while in progress
SELECT item_id, status, assigned_team
FROM workflow_items
WHERE status = 'In Progress'
  AND (assigned_team IS NULL OR assigned_team = '');

-- Closed records missing resolution notes
SELECT item_id, status, resolution_notes
FROM workflow_items
WHERE status = 'Closed'
  AND (resolution_notes IS NULL OR resolution_notes = '');

-- Non-standard raw priority values for review
SELECT item_id, reported_priority, normalized_priority
FROM workflow_items
WHERE normalized_priority = 'Needs Review';

-- Potential duplicates
SELECT item_id, duplicate_of, description
FROM workflow_items
WHERE duplicate_of IS NOT NULL AND duplicate_of <> '';

-- Records marked as missing information
SELECT item_id, request_type, description, assigned_team
FROM workflow_items
WHERE missing_info_flag = TRUE;

-- Records with validation issues
SELECT item_id, validation_issues
FROM workflow_items
WHERE validation_issues IS NOT NULL AND validation_issues <> '';
