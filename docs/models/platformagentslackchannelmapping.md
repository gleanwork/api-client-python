# PlatformAgentSlackChannelMapping

A Slack channel the agent is mapped to.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `channel_id`                                                     | *str*                                                            | :heavy_check_mark:                                               | ID of the Slack channel.                                         |
| `auto_engage`                                                    | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Whether the agent engages with messages without being mentioned. |