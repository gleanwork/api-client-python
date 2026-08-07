# ToolDefinitionsResponse


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `tools`                                                        | List[[models.ToolDefinition](../models/tooldefinition.md)]     | :heavy_check_mark:                                             | Definitions for the requested tools that exist on this server. |
| `not_found`                                                    | List[*str*]                                                    | :heavy_minus_sign:                                             | Requested names that do not exist on this server.              |