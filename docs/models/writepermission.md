# WritePermission

Describes the write permissions levels that a user has for a specific feature


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `scope_type`                                                                         | [Optional[models.ScopeType]](../models/scopetype.md)                                 | :heavy_minus_sign:                                                                   | Describes the scope for a ReadPermission, WritePermission, or GrantPermission object |
| `create`                                                                             | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | True if user has create permission for this feature and scope                        |
| `update`                                                                             | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | True if user has update permission for this feature and scope                        |
| `delete`                                                                             | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | True if user has delete permission for this feature and scope                        |