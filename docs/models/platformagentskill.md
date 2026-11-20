# PlatformAgentSkill

A skill defined inline in the agent. Reference a published skill through `dependencies` instead.



## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `display_name`                                                                             | *str*                                                                                      | :heavy_check_mark:                                                                         | Human-readable skill name.                                                                 |
| `main_content`                                                                             | *str*                                                                                      | :heavy_check_mark:                                                                         | Main skill content, inlined from `SKILL.md`.                                               |
| `files`                                                                                    | List[[models.PlatformSkillSourcePreviewFile](../models/platformskillsourcepreviewfile.md)] | :heavy_minus_sign:                                                                         | Additional files bundled in the skill folder.                                              |