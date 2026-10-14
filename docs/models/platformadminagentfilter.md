# PlatformAdminAgentFilter

A filter on one agent field.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `field`                                                                                            | *str*                                                                                              | :heavy_check_mark:                                                                                 | The agent field to filter on. The only supported field is is_active.                               |
| `values`                                                                                           | List[*str*]                                                                                        | :heavy_check_mark:                                                                                 | The values to match. An agent matches when any value matches.                                      |
| `operator`                                                                                         | [Optional[models.PlatformAdminAgentFilterOperator]](../models/platformadminagentfilteroperator.md) | :heavy_minus_sign:                                                                                 | The only supported operator is EQUALS. Defaults to EQUALS.                                         |