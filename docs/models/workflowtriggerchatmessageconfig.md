# WorkflowTriggerChatMessageConfig

Trigger configuration for a chat message sent by a user.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `prompts`                                                                | List[[models.Prompt](../models/prompt.md)]                               | :heavy_minus_sign:                                                       | Simpler prompts for ChatMessage triggers, i.e. conversational starters   |
| `slack_config`                                                           | [Optional[models.WorkflowSlackConfig]](../models/workflowslackconfig.md) | :heavy_minus_sign:                                                       | Configuration for the Agent's behaviour in Slack                         |