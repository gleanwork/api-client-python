# PlatformAgentRunResponsesRequest

Invocation-scoped decisions for the complete pending approval batch.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `run_id`                                                                                                   | *str*                                                                                                      | :heavy_check_mark:                                                                                         | ID of the run whose pending approvals are being answered. Must belong to the agent identified in the path. |
| `responses`                                                                                                | List[[models.PlatformAgentRunApprovalDecision](../models/platformagentrunapprovaldecision.md)]             | :heavy_check_mark:                                                                                         | One decision per pending interaction. Interaction IDs must be unique.                                      |