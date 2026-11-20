# McpServerBreakdown


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `server`                                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | MCP server name.                                                           |
| `total_calls`                                                              | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | Total number of MCP calls for this server in the specified time period.    |
| `active_users`                                                             | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | Total number of active users for this server in the specified time period. |
| `host_applications`                                                        | List[*str*]                                                                | :heavy_minus_sign:                                                         | Host applications using this server in the specified time period.          |