# DlpIssueFilter

Filter for DLP issues. Includes document-level filters and issue-specific filters.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `search_text`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Text to search for in issue fields.                              |
| `statuses`                                                       | List[[models.DlpIssueStatus](../models/dlpissuestatus.md)]       | :heavy_minus_sign:                                               | Filter by one or more issue statuses.                            |
| `assignee_id`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Filter by assignee user ID.                                      |
| `info_type`                                                      | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `regex_id`                                                       | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `report_ids`                                                     | List[*str*]                                                      | :heavy_minus_sign:                                               | Filter by one or more report/policy IDs.                         |
| `doc_id`                                                         | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `datasource`                                                     | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `visibility`                                                     | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `severities`                                                     | List[[models.DlpSeverity](../models/dlpseverity.md)]             | :heavy_minus_sign:                                               | Filter by one or more severity levels.                           |
| `time_range`                                                     | [Optional[models.TimeRangeFilter]](../models/timerangefilter.md) | :heavy_minus_sign:                                               | N/A                                                              |