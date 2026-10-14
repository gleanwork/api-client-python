# PlatformUserFilter

A filter on one user field.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `field`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | The user field to filter on. The only supported field is is_active.                    |
| `values`                                                                               | List[*str*]                                                                            | :heavy_check_mark:                                                                     | The values to match. A user matches when any value matches.                            |
| `operator`                                                                             | [Optional[models.PlatformUserFilterOperator]](../models/platformuserfilteroperator.md) | :heavy_minus_sign:                                                                     | The only supported operator is EQUALS. Defaults to EQUALS.                             |