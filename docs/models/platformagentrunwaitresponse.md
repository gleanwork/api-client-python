# PlatformAgentRunWaitResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `run`                                                              | [Optional[models.PlatformAgentRun]](../models/platformagentrun.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `messages`                                                         | List[[models.PlatformMessage](../models/platformmessage.md)]       | :heavy_minus_sign:                                                 | Messages returned by the completed run.                            |
| `request_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | Platform-generated request ID for support correlation.             |