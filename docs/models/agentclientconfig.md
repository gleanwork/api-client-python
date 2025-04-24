# AgentClientConfig

Describes the configurations that GleanChat has based on an AgentConfig.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `agent_config`                                                                | [Optional[models.AgentConfig]](../models/agentconfig.md)                      | :heavy_minus_sign:                                                            | Describes the agent that executes the request.                                |
| `input_char_limit`                                                            | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | The character limit of an input to GleanChat under the specified AgentConfig. |