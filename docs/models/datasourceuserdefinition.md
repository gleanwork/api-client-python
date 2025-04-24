# DatasourceUserDefinition

describes a user in the datasource


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `email`                                                          | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `user_id`                                                        | *Optional[str]*                                                  | :heavy_minus_sign:                                               | To be supplied if the user id in the datasource is not the email |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `is_active`                                                      | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | set to false if the user is a former employee or a bot           |