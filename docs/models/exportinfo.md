# ExportInfo


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `created_by`                                                       | [Optional[models.DlpPerson]](../models/dlpperson.md)               | :heavy_minus_sign:                                                 | Details about the person who created this report/policy.           |
| `start_time`                                                       | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Timestamp at which this export started.                            |
| `end_time`                                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Timestamp at which this export completed.                          |
| `export_id`                                                        | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The ID of the export                                               |
| `file_name`                                                        | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The name of the file to export the findings to                     |
| `filter_`                                                          | [Optional[models.DlpFindingFilter]](../models/dlpfindingfilter.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `status`                                                           | [Optional[models.ExportInfoStatus]](../models/exportinfostatus.md) | :heavy_minus_sign:                                                 | The status of the export                                           |