# ToolsCallParameter


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `name`                                                                  | *str*                                                                   | :heavy_check_mark:                                                      | The name of the parameter                                               |
| `value`                                                                 | *str*                                                                   | :heavy_check_mark:                                                      | The value of the parameter (for primitive types)                        |
| `items`                                                                 | List[[models.ToolsCallParameter](../models/toolscallparameter.md)]      | :heavy_minus_sign:                                                      | The value of the parameter (for array types)                            |
| `properties`                                                            | Dict[str, [models.ToolsCallParameter](../models/toolscallparameter.md)] | :heavy_minus_sign:                                                      | The value of the parameter (for object types)                           |