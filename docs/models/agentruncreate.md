# AgentRunCreate

Payload for creating a run.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `agent_id`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The ID of the agent to run.                                              |
| `input`                                                                  | [Optional[models.AgentRunCreateInput]](../models/agentruncreateinput.md) | :heavy_minus_sign:                                                       | The input to the agent.                                                  |
| `messages`                                                               | List[[models.Message](../models/message.md)]                             | :heavy_minus_sign:                                                       | The messages to pass an input to the agent.                              |