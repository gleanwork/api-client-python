# AutoAgentAction

Details of each action within Auto Agent (new actions supported for Auto Agent will be added to properties over time).


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `action_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | ID of each action within Auto Agent.                                 |
| `glean_search_config`                                                | [Optional[models.GleanSearchConfig]](../models/gleansearchconfig.md) | :heavy_minus_sign:                                                   | Configuration for the Glean Search action.                           |