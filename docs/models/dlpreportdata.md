# DlpReportData

Dlp report metadata which is used to construct report email


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `frequency`                                                             | [Optional[models.Frequency]](../models/frequency.md)                    | :heavy_minus_sign:                                                      | The frequency of the report                                             |
| `request_time`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)    | :heavy_minus_sign:                                                      | The time the report was requested, applicable only for one time reports |
| `report_name`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |
| `status`                                                                | [Optional[models.DlpSimpleResult]](../models/dlpsimpleresult.md)        | :heavy_minus_sign:                                                      | N/A                                                                     |