# McpToolBreakdown


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `tool`                                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | MCP tool name.                                                           |
| `total_calls`                                                            | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Total number of MCP calls for this tool in the specified time period.    |
| `active_users`                                                           | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Total number of active users for this tool in the specified time period. |
| `host_applications`                                                      | List[*str*]                                                              | :heavy_minus_sign:                                                       | Host applications using this tool in the specified time period.          |