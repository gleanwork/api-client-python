# DatasourceMembershipDefinition

describes the membership row of a group. Only one of memberUserId and memberGroupName can be specified.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `group_name`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | The group for which the membership is specified                       |
| `member_user_id`                                                      | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | If the member is a user, then the email or datasource id for the user |
| `member_group_name`                                                   | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | If the member is a group, then the name of the member group           |