# GetToolServerToolsRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `server_id`                                        | *str*                                              | :heavy_check_mark:                                 | Unique identifier of the tool server.              |
| `tool_names`                                       | List[*str*]                                        | :heavy_check_mark:                                 | Tool names to look up on this server. Maximum 100. |