-- Count by status
SELECT status, COUNT(*) AS item_count
FROM workflow_items
GROUP BY status
ORDER BY item_count DESC;

-- Count by normalized priority
SELECT normalized_priority, COUNT(*) AS item_count
FROM workflow_items
GROUP BY normalized_priority
ORDER BY item_count DESC;

-- Count by customer impact
SELECT customer_impact, COUNT(*) AS item_count
FROM workflow_items
GROUP BY customer_impact
ORDER BY item_count DESC;

-- Open high-impact items
SELECT item_id, request_type, assigned_team, system_area
FROM workflow_items
WHERE status <> 'Closed'
  AND customer_impact = 'High';

-- Closure documentation completeness
SELECT
  COUNT(*) AS closed_items,
  SUM(CASE WHEN resolution_notes IS NOT NULL AND resolution_notes <> '' THEN 1 ELSE 0 END) AS closed_with_notes
FROM workflow_items
WHERE status = 'Closed';

-- Items by system area
SELECT system_area, COUNT(*) AS item_count
FROM workflow_items
GROUP BY system_area
ORDER BY item_count DESC;
