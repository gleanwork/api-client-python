# ToolSets

The types of tools that the agent is allowed to use. Only works with FAST and ADVANCED `agent` values


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `enable_web_search`                                                                | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Whether the agent is allowed to use web search (default: true).                    |
| `enable_company_tools`                                                             | *Optional[bool]*                                                                   | :heavy_minus_sign:                                                                 | Whether the agent is allowed to search internal company resources (default: true). |