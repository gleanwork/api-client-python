# PlatformSkillsListResponse


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `skills`                                                              | List[[models.PlatformSkill](../models/platformskill.md)]              | :heavy_check_mark:                                                    | Skills available to the user.                                         |
| `has_more`                                                            | *bool*                                                                | :heavy_check_mark:                                                    | Whether additional results are available.                             |
| `next_cursor`                                                         | *Nullable[str]*                                                       | :heavy_check_mark:                                                    | Cursor for the next page, or null when no more results are available. |
| `request_id`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | Platform-generated request ID for support correlation.                |