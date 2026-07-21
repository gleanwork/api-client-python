# PlatformSkillVersionsListResponse


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `versions`                                                             | List[[models.PlatformSkillVersion](../models/platformskillversion.md)] | :heavy_check_mark:                                                     | Versions available for the skill.                                      |
| `has_more`                                                             | *bool*                                                                 | :heavy_check_mark:                                                     | Whether additional results are available.                              |
| `next_cursor`                                                          | *Nullable[str]*                                                        | :heavy_check_mark:                                                     | Cursor for the next page, or null when no more results are available.  |
| `request_id`                                                           | *str*                                                                  | :heavy_check_mark:                                                     | Platform-generated request ID for support correlation.                 |