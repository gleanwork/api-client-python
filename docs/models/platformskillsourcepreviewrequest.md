# PlatformSkillSourcePreviewRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `source_url`                                                               | *str*                                                                      | :heavy_check_mark:                                                         | GitHub URL for a skill directory, SKILL.md file, or repository to inspect. |
| `stream`                                                                   | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Whether to stream repository scan progress using server-sent events.       |