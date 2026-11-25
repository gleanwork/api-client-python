# ToolInfo


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `metadata`                                                                  | [Optional[models.ToolMetadata]](../models/toolmetadata.md)                  | :heavy_minus_sign:                                                          | The manifest for a tool that can be used to augment Glean Assistant.        |
| `parameters`                                                                | Dict[str, [models.WriteActionParameter](../models/writeactionparameter.md)] | :heavy_minus_sign:                                                          | Parameters supported by the tool.                                           |