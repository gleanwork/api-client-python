# AgentSchemas

Defines the structure and properties of an agent.


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `agent_id`                                              | *str*                                                   | :heavy_check_mark:                                      | The ID of the agent.                                    |
| `input_schema`                                          | [models.InputSchema](../models/inputschema.md)          | :heavy_check_mark:                                      | The schema for the agent input. In JSON Schema format.  |
| `output_schema`                                         | [models.OutputSchema](../models/outputschema.md)        | :heavy_check_mark:                                      | The schema for the agent output. In JSON Schema format. |