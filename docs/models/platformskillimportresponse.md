# PlatformSkillImportResponse


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `skills`                                                 | List[[models.PlatformSkill](../models/platformskill.md)] | :heavy_check_mark:                                       | Independently persisted skills in request order.         |
| `request_id`                                             | *str*                                                    | :heavy_check_mark:                                       | Platform-generated request ID for support correlation.   |