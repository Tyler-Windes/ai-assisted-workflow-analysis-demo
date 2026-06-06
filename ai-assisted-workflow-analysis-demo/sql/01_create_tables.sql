CREATE TABLE workflow_items (
    item_id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    submitted_date DATE NOT NULL,
    request_type TEXT NOT NULL,
    description TEXT NOT NULL,
    reported_priority TEXT NOT NULL,
    normalized_priority TEXT,
    assigned_team TEXT,
    status TEXT NOT NULL,
    resolution_notes TEXT,
    customer_impact TEXT NOT NULL,
    system_area TEXT NOT NULL,
    duplicate_of TEXT,
    missing_info_flag BOOLEAN NOT NULL,
    validation_issues TEXT
);
