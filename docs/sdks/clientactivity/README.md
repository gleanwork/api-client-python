# ClientActivity
(*client.activity*)

## Overview

### Available Operations

* [report](#report) - Report document activity

## report

Report user activity that occurs on indexed documents such as viewing or editing. This signal improves search quality.

### Example Usage

```python
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activity.report(events=[
        {
            "action": models.ActivityEventAction.HISTORICAL_VIEW,
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
        {
            "action": models.ActivityEventAction.SEARCH,
            "params": {
                "query": "query",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/search?q=query",
        },
        {
            "action": models.ActivityEventAction.VIEW,
            "params": {
                "duration": 20,
                "referrer": "https://example.com/document",
            },
            "timestamp": parse_datetime("2000-01-23T04:56:07.000Z"),
            "url": "https://example.com/",
        },
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `events`                                                            | List[[models.ActivityEvent](../../models/activityevent.md)]         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |