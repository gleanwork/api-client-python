# Group


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `type`                                                                | [models.GroupType](../models/grouptype.md)                            | :heavy_check_mark:                                                    | The type of user group                                                |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | A unique identifier for the group. May be the same as name.           |
| `name`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Name of the group.                                                    |
| `datasource_instance`                                                 | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Datasource instance if the group belongs to one e.g. external groups. |