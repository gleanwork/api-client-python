# WorkflowStep


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The id of this step in the workflow.                               |
| `label`                                                            | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | A label associated with the step.                                  |
| `instruction_template`                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The templatic input to the workflow step.                          |
| `tool_config`                                                      | List[[models.WorkflowToolConfig](../models/workflowtoolconfig.md)] | :heavy_minus_sign:                                                 | N/A                                                                |
| `memory_config`                                                    | [Optional[models.MemoryConfig]](../models/memoryconfig.md)         | :heavy_minus_sign:                                                 | Memory used to plan the tool's inputs.                             |