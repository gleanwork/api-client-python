# WorkflowSlackConfig

Configuration for the Agent's behaviour in Slack


## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `enabled`                                                                                             | *Optional[bool]*                                                                                      | :heavy_minus_sign:                                                                                    | Indicates whether the Agent can be used in Slack for the associated channels.                         |
| `instance_channels`                                                                                   | Dict[str, List[*str*]]                                                                                | :heavy_minus_sign:                                                                                    | Map of data source instance name corresponding to slack / slack enterprise to a list of channel ids.<br/> |
| `sharing_settings`                                                                                    | [Optional[models.SharingSettings]](../models/sharingsettings.md)                                      | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |