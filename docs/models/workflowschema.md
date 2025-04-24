# WorkflowSchema

The schema of a workflow, such as the goal and the steps.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `goal`                                                                                       | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | The goal of the workflow. This is passed into each step.                                     |
| `steps`                                                                                      | List[[models.WorkflowStep](../models/workflowstep.md)]                                       | :heavy_check_mark:                                                                           | N/A                                                                                          |
| `fields`                                                                                     | List[[models.WorkflowInputField](../models/workflowinputfield.md)]                           | :heavy_minus_sign:                                                                           | Fields can be used in the goal, step instruction templates, and tool config input templates. |
| `trigger`                                                                                    | [Optional[models.Trigger]](../models/trigger.md)                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |