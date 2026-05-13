# Client.Insights

## Overview

### Available Operations

* [retrieve](#retrieve) - Get insights

## retrieve

Gets the aggregate usage insights data displayed in the Insights Dashboards.

### Example Usage

<!-- UsageSnippet language="python" operationID="insights" method="post" path="/rest/api/v1/insights" -->
```python
from glean.api_client import Glean
import os


with Glean(
    api_token=os.getenv("GLEAN_API_TOKEN", ""),
) as glean:

    res = glean.client.insights.retrieve()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | The client's preferred locale in rfc5646 format (e.g. `en`, `ja`, `pt-BR`). If omitted, the `Accept-Language` will be used. If not present or not supported, defaults to the closest match or `en`. |
| `overview_request`                                                                                                                                                                                  | [Optional[models.InsightsOverviewRequest]](../../models/insightsoverviewrequest.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `assistant_request`                                                                                                                                                                                 | [Optional[models.InsightsAssistantRequest]](../../models/insightsassistantrequest.md)                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `agents_request`                                                                                                                                                                                    | [Optional[models.AgentsInsightsV2Request]](../../models/agentsinsightsv2request.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `mcp_breakdown_request`                                                                                                                                                                             | [Optional[models.McpBreakdownInsightsRequest]](../../models/mcpbreakdowninsightsrequest.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                  | N/A                                                                                                                                                                                                 |
| `disable_per_user_insights`                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | If true, suppresses the generation of per-user Insights in the response. Default is false.                                                                                                          |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.InsightsResponse](../../models/insightsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |