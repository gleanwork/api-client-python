# UpdateDlpConfigRequest


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `config`                                                                        | [Optional[models.DlpConfig]](../models/dlpconfig.md)                            | :heavy_minus_sign:                                                              | Detailed configuration of what documents and sensitive content will be scanned. |
| `frequency`                                                                     | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Only "ONCE" is supported for reports.                                           |