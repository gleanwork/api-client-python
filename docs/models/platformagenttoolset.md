# PlatformAgentToolset

A tool provider and the subset of its tools available to the agent.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `tool_provider_id`                                                               | *str*                                                                            | :heavy_check_mark:                                                               | ID of the tool provider, or `native` for built-in Glean tools.                   |
| `selected_tools`                                                                 | List[[models.PlatformAgentSelectedTool](../models/platformagentselectedtool.md)] | :heavy_minus_sign:                                                               | Tools from the provider that are exposed to the agent.                           |
| `customisation_data`                                                             | [Optional[models.CustomisationData]](../models/customisationdata.md)             | :heavy_minus_sign:                                                               | Settings applied to every tool in this provider entry.                           |