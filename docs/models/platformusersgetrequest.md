# PlatformUsersGetRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `user_id`                                                            | *str*                                                                | :heavy_check_mark:                                                   | Canonical Glean user ID, as the list returns it.                     | {user_id}                                                            |
| `include`                                                            | List[[models.PlatformUserInclude](../models/platformuserinclude.md)] | :heavy_minus_sign:                                                   | Optional fields to add to the user. Each value only adds fields.<br/> |                                                                      |