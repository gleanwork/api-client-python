# Activities
(*client.activities*)

## Overview

### Available Operations

* [report_activity](#report_activity) - Report client activity

## report_activity

Report events that happen to results within a Glean client UI, such as search result views and clicks.  This signal improves search quality.

### Example Usage

```python
from glean import Glean, models
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    g_client.client.activities.report_activity(feedback1={
        "tracking_tokens": [
            "trackingTokens",
        ],
        "event": models.Event.VIEW,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_glean_act_as`                                                                                                         | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |                                                                                                                          |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |                                                                                                                          |
| `feedback_query_parameter`                                                                                               | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | A URL encoded versions of Feedback. This is useful for requests.                                                         |                                                                                                                          |
| `feedback1`                                                                                                              | [Optional[models.Feedback]](../../models/feedback.md)                                                                    | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      | {<br/>"trackingTokens": [<br/>"trackingTokens"<br/>],<br/>"event": "VIEW"<br/>}                                          |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |                                                                                                                          |

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |