# AgentRunCreate

Payload for creating a run.


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `agent_id`                                   | *str*                                        | :heavy_check_mark:                           | The ID of the agent to run.                  |
| `input`                                      | Dict[str, *Any*]                             | :heavy_minus_sign:                           | The input to the agent.                      |
| `messages`                                   | List[[models.Message](../models/message.md)] | :heavy_minus_sign:                           | The messages to pass an input to the agent.  |
| `metadata`                                   | Dict[str, *Any*]                             | :heavy_minus_sign:                           | The metadata to pass to the agent.           |