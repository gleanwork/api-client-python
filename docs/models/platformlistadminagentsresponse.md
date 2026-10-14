# PlatformListAdminAgentsResponse

One page of agents.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `results`                                                               | List[[models.PlatformAdminAgent](../models/platformadminagent.md)]      | :heavy_check_mark:                                                      | The agents on this page, ordered by display_name and then by agent_id.  |
| `has_more`                                                              | *bool*                                                                  | :heavy_check_mark:                                                      | Whether more agents are available after this page.                      |
| `next_cursor`                                                           | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | Opaque cursor for the next page; null or absent when has_more is false. |
| `request_id`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | Request identifier for correlating this response.                       |