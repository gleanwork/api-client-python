# Insights
(*client.insights*)

## Overview

### Available Operations

* [retrieve](#retrieve) - Read insights

## retrieve

Reads the aggregate information for each user, query, and content.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        api_token=os.getenv("GLEAN_API_TOKEN", ""),
    ),
) as g_client:

    res = g_client.client.insights.retrieve(categories=[
        models.InsightsRequestCategory.COLLECTIONS,
        models.InsightsRequestCategory.SHORTCUTS,
        models.InsightsRequestCategory.ANNOUNCEMENTS,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `categories`                                                                                                              | List[[models.InsightsRequestCategory](../../models/insightsrequestcategory.md)]                                           | :heavy_check_mark:                                                                                                        | Categories of data requested. Request can include single or multiple types.                                               |
| `departments`                                                                                                             | List[*str*]                                                                                                               | :heavy_minus_sign:                                                                                                        | Departments that the data is requested for. If this is empty, corresponds to whole company.                               |
| `day_range`                                                                                                               | [Optional[models.Period]](../../models/period.md)                                                                         | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `ai_app_request_options`                                                                                                  | [Optional[models.InsightsAiAppRequestOptions]](../../models/insightsaiapprequestoptions.md)                               | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `agents_request_options`                                                                                                  | [Optional[models.InsightsAgentsRequestOptions]](../../models/insightsagentsrequestoptions.md)                             | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `assistant_activity_types`                                                                                                | List[[models.AssistantActivityType](../../models/assistantactivitytype.md)]                                               | :heavy_minus_sign:                                                                                                        | Types of activity that should count in the definition of an Assistant Active User. Affects only insights for AI category. |
| `disable_per_user_insights`                                                                                               | *Optional[bool]*                                                                                                          | :heavy_minus_sign:                                                                                                        | If true, suppresses the generation of per-user Insights in the response. Default is false.                                |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.InsightsResponse](../../models/insightsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |