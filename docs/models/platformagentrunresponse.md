# PlatformAgentRunResponse

Persisted agent run snapshot with a request ID for support correlation.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `run`                                                                                                | [models.PlatformDurableAgentRun](../models/platformdurableagentrun.md)                               | :heavy_check_mark:                                                                                   | Agent run state, pending tool approvals, and output available independently of the creation request. |
| `request_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | Platform-generated request ID for support correlation.                                               |