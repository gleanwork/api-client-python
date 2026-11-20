# PlatformActionSummary


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `tool_id`                                          | *str*                                              | :heavy_check_mark:                                 | Unique identifier of the action.                   |
| `display_name`                                     | *str*                                              | :heavy_check_mark:                                 | Display name of the action.                        |
| `type`                                             | *Optional[str]*                                    | :heavy_minus_sign:                                 | Tool type.                                         |
| `auth_type`                                        | *Optional[str]*                                    | :heavy_minus_sign:                                 | Authentication type required by the action.        |
| `write_action_type`                                | *Optional[str]*                                    | :heavy_minus_sign:                                 | Write-action execution type.                       |
| `is_setup_finished`                                | *Optional[bool]*                                   | :heavy_minus_sign:                                 | Whether this action has been fully configured.     |
| `data_source`                                      | *Optional[str]*                                    | :heavy_minus_sign:                                 | Kind of knowledge the action accesses or modifies. |