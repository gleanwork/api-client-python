# Calendar
(*client.calendar*)

## Overview

### Available Operations

* [get_events](#get_events) - Read events

## get_events

Read detailed information about the given event ids.

### Example Usage

```python
from glean import Glean
import os


with Glean(
    bearer_auth=os.getenv("GLEAN_BEARER_AUTH", ""),
) as g_client:

    res = g_client.client.calendar.get_events(ids=[], auth_tokens=[
        {
            "access_token": "123abc",
            "datasource": "gmail",
            "scope": "email profile https://www.googleapis.com/auth/gmail.readonly",
            "token_type": "Bearer",
            "auth_user": "1",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                                    | List[*str*]                                                                                                              | :heavy_check_mark:                                                                                                       | The ids of the calendar events to be retrieved.                                                                          |
| `x_scio_actas`                                                                                                           | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Email address of a user on whose behalf the request is intended to be made (should be non-empty only for global tokens). |
| `x_glean_auth_type`                                                                                                      | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | Auth type being used to access the endpoint (should be non-empty only for global tokens).                                |
| `auth_tokens`                                                                                                            | List[[models.AuthToken](../../models/authtoken.md)]                                                                      | :heavy_minus_sign:                                                                                                       | Auth tokens if client-side authentication.                                                                               |
| `datasource`                                                                                                             | *Optional[str]*                                                                                                          | :heavy_minus_sign:                                                                                                       | The app or other repository type from which the event was extracted                                                      |
| `annotate`                                                                                                               | *Optional[bool]*                                                                                                         | :heavy_minus_sign:                                                                                                       | Whether relevant content and documents, via GeneratedAttachments, should be attached to the events.                      |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetEventsResponse](../../models/geteventsresponse.md)**

### Errors

| Error Type        | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.GleanError | 4XX, 5XX          | \*/\*             |