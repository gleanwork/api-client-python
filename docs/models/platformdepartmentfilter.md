# PlatformDepartmentFilter

A filter on one department field.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `field`                                                                                            | *str*                                                                                              | :heavy_check_mark:                                                                                 | The department field to filter on. The only supported field is is_active.                          |
| `values`                                                                                           | List[*str*]                                                                                        | :heavy_check_mark:                                                                                 | The values to match. A department matches when any value matches.                                  |
| `operator`                                                                                         | [Optional[models.PlatformDepartmentFilterOperator]](../models/platformdepartmentfilteroperator.md) | :heavy_minus_sign:                                                                                 | The only supported operator is EQUALS. Defaults to EQUALS.                                         |