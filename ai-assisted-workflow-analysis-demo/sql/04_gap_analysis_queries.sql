-- Records violating future-state ownership rule
SELECT item_id, status, assigned_team
FROM workflow_items
WHERE status IN ('Open', 'In Progress')
  AND (assigned_team IS NULL OR assigned_team = '');

-- Records violating future-state closure documentation rule
SELECT item_id, status, resolution_notes
FROM workflow_items
WHERE status = 'Closed'
  AND (resolution_notes IS NULL OR resolution_notes = '');

-- Intake records needing human review
SELECT item_id, request_type, description, missing_info_flag, normalized_priority, system_area
FROM workflow_items
WHERE missing_info_flag = TRUE
   OR normalized_priority = 'Needs Review'
   OR system_area = 'Needs Review';

-- Duplicate or related records requiring analyst review
SELECT item_id, duplicate_of, description
FROM workflow_items
WHERE duplicate_of IS NOT NULL AND duplicate_of <> '';
