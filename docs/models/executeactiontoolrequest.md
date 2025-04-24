# ExecuteActionToolRequest


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `action_run_id`                                                             | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Unique identifier for this actionRun execution event.                       |
| `name`                                                                      | *str*                                                                       | :heavy_check_mark:                                                          | The name of the tool.                                                       |
| `action_instance_id`                                                        | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | Unique identifier of an action instance.                                    |
| `parameters`                                                                | Dict[str, [models.WriteActionParameter](../models/writeactionparameter.md)] | :heavy_minus_sign:                                                          | The parameters to be passed to the tool for action.                         |