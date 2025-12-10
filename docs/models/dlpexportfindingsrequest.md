# DlpExportFindingsRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `export_type`                                                      | [Optional[models.ExportType]](../models/exporttype.md)             | :heavy_minus_sign:                                                 | The type of export to perform                                      |
| `filter_`                                                          | [Optional[models.DlpFindingFilter]](../models/dlpfindingfilter.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `file_name`                                                        | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The name of the file to export the findings to                     |
| `field_scope`                                                      | [Optional[models.FieldScope]](../models/fieldscope.md)             | :heavy_minus_sign:                                                 | Controls which fields to include in the export                     |
| `fields_to_exclude`                                                | List[*str*]                                                        | :heavy_minus_sign:                                                 | List of field names to exclude from the export                     |