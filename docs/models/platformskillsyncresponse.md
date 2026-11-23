# PlatformSkillSyncResponse


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `commit_sha`                                           | *str*                                                  | :heavy_check_mark:                                     | Git commit SHA now associated with the skill.          |
| `is_updated`                                           | *bool*                                                 | :heavy_check_mark:                                     | Whether this request created a new skill version.      |
| `request_id`                                           | *str*                                                  | :heavy_check_mark:                                     | Platform-generated request ID for support correlation. |