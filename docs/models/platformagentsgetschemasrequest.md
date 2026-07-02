# PlatformAgentsGetSchemasRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `agent_id`                                         | *str*                                              | :heavy_check_mark:                                 | ID of the agent whose schemas should be retrieved. |
| `include_tools`                                    | *Optional[bool]*                                   | :heavy_minus_sign:                                 | Whether to include tool metadata in the response.  |