# ClientActivity
(*client.activity*)

## Overview

### Available Operations

* [report](#report) - Report document activity
* [feedback](#feedback) - Report client activity

## report

Report user activity that occurs on indexed documents such as viewing or editing. This signal improves search quality.

### Example Usage

```python
from glean import Glean, models
from glean.utils import parse_datetime
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
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

## feedback

Report events that happen to results within a Glean client UI, such as search result views and clicks.  This signal improves search quality.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    security=models.Security(
        act_as_bearer_token=os.getenv("GLEAN_ACT_AS_BEARER_TOKEN", ""),
    ),
) as g_client:

    g_client.client.activity.feedback(feedback1={
        "tracking_tokens": [
            "trackingTokens",
        ],
        "event": models.Event.VIEW,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `feedback_query_parameter`                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A URL encoded versions of Feedback. This is useful for requests.    |                                                                     |
| `feedback1`                                                         | [Optional[models.Feedback]](../../models/feedback.md)               | :heavy_minus_sign:                                                  | N/A                                                                 | {<br/>"trackingTokens": [<br/>"trackingTokens"<br/>],<br/>"event": "VIEW"<br/>} |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |