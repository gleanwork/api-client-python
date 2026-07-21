# PlatformSkillsListVersionsRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `skill_id`                                         | *str*                                              | :heavy_check_mark:                                 | Glean skill ID.                                    |
| `page_size`                                        | *Optional[int]*                                    | :heavy_minus_sign:                                 | Maximum number of versions to return.              |
| `cursor`                                           | *Optional[str]*                                    | :heavy_minus_sign:                                 | Opaque pagination cursor from a previous response. |